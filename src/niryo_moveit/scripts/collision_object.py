#!/usr/bin/python

import sys
import rospy
import moveit_commander
from geometry_msgs.msg import PoseStamped


if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_group_python_interface_tutorial", anonymous=True)
  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  table_size = [0.82, 1.80, 0.85]

  box_pose = PoseStamped()
  box_pose.header.frame_id = "panda_link0"

  box_pose.pose.position.x = 0
  box_pose.pose.position.y = 0
  box_pose.pose.position.z = 0 
  box_name = "table"
  scene.add_box(box_name, box_pose, size=table_size)
  rospy.spin()