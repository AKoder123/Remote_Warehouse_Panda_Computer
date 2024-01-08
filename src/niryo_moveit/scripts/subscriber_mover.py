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

from niryo_moveit.msg import NiryoMoveitJoints

def callback(data):
  # bridge = cv_bridge.CvBridge()
  # cv2_image = bridge.imgmsg_to_cv2(image)
  # cv2.imwrite("cv2_image.png", cv2_image)

  values = data.joints

  for i in range(7):
    joint_goal[i] = values[i]

  # The go command can be called with joint values, poses, or without any
  # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  # Calling ``stop()`` ensures that there is no residual movement
  move_group.stop()

def listener():
  rospy.Subscriber("/niryo_joints", NiryoMoveitJoints, callback)

  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()



if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("mover_subscriber", anonymous=True)

  rospy.Subscriber("/niryo_joints", NiryoMoveitJoints, callback)
  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  # We can get the name of the reference frame for this robot:
  # planning_frame = move_group.src/custom_msg/msg/FingerPosMsg.msgget_planning_frame()
  # print("============ Planning frame: %s" % planning_frame)

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


  # We can get the joint values from the group and adjust some of the values:
  joint_goal = move_group.get_current_joint_values()

  listener()

