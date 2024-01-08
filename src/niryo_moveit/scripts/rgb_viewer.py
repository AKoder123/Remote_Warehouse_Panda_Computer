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

  rospy.spin()


