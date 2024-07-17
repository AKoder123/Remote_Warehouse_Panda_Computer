### Prerequisites

Ensure physics solver is set to `Temporal Gauss Seidel` in [Physics Manager](https://docs.unity3d.com/Manual/class-PhysicsManager.html)

### External Camera VR Demo

1) `roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`

2) `roslaunch realsense2_camera rs_rgbd.launch`

3) `roslaunch ros_tcp_endpoint endpoint.launch`

3) Unity with robot Tuesday_attempt with Robot

4) `rosrun niryo_moveit joint1_control.py` or `rosrun niryo_movit mirrored_joint1_control.py`

5) `rosrun niryo_moveit transform_obj.py`

6) `rosrun niryo_moveit camera_position_publisher.py`





### Mixed reality demo

1) `roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`

2) `roslaunch ros_tcp_endpoint endpoint.launch`

3) Unity with robot and MR project

4) `rosrun niryo_moveit VR_no_camera_srv.py`




### ROS, Unity and Real Arm


Camera:

`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`

quickly do next option

`roslaunch realsense2_camera rs_rgbd.launch`

wait until rviz loads

`rosrun niryo_moveit camera_position_publisher.py`

`roslaunch ros_tcp_endpoint endpoint.launch`

'rosrun niryo_moveit move_subscriber.py'

wait for unity connection and then run move subscriber

`rosrun niryo_moveit move_subscriber.py`

`rosrun niryo_moveit joint1_control.py`


Point cloud publishing:



`roslaunch realsense2_camera rs_rgbd.launch`

`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`

`rosrun niryo_moveit down_sample_pcd.py`

`rosrun niryo_moveit transform_pcd.py`

`roslaunch ros_tcp_endpoint endpoint.launch`

`rosrun niryo_moveit joint1_control.py`

if unable to move robot, stop rviz and launch again




Previous Control methods

`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`

`roslaunch ros_tcp_endpoint endpoint.launch`

`rosrun niryo_moveit subscriber_mover.py`
or
`rosrun niryo_moveit new_subscriber_mover.py`

To run tcp connection using ethernet:
`roslaunch ros_tcp_endpoint endpoint.launch tcp_ip:=192.168.1.69 tcp_port:=10000`

Run transformed point cloud (from cmaera_link to panda_link0):
`rosrun niryo_moveit transform_point_cloud_publisher.py`

In unity: show the 3D visualization for the topic **base_frame_point_cloud**


If something goes wrong try:

`source devel/setup.bash`


To run camera:

`roslaunch realsense2_camera rs_rgbd.launch`

To test camera quickly:
`realsense-viewer`

publishing transformed point clouds:

`rosrun tf static_transform_publisher -0.284 -0.018 0.494 0.999, 0.032, -0.032, 0.001 panda_K created_base 100`

RVIZ errors:

Panda joint values more than 0.1 from expected, 
kill roslaunch panda_moveit_config and run it again


### ROS & Simulated Arm Only
--

**Terminal 1**

```
roscore &
rosparam set ROS_IP 192.168.50.149
rosparam set ROS_TCP_PORT 10000
rosparam set UNITY_IP 192.168.50.13
rosparam set UNITY_SERVER_PORT 5005
rosrun niryo_moveit server_endpoint.py
```

**Terminal 2**

`rosrun niryo_moveit mover.py`

**Terminal 3**

`roslaunch niryo_moveit demo.launch`

**Unity**

Press play in the Editor and press `Send Joint Angles` button in scene.


### Converting to Niryo One & Simulated Arm:
--

Convert the mover service to publish to the `“niryo_one/commander/robot_action` topic of a `RobotMoveCommand` message type.

**RobotMoveCommand.msg**

```
int32 cmd_type

float64[] joints
geometry_msgs/Point position
niryo_one_msgs/RPY rpy
niryo_one_msgs/ShiftPose shift
niryo_one_msgs/TrajectoryPlan Trajectory
geometry_msgs/Pose pose_quat
string  saved_position_name
int32 saved_trajectory_id
```

**TrajectoryPlan.msg**

```
moveit_msgs/RobotState trajectory_start
string group_name
moveit_msgs/RobotTrajectory trajectory
```

**ROS Side**

The current `mover.py` returns a plan with a `RobotTrajectory` and `RobotState` so it is likely that we will be able to convert our service to return the success of planning a trajectory while also publishing the trajectories to the corresponding topic.

**Unity Side**

Convert the current service call into a publisher and subscriber. Subscribe to the same topic as the real robot and move the simulated robot accordiingly.


### Creating Tutorials
--

- Be sure to update all URDFs to include gripper



### Resources Used
--

- [MoveIt](https://github.com/ros-planning/moveit)
- All of the launch and config files used in this package were copied from
[Niryo One ROS Stack](https://github.com/NiryoRobotics/niryo_one_ros) and edited to suit our reduced use case.


Questions:
---
- Why does trajectory planning fail when the target pose is about halfway up the robot? Are there constraints being enforced somewhere?


Notes:
---
Changing from Unity coords to ROS coords:

```
Unity: (x, y z)
ROS: (z, -x, y)
```


0 0.249 0

0, 0, 0.249




