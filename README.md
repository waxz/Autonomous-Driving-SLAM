# Autonomous-Driving - SLAM

  This project is a part of **SLAM** and **Path Planning** course given by the professor *Claus Brenner* from the *University of Leibniz*. The course is based on the data (LiDAR and Encoder) collected from a lego based robot with caterpillar tracks navigated through a controlled environment. 
  
## Overview

### Projects
<table style="width:75%">
  <tr>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_A"><img src="./Unit_A/motion_model.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_A" name="p1_code">Unit_A: Motor and Motion Model </a>
        </p>
    </th>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_B"><img src="./Unit_B/icp.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_B" name="p1_code">Unit_B: Feature based and Featureless localization </a>
        </p>
    </th>
  </tr>
</table>
--- 

## Table of Contents

#### [1. Motion model](Unit_A)
 - **Summary:** Developed a motion model, transformed the motor ticks of the robot into a real world trajectory and corrected the calibration error by using LiDAR data to detect the location of the landmarks in scanner's coordinate system.
 - **Keywords:** Motion model, motor model, LiDAR and encoder data.

#### [2. Localization](Unit_B)
 - **Feature Based Localization:** Assigned the detected landmarks to the respective landmarks in the map, developed the mathematics for similarity transformation and applied as a direct solution, and corrected the pose of the robot based on the transform.
 - **Featureless localization:** Assigned the scan points to the walls of the arena and applied Iterative Closest Point to find the optimal transformation.

