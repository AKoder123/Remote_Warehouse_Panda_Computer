#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Image, PointCloud2
import cv_bridge
import cv2
import franka_gripper
from niryo_moveit.srv import PositionService

def callback(msg):
  # bridge = cv_bridge.CvBridge()
  # cv2_image = bridge.imgmsg_to_cv2(image)
  # cv2.imwrite("cv2_image.png", cv2_image)

  rospy.loginfo(msg)

def position_client():
  rospy.wait_for_service('move_service')
  try:
      service = rospy.ServiceProxy('move_service', PositionService)
      pos = Vector3(0,0,0)
      resp1 = service(pos)
      print(resp1.feedback)
      return resp1.feedback
  except rospy.ServiceException as e:
      print("Service call failed: %s"%e)

if __name__ == "__main__":
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

  # rospy.Subscriber("/camera/color/image_raw", Image, callback)
  # rospy.Subscriber("/camera/depth_registered/points", PointCloud2, callback)
  # rospy.Subscriber
  # rospy.Publisher
  robot = moveit_commander.RobotCommander()

  # scene = moveit_commander.PlanningSceneInterface()
  # print("printing scene:")
  # print (scene.get_objects())

  group_name = "panda_arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)

  # We can get the name of the reference frame for this robot:
  # planning_frame = move_group.src/custom_msg/msg/FingerPosMsg.msgget_planning_frame()
  # print("============ Planning frame: %s" % planning_frame)

  # We can also print the name of the end-effector link for this group:
  # eef_link = move_group.get_end_effector_link()
  # print("============ End effector link: %s" % eef_link)

  # # We can get a list of all the groups in the robot:
  # group_names = robot.get_group_names()
  # print("============ Available Planning Groups:", robot.get_group_names())

  # Sometimes for debugging it is useful to print the entire state of the
  # robot:
  print("============ Printing robot state")
  print(robot.get_current_state())
  print("")

  print("============ Printing robot pose")
  wpose = move_group.get_current_pose().pose
  print(wpose)

  # wpose.position.x = 0.3
  # wpose.position.y = 2.72754313243e-05
  # wpose.position.z = 0.45
  # wpose.orientation.x = -0.82539796679
  # wpose.orientation.y = 0.341598533047
  # wpose.orientation.z = -0.415150454439
  # wpose.orientation.w = 0.172275183408


  # wpose.position.x = 0.490662813768
  # wpose.position.y = -0.182622636949
  # wpose.position.z = 0.671207872685
  # wpose.orientation.x = -0.923999016506
  # wpose.orientation.y = 0.382390205557
  # wpose.orientation.z = -0.00186140917219
  # wpose.orientation.w = 0.000288695182569

  # [0.18120097560705117, -0.69141019095036, -0.1826890494049641, -2.535297429157607, -0.11813207982707395, 1.9465357708136242, 0.8242967599561276, 4.6623332309536636e-05, 4.6623332309536636e-05]
  # [-0.01593474851888523, -0.6810690838161267, -0.021073979630020626, -2.3177276908472964, 0.031027641724075152, 1.5636422585209573, 0.6927000413023763, 0.04016074910759926, 0.04016074910759926]

  # [3.843972435732143e-05, -0.7848056303576417, -1.3633491700295202e-05, -2.356355799762344, 0.0008377492449556786, 1.574822178096435, 0.7845437594994964]

  joint_goal = move_group.get_current_joint_values()
  # print(joint_goal)
  # joint_goal[0] = 3.843972435732143e-05
  # joint_goal[1] = -0.7848056303576417
  # joint_goal[2] = -1.3633491700295202e-05
  # joint_goal[3] = -2.356355799762344
  # joint_goal[4] = 0.0008377492449556786
  # joint_goal[5] = 3
  # joint_goal[6] = 0.7845437594994964
  print(joint_goal)
  # move_group.go(joint_goal, wait=True)

  # x=0.4, z=0.3, joint 5 = 2.8
  # [0.00020698689423158674, -0.025882745280430674, 0.0004090112372144739, -2.4832404763415052, -0.00040863626964131425, 2.8038245557943977, 0.7850969508213886]
  # joint 5 = 3
  # [9.177317792184023e-05, -0.221693881682991, 0.0003451252640268467, -2.703369733174642, -0.0008918122599178247, 3.003634447177251, 0.7847068120721321]

  # x=0.35 (Reached joint limit -- Joint 4)
  # [0.0012331994194864214, -0.21075665437129507, -0.0005770062959279146, -2.818711800133567, 0.0003851178548536155, 2.9575422167162735, 0.7829431012062428]


  # wpose.position.x = 0.47
  # wpose.position.y = 0
  # wpose.position.z = 0.17
  # print("============ Printing robot state")
  # print(robot.get_current_state())
  # print("")

  # move_group.set_pose_target(wpose)

  # `go()` returns a boolean indicating whether the planning and execution was successful.
  # success = move_group.go(wait=True)
  # # Calling `stop()` ensures that there is no residual movement
  # move_group.stop()
  # # It is always good to clear your targets after planning with poses.
  # # Note: there is no equivalent function for clear_joint_value_targets().
  # move_group.clear_pose_targets()



  rospy.spin()


