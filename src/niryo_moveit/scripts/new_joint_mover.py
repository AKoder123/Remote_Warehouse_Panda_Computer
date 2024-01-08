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

def move_robot(sel_state):
  ready_values = [0.00019025905158115864, -0.7850538262986299, 2.8837701730560838e-05, -2.356203691054924, -0.00016141187679397914, 1.5732667469142465, 0.7851245770537191]

  left_values = [0.7265509473733734, 0.31427018733610185, -0.2680263785437534, -2.467356380931118, 0.024662607025776107, 2.819748551766078, 1.1758973142251432]

  right_values = [0.2619991096153594, 0.023486502526967056, -0.7306691922891514, -2.38161687707855, 0.040072656255846904, 2.4436565056641895, 0.3069542164476351]

  
  if sel_state == "ready":
    values = ready_values
  elif sel_state == "left":
    values = left_values
  elif sel_state == "right":
    values = right_values
  else:
    values = ready_values

  for i in range(len(values)):
    joint_goal[i] = values[i]

  # # The go command can be called with joint values, poses, or without any
  # # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  # # Calling ``stop()`` ensures that there is no residual movement
  move_group.stop()


def move_gripper(sel_grip):
  open = [0.04, 0.04]
  closed = [0,0]
  grip = [0.039, 0.039]

  if sel_grip == "open":
    values = open
  elif sel_grip == "closed":
    values = closed
  elif sel_grip == "grip":
    values = grip
  else:
    values = open

  for i in range(len(values)):
    finger_joint_goal[i] = values[i]

  hand_move_group.go(finger_joint_goal, wait=True)

  hand_move_group.stop()
  




if __name__=="__main__":

  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  print("============ Printing robot state")
  print(robot.get_current_state())
  print("")

  joint_goal = move_group.get_current_joint_values()

  hand_group_name = "hand"
  hand_move_group = moveit_commander.MoveGroupCommander(hand_group_name)

  finger_joint_goal = hand_move_group.get_current_joint_values()

  # move_gripper("open")

  move_robot("right")

  # move_gripper("grip")

  move_robot("ready")

  # move_gripper("open")

