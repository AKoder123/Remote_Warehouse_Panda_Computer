#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from sensor_msgs.msg import Image, PointCloud2
from cv_bridge import CvBridge, CvBridgeError
import cv2


def callback(data):
  bridge = CvBridge()
  cv2_image = bridge.imgmsg_to_cv2(data, "bgr8")
  cv2.imshow("Image window", cv2_image)
  cv2.waitKey(3)

  # rospy.loginfo(msg)


if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

  rospy.Subscriber("/camera/color/image_raw", Image, callback)
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

  wpose = move_group.get_current_pose().pose

  
  wpose.position.x = 0.307555363916
  wpose.position.y = -3.04037977349e-05
  wpose.position.z = 0.590409526104
  wpose.orientation.x = -0.924094304854
  wpose.orientation.y = 0.382158665237
  wpose.orientation.z = -0.00205988698261
  wpose.orientation.w = 0.000476639753737


  # wpose.position.x = 0.490662813768
  # wpose.position.y = -0.182622636949
  # wpose.position.z = 0.671207872685
  # wpose.orientation.x = -0.923999016506
  # wpose.orientation.y = 0.382390205557
  # wpose.orientation.z = -0.00186140917219
  # wpose.orientation.w = 0.000288695182569

  # [0.18120097560705117, -0.69141019095036, -0.1826890494049641, -2.535297429157607, -0.11813207982707395, 1.9465357708136242, 0.8242967599561276, 4.6623332309536636e-05, 4.6623332309536636e-05]
  # [-0.01593474851888523, -0.6810690838161267, -0.021073979630020626, -2.3177276908472964, 0.031027641724075152, 1.5636422585209573, 0.6927000413023763, 0.04016074910759926, 0.04016074910759926]

  # joint_goal = move_group.get_current_joint_values()
  # print(joint_goal)
  # joint_goal[0] = -0.01593474851888523
  # joint_goal[1] = -0.6810690838161267
  # joint_goal[2] = -0.021073979630020626
  # joint_goal[3] = -2.3177276908472964
  # joint_goal[4] = 0.031027641724075152
  # joint_goal[5] = 1.5636422585209573
  # joint_goal[6] = 0.6927000413023763
  # joint_goal[0] = 0.04016074910759926
  # joint_goal[1] = 0.04016074910759926
  # move_group.go(joint_goal, wait=True)



  move_group.set_pose_target(wpose)

  # `go()` returns a boolean indicating whether the planning and execution was successful.
  success = move_group.go(wait=True)
  # Calling `stop()` ensures that there is no residual movement
  move_group.stop()
  # It is always good to clear your targets after planning with poses.
  # Note: there is no equivalent function for clear_joint_value_targets().
  move_group.clear_pose_targets()

  rospy.spin()


