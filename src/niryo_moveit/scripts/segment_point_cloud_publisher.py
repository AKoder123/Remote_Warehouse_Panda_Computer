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

class Segmentation():

    def __init__(self):
        # self.input_cloud_topic = rospy.get_param('~input_cloud_topic')
        self.compute_bounding_boxes = True

        self.point_cloud_listener = rospy.Subscriber(
            "base_frame_point_cloud",
            PointCloud2,
            self.callback,
            queue_size=1,
            tcp_nodelay=True
        )

        self.bounding_box_publisher = rospy.Publisher(
            'segmentation/bounding_boxes',
            BoundingBoxArray, 
            tcp_nodelay=True, 
            queue_size=1
        )

        

    def callback(self, pcd_ros):

        start_time = time.time()

        pcd_frame = pcd_ros.header.frame_id
        # print(pcd_frame)

        pcd = rospc_to_o3dpc(pcd_ros)
        print('src:', pcd)
        
        if self.compute_bounding_boxes:
            # Run DBscan on the rest of the point cloud to segment the objects on the table
            labels = np.array(pcd.cluster_dbscan(eps=0.04, min_points=500))
            max_label = labels.max()
            print(f"{max_label + 1} objects detected in point cloud")

            # Get bounding boxes for each segmented object
            # Initialise jsk BBArray message
            bbox_array = BoundingBoxArray()
            bbox_array.header.frame_id = pcd_frame
            bbox_array.header.stamp = rospy.Time.now()

            # Loop through each segmented object
            for i in range(max_label + 1):
                
                # Obtain bounding box for the object
                cluster = o3d.geometry.PointCloud()
                cluster.points = o3d.utility.Vector3dVector(np.asarray(pcd.points)[np.where(labels==i)])

                bbox = cluster.get_oriented_bounding_box()

                # Construct bounding box message
                bbox_msg = BoundingBox()
                bbox_msg.header.frame_id = pcd_frame
                bbox_msg.header.stamp = rospy.Time.now()
                
                # open3d rotation matrices can have -1 det, improper roation with reflections
                # scipy only works with +1 det, will convert the matrix
                # inverting each element will change det from -1 to +1
                if np.linalg.det(bbox.R) > 0:
                    quat = scipy.spatial.transform.Rotation.from_matrix(bbox.R).as_quat()
                else:
                    quat = scipy.spatial.transform.Rotation.from_matrix(-bbox.R).as_quat()
                
                bbox_msg.pose = Pose(Point(*bbox.center), Quaternion(*quat))

                bbox_msg.dimensions = Vector3(*bbox.extent)

                # Add to array
                bbox_array.boxes.append(bbox_msg)
            
            # print(f"point cloud has {max_label + 1} clusters")

            # Publish segment bounding boxes
            self.bounding_box_publisher.publish(bbox_array)
            print(bbox_array)
            print("Publishing bounding boxes...")


        print(f"Time taken: {time.time() - start_time}")

if __name__ == "__main__":

    rospy.init_node('tabletop_segmentation', anonymous=False)

    seg = Segmentation()

    rospy.spin()
