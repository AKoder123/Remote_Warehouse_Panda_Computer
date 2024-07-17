#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Vector3


def callback(position):
  waypoints = []

 



if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_subcriber", anonymous=True)
  control_subcriber = rospy.Subscriber("/obj_position_topic", Vector3, callback, queue_size=1)

  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  # Does not work in python
  # move_group.setPlanningTime(100) 

  hand_group_name = "hand"
  hand_move_group = moveit_commander.MoveGroupCommander(hand_group_name)

  jointVal = hand_move_group.get_current_joint_values()
  jointVal = [0.02, 0.02]

  hand_move_group.go(jointVal, wait=True)

  hand_move_group.stop()

  hand_move_group.clear_pose_targets()

  wpose = hand_move_group.get_current_pose().pose

  print(wpose)

  
  rospy.spin()