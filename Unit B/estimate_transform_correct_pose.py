from lego_robot import *
from slam_b_library import filter_step
from project_landmarks import\
     compute_scanner_cylinders, write_cylinders
from math import sqrt, atan2
import sys
def find_cylinder_pairs(cylinders, reference_cylinders, max_radius):
    cylinder_pairs = []
    index_j = len(reference_cylinders)
    for i in xrange(len(cylinders)): # Loop over every world cylinder
        min_dist = float("inf") # Setting a very large value initially
        for j in xrange(len(reference_cylinders)): # Loop over every reference cylinder
            dist = sqrt((cylinders[i][0] - reference_cylinders[j][0])**2 + (cylinders[i][1] - reference_cylinders[j][1])**2) 
            # Take the world cylinder and calculate the distance between it and every reference cylinder.
            # Assign the world cylinder to the reference cylinder for which the distance is the shortest provided the distance doesn't exceed the maximum allowable radius.
            if(dist<min_dist):
                min_dist = dist
                index_j = j
        if(min_dist<max_radius):
            cylinder_pairs.append((i, index_j))
        # Loop this over for every world cylinder found.

    return cylinder_pairs

def compute_center(point_list):
    # Safeguard against empty list.
    if not point_list:
        return (0.0, 0.0)
    # If not empty, sum up and divide.
    sx = sum([p[0] for p in point_list])
    sy = sum([p[1] for p in point_list])
    return (float(sx) / len(point_list), float(sy) / len(point_list))
def estimate_transform(left_list, right_list, fix_scale = False):
    # Compute left and right center of mass.
    lc = compute_center(left_list)
    rc = compute_center(right_list)
    cs, ss, rr, ll = 0, 0, 0, 0 

    for i in xrange(0, len(left_list)):
        # Reduced left coordinates
        lx_dash = left_list[i][0] - lc[0]
        ly_dash = left_list[i][1] - lc[1]

        # Reduced right coordinates
        rx_dash = right_list[i][0] - rc[0]
        ry_dash = right_list[i][1] - rc[1]
        
        # Cosine sum and Sine sum        
        cs += rx_dash*lx_dash + ry_dash * ly_dash
        ss += - rx_dash*ly_dash + ry_dash *lx_dash
        
        # Square length of the vectors
        rr += rx_dash * rx_dash + ry_dash *ry_dash
        ll += lx_dash * lx_dash + ly_dash * ly_dash
        
        if(not rr and not ll):
            return None
        
        # la = lambda (scaling)
        # c = cosine
        # s = sine
        # tx = translation along x
        # ty = translation along y
        la = 1 if (fix_scale) else sqrt (rr/ll)
            
        leng = sqrt(cs**2 + ss**2)
        c = cs/leng
        s = ss/leng 
        
        tx = rc[0] - la*c*lc[0] + la*s*lc[1]
        ty = rc[1] - la*s*lc[0] - la*c*lc[1]
        
        return la, c, s, tx, ty

def apply_transform(trafo, p):
    la, c, s, tx, ty = trafo
    lac = la * c
    las = la * s
    x = lac * p[0] - las * p[1] + tx
    y = las * p[0] + lac * p[1] + ty
    return (x, y)

def correct_pose(pose, trafo):
    
    x, y = apply_transform(trafo, pose[:2])
    
    theta = pose[2] + atan2(trafo[2], trafo[1])
    
    return (x, y, theta)
if __name__ == '__main__':
    # The constants we used for the filter_step.
    scanner_displacement = 30.0
    ticks_to_mm = 0.349
    robot_width = 150.0

    # The constants we used for the cylinder detection in our scan.
    minimum_valid_distance = 20.0
    depth_jump = 100.0
    cylinder_offset = 90.0

    # The maximum distance allowed for cylinder assignment.
    max_cylinder_distance = 400.0

    # The start pose we obtained miraculously.
    pose = (1850.0, 1897.0, 3.717551306747922)

    # Read the logfile which contains all scans.
    logfile = LegoLogfile()
    logfile.read("robot4_motors.txt")
    logfile.read("robot4_scan.txt")

    # Also read the reference cylinders (this is our map).
    logfile.read("robot_arena_landmarks.txt")
    reference_cylinders = [l[1:3] for l in logfile.landmarks]

    out_file = file("apply_transform.txt", "w")
    for i in xrange(len(logfile.scan_data)):
        # Compute the new pose.
        pose = filter_step(pose, logfile.motor_ticks[i],
                           ticks_to_mm, robot_width,
                           scanner_displacement)

        # Extract cylinders, also convert them to world coordinates.
        cartesian_cylinders = compute_scanner_cylinders(
            logfile.scan_data[i],
            depth_jump, minimum_valid_distance, cylinder_offset)
        world_cylinders = [LegoLogfile.scanner_to_world(pose, c)
                           for c in cartesian_cylinders]

        # For every cylinder, find the closest reference cylinder.
        cylinder_pairs = find_cylinder_pairs(
            world_cylinders, reference_cylinders, max_cylinder_distance)

        # Estimate a transformation using the cylinder pairs.
        trafo = estimate_transform(
            [world_cylinders[pair[0]] for pair in cylinder_pairs],
            [reference_cylinders[pair[1]] for pair in cylinder_pairs],
            fix_scale = True)

        # Transform the cylinders using the estimated transform.
        transformed_world_cylinders = []
        if trafo:
            transformed_world_cylinders =\
                [apply_transform(trafo, c) for c in
                 [world_cylinders[pair[0]] for pair in cylinder_pairs]]

        # Also apply the trafo to correct the position and heading.
        if trafo:
            pose = correct_pose(pose, trafo)

        # Write to file.
        # The pose.
        out_file.write("F %f %f %f\n" % pose)
        # The detected cylinders in the scanner's coordinate system.
        write_cylinders(out_file, "D C", cartesian_cylinders)
        # The detected cylinders, transformed using the estimated trafo.
        write_cylinders(out_file, "W C", transformed_world_cylinders)

    out_file.close()