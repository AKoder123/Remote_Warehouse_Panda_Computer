#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from sensor_msgs.msg import Image, PointCloud2
import cv_bridge
import cv2


if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  # We can get the name of the reference frame for this robot:
  planning_frame = move_group.get_planning_frame()
  # print("============ Planning frame: %s" % planning_frame)

  # We can also print the name of the end-effector link for this group:
  eef_link = move_group.get_end_effector_link()
  # print("============ End effector link: %s" % eef_link)

  # We can get a list of all the groups in the robot:
  group_names = robot.get_group_names()
  # print("============ Available Planning Groups:", robot.get_group_names())

  # Sometimes for debugging it is useful to print the entire state of the
  # robot:
  print("============ Printing robot state")
  # print(robot.get_current_state())
  print("")

  wpose = move_group.get_current_pose().pose

  joint_goal = move_group.get_current_joint_values()
  print(eef_link)

  # move_group.go(joint_goal, wait=True)

  # # Calling ``stop()`` ensures that there is no residual movement
  # move_group.stop()