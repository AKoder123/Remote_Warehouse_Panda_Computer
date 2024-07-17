#!/usr/bin/python

import sys
import rospy
import moveit_commander
from enum import Enum
from geometry_msgs.msg import Vector3, PoseArray, Pose, Quaternion
from std_msgs.msg import String

"""
  A:
  (0.47, 0.136)
  show when x>0.51 and y<0.15
  (0.434, -0.239)
  show when x<0.434 and y>-0.239

  B:
  (0.473, -0.148)
  show when x<0.473 and y<-0.148

  C:
  (0.469, 0.159)
  show when x<0.469 and y>0.159
  """

class Object():

  def __init__(self, position, x_bounds, y_bounds, available):
    self.position = position
    self.x_bounds = x_bounds
    self.y_bounds = y_bounds
    self.available = available

def check(obj):
  if not obj.available:
    return
  
  wpose = move_group.get_current_pose().pose
  robot_pos = wpose.position

  if obj.x_bounds[0] < robot_pos.x < obj.x_bounds[1] and obj.y_bounds[0] < robot_pos.y < obj.y_bounds[1]:
    return obj.position
  


def display_callback(msg):
  msg_arr = PoseArray()
  for obj in objects_array:
    pos = check(obj)
    if pos:
      curr_pose = Pose()
      curr_pose.position.x = pos.x
      curr_pose.position.y = pos.y
      curr_pose.position.z = pos.z
      msg_arr.poses.append(curr_pose)
  obj_display_pub.publish(msg_arr)

def status_callback(msg):
  for obj in objects_array:
    if round(msg.x, 2) == obj.position.x and round(msg.y, 2) == obj.position.y:
      obj.available = False



if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("spawn_obj_pub", anonymous=True)

  obj_check_sub = rospy.Subscriber("/check_objects", String, display_callback, queue_size=1)
  obj_display_pub = rospy.Publisher("/display_objects", PoseArray, queue_size=1)

  obj_status_sub = rospy.Subscriber("/object_status", Vector3, status_callback, queue_size=1)

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  # Hard coded object position and visibility bounds. 
  # 2 and -2 is used to mark large values. this indicates that within the joint limit, the object will always be visible

  obj_A = Object(position=Vector3(0.47, 0, 0.17), x_bounds=(0.28, 0.51), y_bounds=(-0.239, 0.1), available=True)
  obj_B = Object(position=Vector3(0.37, -0.33, 0.17), x_bounds=(-2, 0.4702), y_bounds=(-2, -0.1), available=True)
  obj_C = Object(position=Vector3(0.42, 0.42, 0.17), x_bounds=(-2, 0.4757), y_bounds=(0.11, 2), available=True)

  objects_array = [obj_A, obj_B, obj_C]
  

  rospy.spin()