#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


'''
Ready position and Orientation for Robot near enterance of robotics lab

position: 
  x: 0.307555363916
  y: -3.04037977349e-05
  z: 0.590409526104
orientation: 
  x: -0.924094304854
  y: 0.382158665237
  z: -0.00205988698261
  w: 0.000476639753737

after moving:

position: 
  x: 0.490662813768
  y: -0.182622636949
  z: 0.671207872685
orientation: 
  x: -0.923999016506
  y: 0.382390205557
  z: -0.00186140917219
  w: 0.000288695182569



'''


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

# rospy.Subscriber
# rospy.Publisher
robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

# We can get the name of the reference frame for this robot:
planning_frame = move_group.get_planning_frame()
print("============ Planning frame: %s" % planning_frame)

# We can also print the name of the end-effector link for this group:
eef_link = move_group.get_end_effector_link()
print("============ End effector link: %s" % eef_link)

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print("============ Available Planning Groups:", robot.get_group_names())

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print("============ Printing robot state")
print(robot.get_current_state())
print("")

wpose = move_group.get_current_pose().pose
print(wpose)

# wpose = move_group.get_current_pose().pose

# wpose.position.x += 0.1

# move_group.set_pose_target(wpose)

# # `go()` returns a boolean indicating whether the planning and execution was successful.
# success = move_group.go(wait=True)
# # Calling `stop()` ensures that there is no residual movement
# move_group.stop()
# # It is always good to clear your targets after planning with poses.
# # Note: there is no equivalent function for clear_joint_value_targets().
# move_group.clear_pose_targets()
