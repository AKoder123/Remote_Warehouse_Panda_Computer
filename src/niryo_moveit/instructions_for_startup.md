# Non-finalised instructions

`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`

`roslaunch ros_tcp_endpoint endpoint.launch`

Connect Unity now 

## Launch File

Run object spawner and annotating image (VR/MR interface):

`roslaunch niryo_moveit multierror.launch visualization:=VR error:=2b`

Run object spawner and annotating image (Camera stream interface):

`roslaunch niryo_moveit multierror.launch visualization:=camera error:=2b`



## Commands to subsitute if launch file fails

if proximity sensor issue in quest persists, make sure you are wearing quest when hitting play in unity

Launch camera:

`roslaunch realsense2_camera rs_rgbd.launch`

Control Joint 1 and 6:

`rosrun niryo_moveit mirrored_joint1_control.py`

Pick and place service:

`rosrun niryo_moveit VR_no_camera_srv.py`


