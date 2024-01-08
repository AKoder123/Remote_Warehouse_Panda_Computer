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

import random
import rospy
import rosgraph
import time
from unity_robotics_demo_msgs.msg import FingerPosMsg


TOPIC_NAME = 'finger'
NODE_NAME = 'finger_publisher'


def post_color():
    
    pub = rospy.Publisher(TOPIC_NAME, FingerPosMsg, queue_size=10)
    rospy.init_node(NODE_NAME, anonymous=True)

    values = FingerPosMsg()
    values.pos_1 = 0.4
    values.pos_2 = 0.4

    wait_for_connections(pub, TOPIC_NAME)
    pub.publish(values)

    time.sleep(0.1)


def wait_for_connections(pub, topic):
    ros_master = rosgraph.Master('/rostopic')
    topic = rosgraph.names.script_resolve_name('rostopic', topic)
    num_subs = 0
    for sub in ros_master.getSystemState()[1]:
        if sub[0] == topic:
            num_subs+=1

    for i in range(10):
        if pub.get_num_connections() == num_subs:
            return
        time.sleep(0.1)
    raise RuntimeError("failed to get publisher")


if __name__ == '__main__':
    try:
        post_color()
    except rospy.ROSInterruptException:
        pass
    rospy.spin()