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

from enum import Enum

class GripperState(Enum):
  Grip1 = 0
  Grip2 = 1
  Open = 3
  Closed = 4

def move_robot(sel_state):
  sel_state = sel_state.lower()
  ready_values = [0.00019025905158115864, -0.7850538262986299, 2.8837701730560838e-05, -2.356203691054924, -0.00016141187679397914, 1.5732667469142465, 0.7851245770537191]

  # left_values = [0.7265509473733734, 0.31427018733610185, -0.2680263785437534, -2.467356380931118, 0.024662607025776107, 2.819748551766078, 1.1758973142251432]
  left_values = [0.698739512853455, 0.4103175682387684, -0.23583577202495776, -2.4437533416374535, 0.06087147524037352, 2.8961014967092265, 1.149806387591693]

  right_values = [0.2619991096153594, 0.023486502526967056, -0.7306691922891514, -2.38161687707855, 0.040072656255846904, 2.4436565056641895, 0.3069542164476351]
  # right_values = [0.2561833516212932, 0.2688411496731273, -0.6150570143147518, -2.4070403182046456, 0.3395954543331797, 2.6532573484579722, 0.16921209685490773]

  rice_values = [0.3220515858442509, 0.4657052730175486, -0.058544621554383044, -1.9978825529590571, 0.028258240304059445, 2.628034859418869, 1.0210898673094926]
  
  if sel_state == "ready":
    values = ready_values
  elif sel_state == "left":
    values = left_values
  elif sel_state == "right":
    values = right_values
  elif sel_state == "rice":
    values = rice_values
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
  open = [0.039, 0.039]
  closed = [0,0]
  grip1 = [0.022, 0.022]
  grip2 = [0.01, 0.01]


  if sel_grip == GripperState.Open:
    values = open
  elif sel_grip == GripperState.Closed:
    values = closed
  elif sel_grip == GripperState.Grip1:
    values = grip1
  elif sel_grip == GripperState.Grip2:
    values = grip2
  else:
    values = open

  for i in range(len(values)):
    finger_joint_goal[i] = values[i]

  hand_move_group.go(finger_joint_goal, wait=True)

  hand_move_group.stop()

  move_group.clear_pose_targets()

def pick_and_place():

  move_gripper(GripperState.Open)

  move_robot("left")

  move_gripper(GripperState.Grip1)
  move_gripper(GripperState.Grip1)

  move_robot("ready")

  move_robot("right")

  move_gripper(GripperState.Open)

  move_robot("ready")

def rice_pick_and_place():

  move_gripper(GripperState.Open)

  move_robot("rice")

  move_gripper(GripperState.Grip2)

  move_robot("ready")

  move_gripper(GripperState.Grip2)

  move_robot("right")

  move_gripper(GripperState.Open)

  move_robot("ready")

def can_pick_and_place():

  # move_gripper(GripperState.Open)

  move_robot("left")
  move_gripper(GripperState.Open)
  move_gripper(GripperState.Grip1)

  move_robot("ready")

  move_robot("left")

  move_gripper(GripperState.Open)

  move_robot("ready")

  move_gripper(GripperState.Open)


if __name__ == "__main__":

  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("new_joint_mover", anonymous=True)

  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm_hand"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  print("============ Printing robot state")
  print(robot.get_current_state())
  print("")

  joint_goal = move_group.get_current_joint_values()

  hand_group_name = "hand"
  hand_move_group = moveit_commander.MoveGroupCommander(hand_group_name)

  finger_joint_goal = hand_move_group.get_current_joint_values()

  

  
  # move_gripper(GripperState.Open)
  
  move_robot("ready")

