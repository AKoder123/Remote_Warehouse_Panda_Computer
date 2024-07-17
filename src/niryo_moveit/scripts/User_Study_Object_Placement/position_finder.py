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

  wpose = move_group.get_current_pose().pose

  print(wpose)
  
  rospy.spin()