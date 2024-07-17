#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
from std_msgs.msg import String, Bool


exploration = True

def callback(data):
  global exploration
  if not exploration:
    feedback_publisher.publish("Exploration unvailable!")
    return
  # Set joint limit
  joint1_lower = -1.0
  joint1_upper = 1.0
  joint6_lower = 1.45
  joint6_upper = 2.75

  # current_state is a tuple, so get each elemnt and put it into a list (to be modified)
  current_state = robot.get_current_state().joint_state.position
  joint_goal = []
  for i in range(7):
    joint_goal.append(current_state[i])

  # Move joint by offset
  joint1_offset = 0
  joint6_offset = 0
  if data.data == "R":
    joint1_offset = -0.05
  elif data.data == "L":
    joint1_offset = 0.05
  elif data.data == "U":
    joint6_offset = 0.02
  elif data.data == "D":
    joint6_offset = -0.02
  
  joint_goal[0] += joint1_offset
  joint_goal[5] += joint6_offset
  # joint_goal[5] = 1.6
  
  # check for joint limit
  if joint1_lower > joint_goal[0]:
    feedback_publisher.publish("Right limit reached!")
  elif joint_goal[0] > joint1_upper:
    feedback_publisher.publish("Left limit reached!")
  elif joint6_lower > joint_goal[5]:
    feedback_publisher.publish("Down limit reached!")
  elif joint_goal[5] > joint6_upper:
    feedback_publisher.publish("Up limit reached!")
  else:
    # move the robot and publish the message
    move_group.go(joint_goal, wait=True)
    move_group.stop()
    feedback_publisher.publish("Moving the robot...")
    check_obj_pub.publish("check")

def explore_callback(msg):
  global exploration
  exploration = msg.data

  if exploration:
    explore_position() # put in exploration position
    feedback_publisher.publish("Ready!")
  

def explore_position():
  explore_val = [1.2608034320238504e-05, -0.7849912622149987, -0.00010200676340890865, -2.3561573313997664, 0.00014997490218633571, 1.5726829244560665, 0.7847366398258588]
  joint_goal = move_group.get_current_joint_values()
  for i in range(len(explore_val)):
      joint_goal[i] = explore_val[i]

  move_group.go(joint_goal, wait=True)

  # Calling ``stop()`` ensures that there is no residual movement
  move_group.stop()

if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("joint1_control", anonymous=True)
  control_subcriber = rospy.Subscriber("/joint1_topic", String, callback, queue_size=1)
  feedback_publisher = rospy.Publisher("/joint1_limit_topic", String, queue_size=1)

  check_obj_pub = rospy.Publisher("/check_objects", String, queue_size=1)

  exploration_sub = rospy.Subscriber("/exploration_topic", Bool, explore_callback, queue_size=1)


  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  explore_position()
  rospy.sleep(1)

  check_obj_pub.publish("check")

  rospy.spin()

