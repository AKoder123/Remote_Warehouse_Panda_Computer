#!/usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import Pose
from std_msgs.msg import Float32
from sensor_msgs.msg import CompressedImage

class CameraPosition():
    
    def __init__(self):
        self.source_frame_topic = "camera_link"
        self.target_frame_topic = "panda_link0"


        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

        self.pose_publisher = rospy.Publisher(
            'camera_position', 
            Pose, 
            queue_size=1
            )
        
        self.scale_publlisher = rospy.Publisher(
            'camera_scale', 
            Float32, 
            queue_size=1
            )
        
        self.subscriber = rospy.Subscriber(
            "/camera/color/image_raw/compressed",
            CompressedImage,
            self.callback,
            queue_size=1
            )
        
    def callback(self, img):
        trans = self.tf_buffer.lookup_transform(
            self.target_frame_topic,
            self.source_frame_topic, 
            rospy.Time()
            )
        position_msg = Pose()
        position_msg.position = trans.transform.translation
        position_msg.orientation = trans.transform.rotation
        self.pose_publisher.publish(position_msg)

        current_z = trans.transform.translation.z
        scale = Float32()
        scale = current_z/initial_camera_z
        self.scale_publlisher.publish(scale)


if __name__ == '__main__':
    rospy.init_node('camera_position')
    transform_point_cloud = CameraPosition()
    print("Camera Position")
    initial_camera_z = 0.524424352401
    rospy.spin()
        