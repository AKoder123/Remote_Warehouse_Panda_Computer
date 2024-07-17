#!/usr/bin/env python3

import numpy as np
import open3d as o3d
import rospy
import scipy
import time

from geometry_msgs.msg import Point, Quaternion, Pose, Vector3
from jsk_recognition_msgs.msg import BoundingBox, BoundingBoxArray
from open3d_ros_helper import rospc_to_o3dpc, o3dpc_to_rospc
from sensor_msgs.msg import PointCloud2


class DownSamplePCD():
    
    def __init__(self):

        

        self.pcd_publisher = rospy.Publisher(
            'compressed_point_cloud', 
            PointCloud2, 
            queue_size=1
            )
        self.pcd_subscriber = rospy.Subscriber(
            "/camera/depth_registered/points",
            PointCloud2,
            self.pcd_callback,
            queue_size=1
            )


    def pcd_callback(self, pcd):
        pcd_frame = pcd.header.frame_id
        o3d_pcd = rospc_to_o3dpc(pcd)
        # downpcd = o3d_pcd.voxel_down_sample(voxel_size=0.015)
        downpcd = o3d_pcd
        
        # Remove point cloud lower than 0.52
        height_threshold = 0.52
        heights = np.asarray(downpcd.points)[:, 2]
        downpcd = downpcd.select_by_index([i for i in range(len(heights)) if heights[i] < height_threshold])
        
        # downpcd.transla


        pcd_msg = o3dpc_to_rospc(downpcd, frame_id=pcd_frame)
    

        self.pcd_publisher.publish(pcd_msg)

if __name__ == "__main__":
    rospy.init_node('down_sample_pcd')
    down_sample_point_cloud = DownSamplePCD()
    print("Compressing pcd...")
    rospy.spin()