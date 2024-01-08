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


def callback(msg):
  # bridge = cv_bridge.CvBridge()
  # cv2_image = bridge.imgmsg_to_cv2(image)
  # cv2.imwrite("cv2_image.png", cv2_image)

  rospy.loginfo(msg)


if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

  # rospy.Subscriber("/camera/color/image_raw", Image, callback)
  # rospy.Subscriber("/camera/depth_registered/points", PointCloud2, callback)
  # rospy.Subscriber
  # rospy.Publisher
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

  print(joint_goal)

  # values = [-0.01593474851888523, -0.6810690838161267, -0.021073979630020626, -2.3177276908472964, 0.031027641724075152, 1.5636422585209573, 0.69270004130237630]

  ready_values = [0.00019025905158115864, -0.7850538262986299, 2.8837701730560838e-05, -2.356203691054924, -0.00016141187679397914, 1.5732667469142465, 0.7851245770537191]

  left_values = [1.1096979659565709, 0.3628375442948258, -0.5438025274583477, -2.5157677164579693, 0.2401969484236888, 2.8715361602298977, 1.1414001283728414]

  right_values = [0.2619991096153594, 0.023486502526967056, -0.7306691922891514, -2.38161687707855, 0.040072656255846904, 2.4436565056641895, 0.3069542164476351]

  hand_group_name = "hand"
  hand_move_group = moveit_commander.MoveGroupCommander(hand_group_name)

  finger_joint_goal = hand_move_group.get_current_joint_values()

  print(finger_joint_goal)


  open = [0.04, 0.04]
  closed = [0,0]
  grip = [0.038, 0.038]

  gripper = open

  for i in range(len(gripper)):
    finger_joint_goal[i] = gripper[i]

  hand_move_group.go(finger_joint_goal, wait=True)

  hand_move_group.stop()

  values = left_values

  for i in range(len(values)):
    joint_goal[i] = values[i]

  # # The go command can be called with joint values, poses, or without any
  # # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  # # Calling ``stop()`` ensures that there is no residual movement
  move_group.stop()

  gripper = grip

  for i in range(len(gripper)):
    finger_joint_goal[i] = gripper[i]

  hand_move_group.go(finger_joint_goal, wait=True)

  hand_move_group.stop()


  values = ready_values

  for i in range(len(values)):
    joint_goal[i] = values[i]

  # # The go command can be called with joint values, poses, or without any
  # # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  # # Calling ``stop()`` ensures that there is no residual movement
  move_group.stop()

  values = left_values

  for i in range(len(values)):
    joint_goal[i] = values[i]

  # # The go command can be called with joint values, poses, or without any
  # # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  move_group.stop()

  gripper = open

  for i in range(len(gripper)):
    finger_joint_goal[i] = gripper[i]

  hand_move_group.go(finger_joint_goal, wait=True)

  hand_move_group.stop()

  values = ready_values

  for i in range(len(values)):
    joint_goal[i] = values[i]

  # # The go command can be called with joint values, poses, or without any
  # # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  move_group.stop()