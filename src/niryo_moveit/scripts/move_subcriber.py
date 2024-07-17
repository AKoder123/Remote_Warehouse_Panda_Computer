#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Vector3
from niryo_moveit.msg import PickPlacePosition
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String

def callback(position):
  msg = PickPlacePosition()
  msg.position = Vector3()
  msg.position.x = 0
  msg.position.y = 0
  msg.position.z = 0
  msg.state = String()
  msg.state.data = "pick"
  pub.publish(msg)
  # wpose.position.x = position.x
  # wpose.position.y = position.y
  # wpose.position.z = 0.17  #for cube on 2 blue ruko marker blocks

  # move_group.set_pose_target(wpose)
  # print(wpose)

  # # `go()` returns a boolean indicating whether the planning and execution was successful.
  # success = move_group.go(wait=True)
  # # Calling `stop()` ensures that there is no residual movement
  # move_group.stop()
  # # It is always good to clear your targets after planning with poses.
  # # Note: there is no equivalent function for clear_joint_value_targets().
  # move_group.clear_pose_targets()

  # move_gripper("closed")


def reset():
  joint_goal = move_group.get_current_joint_values()
  reset_value = [-2.008500200120623e-05, -0.19160002241845717, 0.0001590548822974884, -1.8770316369240743, -0.00010980078909132216, 1.6890316716035205, 0.7851252986672852]
  for i in range(len(reset_value)):
    joint_goal[i] = reset_value[i]

  # # The go command can be called with joint values, poses, or without any
  # # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  # # Calling ``stop()`` ensures that there is no residual movement
  move_group.stop()



def move_gripper(sel_grip):
  open = [0.04, 0.04]
  closed = [0,0]
  grip1 = [0.025, 0.025]
  grip2 = [0.01, 0.01]


  if sel_grip == "open":
    values = open
  elif sel_grip == "closed":
    values = closed
  elif sel_grip == "grip1":
    values = grip1
  elif sel_grip == "grip2":
    values = grip2
  else:
    values = open

  for i in range(len(values)):
    finger_joint_goal[i] = values[i]

  hand_move_group.go(finger_joint_goal, wait=True)

  hand_move_group.stop()

  hand_move_group.clear_pose_targets()

if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_subcriber", anonymous=True)
  control_subcriber = rospy.Subscriber("/camera/color/image_rect_color/compressed", CompressedImage, callback, queue_size=1)
  pub = rospy.Publisher("/trying_msg", PickPlacePosition, queue_size=1)
  

  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  # Does not work in python
  # move_group.setPlanningTime(100) 

  hand_group_name = "hand"
  hand_move_group = moveit_commander.MoveGroupCommander(hand_group_name)

  finger_joint_goal = hand_move_group.get_current_joint_values()

  wpose = move_group.get_current_pose().pose
  print(wpose)

  # move_gripper("open")
  reset()

  wpose = move_group.get_current_pose().pose

  print(wpose)



  rospy.spin()