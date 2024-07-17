#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Vector3
from niryo_moveit.msg import PickPlacePosition
from tf.transformations import quaternion_from_euler, euler_from_quaternion

def mover_helper(position):
  waypoints = []

  wpose = move_group.get_current_pose().pose
  
  waypoints.append(copy.deepcopy(wpose))

  wpose.position.x = position.x
  wpose.position.y = position.y
  wpose.position.z = position.z  #for cube on 2 blue ruko marker blocks

  # q = quaternion_from_euler(-3.1314518487370555, -0.009005753462883438, -1.5708)
  # print(q)
  # wpose.orientation.x = q[0]
  # wpose.orientation.y = q[1]
  # wpose.orientation.z = q[2]
  # wpose.orientation.w = q[3]

  waypoints.append(copy.deepcopy(wpose))

  (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

  move_group.execute(plan, wait = True)

  # waypoints = []

  # waypoints.append(copy.deepcopy(wpose))

  # waypoints.append(copy.deepcopy(ready_wpose))

  # (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

  # move_group.execute(plan, wait = True)



def callback(position):
  ready_wpose = move_group.get_current_pose().pose
  # position.z = 0.17
  mover_helper(position)
  rospy.sleep(0.5)
  # mover_helper(ready_wpose.position)
  



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

  test_pos = Vector3()
  # test_pos.x = 0.37
  # test_pos.y = -0.33
  # test_pos.z = 0.165

  test_pos.x = 0.49
  test_pos.y = -0.1
  test_pos.z = 0.165

  # test_pos.x = 0.55
  # test_pos.y = 0.25
  # test_pos.z = 0.165

  # test_pos.x = 0.42
  # test_pos.y = 0.42
  # test_pos.z = 0.165

  # test_pos.x = 0.666
  # test_pos.y = -0.2
  # test_pos.z = 0.23

  callback(test_pos)

  # q = quaternion_from_euler(-3.1314518487370555, -0.009005753462883438, -1.5708)
  # print(q)

  # a = euler_from_quaternion((-0.924143533781, 0.381985268683, -0.00609823588161, 0.0029656363353))
  # print (a)

  rospy.spin()