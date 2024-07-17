#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Vector3
from niryo_moveit.msg import PickPlacePosition

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

  # waypoints = []

  # waypoints.append(copy.deepcopy(wpose))

  # waypoints.append(copy.deepcopy(ready_wpose))

  # (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

  # move_group.execute(plan, wait = True)



def callback(position):
  ready_wpose = move_group.get_current_pose().pose
  position.z = 0.30
  mover_helper(position)
  rospy.sleep(0.5)
  position.z = 0.17
  mover_helper(position)
  rospy.sleep(0.5)
  
  
  



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
  test_pos.x = 0.47
  test_pos.y = 0
  test_pos.z = 0.17
  callback(test_pos)

  rospy.spin()