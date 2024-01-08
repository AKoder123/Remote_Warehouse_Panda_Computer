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

  left_values = [0.6950713977981032, 0.36798056143626834, -0.2248628552671064, -2.4354596992291886, 0.024714471658070877, 2.8088217362967547, 1.2189255104147723]

  right_values = [0.2619991096153594, 0.023486502526967056, -0.7306691922891514, -2.38161687707855, 0.040072656255846904, 2.4436565056641895, 0.3069542164476351]


  values = ready_values

  for i in range(7):
    joint_goal[i] = values[i]

  # # The go command can be called with joint values, poses, or without any
  # # parameters if you have already set the pose or joint target for the group
  move_group.go(joint_goal, wait=True)

  # # Calling ``stop()`` ensures that there is no residual movement
  move_group.stop()