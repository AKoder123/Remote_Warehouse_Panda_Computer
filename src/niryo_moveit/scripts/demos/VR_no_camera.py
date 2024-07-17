#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
from niryo_moveit.msg import PickPlacePosition
import franka_gripper.msg
import actionlib


def ready():
  waypoints = []

  wpose = move_group.get_current_pose().pose
  
  waypoints.append(copy.deepcopy(wpose))

  wpose.position.x = 0.508441655856
  wpose.position.y = 0.000285314360859
  wpose.position.z = 0.589967571678
  wpose.orientation.x = -0.923914304259
  wpose.orientation.y = 0.382579657528
  wpose.orientation.z = -0.00346098525941
  wpose.orientation.w = 0.00178482843911

  waypoints.append(copy.deepcopy(wpose))

  (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

  move_group.execute(plan, wait = True)
   


def gripper_open():
    client = actionlib.SimpleActionClient("/franka_gripper/move", franka_gripper.msg.MoveAction)
    client.wait_for_server()
    # widths
    # 0.1 - fully open
    # 0.6 - 4x4 rubiks cube
    goal = franka_gripper.msg.MoveGoal(width=0.09, speed=1.0)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def gripper_close():
    client = actionlib.SimpleActionClient("/franka_gripper/move", franka_gripper.msg.MoveAction)
    client.wait_for_server()
    # widths
    # 0.1 - fully open
    # 0.6 - 4x4 rubiks cube
    goal = franka_gripper.msg.MoveGoal(width=0.06, speed=1.0)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()


def mover_helper(position):
  waypoints = []

  wpose = move_group.get_current_pose().pose
  
  waypoints.append(copy.deepcopy(wpose))

  wpose.position.x = position.x
  wpose.position.y = position.y
  wpose.position.z = position.z  #for cube on 2 blue ruko marker blocks

  waypoints.append(copy.deepcopy(wpose))

  (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

  move_group.execute(plan, wait = True)


def gripper_helper():
    joint_values = hand_move_group.get_current_joint_values()
    print(joint_values)

    if joint_values[0] < 0.04:
       result = gripper_open()
       obj_state_pub.publish("PLACE")
    else:
       result = gripper_close()
       obj_state_pub.publish("PICK")

    print(result)
       

def callback(position):
  ready()
  # ready_wpose = move_group.get_current_pose().pose
  joint_values = hand_move_group.get_current_joint_values()

  if position.z == 0 and joint_values[0] < 0.04:
    obj_state_pub.publish("Cannot pick another object while current object is not dropped!")
  else:

    position.z = 0.17
    mover_helper(position)
    rospy.sleep(0.5)
    gripper_helper()
    rospy.sleep(0.5)
    # mover_helper(ready_wpose.position)
    ready()



if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_subcriber", anonymous=True)
  control_subcriber = rospy.Subscriber("/obj_position_topic", Vector3, callback, queue_size=1)
  obj_state_pub = rospy.Publisher("/obj_state_topic", String, queue_size=1)

  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  hand_group_name = "hand"
  hand_move_group = moveit_commander.MoveGroupCommander(hand_group_name)

  # ready()
  # rospy.sleep(0.5)
  print(move_group.get_current_pose().pose)



  # Does not work in python
  # move_group.setPlanningTime(100) 

  test_pos = Vector3()
  test_pos.x = 0.47
  test_pos.y = 0
  test_pos.z = 0.2
  callback(test_pos)

  rospy.spin()