
## Robot Running
Make sure workspace is selected currently \#13
To run robot:

`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`

To run camera:

`roslaunch realsense2_camera rs_rgbd.launch`

To test camera quickly:
`realsense-viewer`

To run code

`rosrun robot_control yeet.py `

Or in the more dodgy (non-ros) way

```bash
cd /home/hrigroup2/mrtele_ws/src/robot_control
python yeet.py
```

To send joint values to robot computer from unity

`roslaunch ros_tcp_endpoint endpoint.launch`
`rosrun niryo_moveit trajectory_subscriber.py`