# Autonomous-Driving - SLAM

  This project is a part of **SLAM** and **Path Planning** course given by the professor *Claus Brenner* from the *University of Leibniz*. The course is based on the data (LiDAR and Encoder) collected from a lego based robot with caterpillar tracks navigated through a controlled environment. 
  
## Overview

### Projects
<table style="width:100%">
  <tr>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_A"><img src="./Unit_A/robot_motion_model.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_A" name="p1_code">Unit_A: Motion and Sensor Model </a>
        </p>
    </th>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_B"><img src="./Unit_B/featureless_icp.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_B" name="p1_code">Unit_B: Feature based and Featureless localization </a>
        </p>
    </th>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_C"><img src="./Unit_C/img_03_KF.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_C" name="p1_code">Unit_C: Bayes Filter </a>
        </p>
    </th>
  </tr>
  <tr>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_D"><img src="./Unit_D/kalman_prediction_and_correction.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_D" name="p1_code">Unit_D: Extended Kalman Filter </a>
        </p>
    </th>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_E"><img src="./Unit_E/particle_filter.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_E" name="p1_code">Unit_D: Particle Filter </a>
        </p>
    </th>
    <th>
      <p align="center">
           <a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_F"><img src="./Unit_F/ekf_slam.gif" alt="Overview" width="100%" height="100%"></a>
           <br><a href="https://github.com/KarthickPN/Autonomous-Driving---SLAM/tree/master/Unit_F" name="p1_code">Unit_F: EKF SLAM </a>
        </p>
    </th>
  </tr>
</table>
--- 

## Table of Contents

#### [1. Model](Unit_A)
 - **Summary:** Developed a motion model of the robot, transformed the motor ticks of the robot into a real world trajectory and corrected the calibration error with the sensor model, developed using the LiDAR data by detecting the location of the landmarks in scanner's coordinate system.
 - **Keywords:** Motion model, motor control, LiDAR and encoder data.

#### [2. Localization](Unit_B)
 - **Summary** _Feature Based Localization:_ Assigned the detected landmarks to the respective landmarks in the map, developed the mathematics for similarity transformation and applied as a direct solution, and corrected the pose of the robot based on the transform. _Featureless localization:_ Assigned the scan points to the walls of the arena and applied Iterative Closest Point to find the optimal transformation.
 - **Keywords:** Similarity transformation, ICP
#### [3. Bayes Filter](Unit_C)
 - **Summary:** Developed a histogram filter and a 1-D Kalman filter which are recursive Bayes filters, to estimate the true position of the Robot, which is uncertain about its movement and has measurement noise.
 - **Keywords:** Histogram filter, 1-D Kalman filter.
#### [4. Kalman Filter](Unit_D)
 - **Summary:** Augmented the Kalman filter developed in Unit 3 to _n_ dimensions and implemented Exteded Kalman filter to localize our robot which has non linear states and control commands.
 - **Keywords:** Sensor fusion, Extended Kalman filter.
#### [5. Particle Filter](Unit_E)
 - **Summary:** Implemented a Monte Carlo Localization algorithm knows as Particle Filter, which could handle any kind of model (not just Gaussian) by discretizing the problem into individual particles to generate different system states. The states which are supported by the sensor data are assigned high weights. Rhe particles with low weights are ignored and new random sampling is done to keep the number of particles constant.
 - **Keywords:** Sensor fusion, Particle filter localization
#### [6. EKF SLAM](Unit_F)
 - **Summary:** What if the robot is not given the map of the environment? This is the common problem in the field of autonomous navigation. We have to estimate both the position and heading of the robot and the position of the landmarks. These 2 processes cannot be separated from each other and must be done simultaneously. In this part of the project, I implement an Extended Kalman Filter Simultaeous Localization and Mapping algorithm, as a solution to this problem.
 - **Keywords:** Sensor fusion, EKF SLAM
