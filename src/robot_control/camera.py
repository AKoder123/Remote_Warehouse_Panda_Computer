#!/usr/bin/python

import sys
import copy
import rospy
from sensor_msgs.msg import Image, PointCloud2
import cv_bridge
import cv2

def callback(msg):
  rospy.loginfo("node")
  rospy.loginfo(msg)

if __name__ == "__main__":
  rospy.init_node("getting_point_cloud", anonymous=True)
  rospy.loginfo("node has started")
  rospy.Subscriber("/camera/depth_registered/points", PointCloud2, callback)
  rospy.spin()