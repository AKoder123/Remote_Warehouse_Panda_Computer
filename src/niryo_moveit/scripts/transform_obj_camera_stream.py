#!/usr/bin/env python

import rospy
import tf2_ros

from sensor_msgs.msg import PointCloud2, CameraInfo, CompressedImage
from std_msgs.msg import String, Bool

from geometry_msgs.msg import Pose, PoseArray, PoseStamped, Vector3, Point

from cv_bridge import CvBridge
import cv2
import tf2_geometry_msgs.tf2_geometry_msgs
from image_geometry import PinholeCameraModel
from niryo_moveit.srv import PositionService, PositionServiceRequest

from copy import copy, deepcopy

RADIUS = 30

class Object():

  def __init__(self, color, position, available, index):
    # color in BGR;
    self.color = color
    self.position = position
    self.available = available
    self.index = index
    self.pixel_coor = None

class TransformObjectPos():
    
    def __init__(self, obj_arr):
        self.check = True
        self.obj_arr =  obj_arr
        self.input_image_topic = "/camera/color/image_raw/compressed"
        # transform from base_link to camera
        self.source_frame_topic = "panda_link0"
        self.target_frame_topic = "camera_color_optical_frame"
        self.cam_info_topic = "/camera/color/camera_info"
        
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

        self.camera_model = PinholeCameraModel()
        self.cam_info_sub = rospy.Subscriber(
            self.cam_info_topic,
            CameraInfo,
            self.cam_info_callback,
            queue_size=1
            )

        self.obj_pos_pub = rospy.Publisher(
            '/display_objects', 
            PoseArray, 
            queue_size=1
            )
        
        self.annotated_img_pub = rospy.Publisher(
            '/annotated_img', 
            CompressedImage
            )
        
        
        self.image_sub = rospy.Subscriber(
            self.input_image_topic,
            CompressedImage,
            self.img_callback
            )
        
        self.pixel_check_sub = rospy.Subscriber(
            "/check_pixel",
            Point,
            self.pixel_check_callback,
            queue_size=1
        )

        self.feedback_pub = rospy.Publisher(
            "/feedback_msg_topic",
            String,
            queue_size=1
        )

        self.ready_pub = rospy.Publisher(
            "/ready_topic", 
            String,
            queue_size=1)
        
        self.obj_check_sub = rospy.Subscriber(
            "/check_objects", 
            String, 
            self.display_callback, 
            queue_size=1)
        
        self.obj_status_sub = rospy.Subscriber(
            "/object_status", 
            Vector3, 
            self.status_callback, 
            queue_size=1)
        
        self.exploration_sub = rospy.Subscriber(
            "/exploration_topic", 
            Bool, 
            self.explore_callback, 
            queue_size=1)
        
        self.exploration = True

    def explore_callback(self, msg):
        self.exploration = msg.data

    def display_callback(self, msg):
        self.check = True

    def cam_info_callback(self, cam_info):
        self.camera_model.fromCameraInfo(cam_info)
        self.cam_info_sub.unregister()

    def trial(self):
        print("OK")
        new_obj_poses = PoseArray()
        for obj in self.obj_arr:
            if not obj.available:
                continue

            curr_pose = Pose()
            curr_pose.position.x = obj.position.x
            curr_pose.position.y = obj.position.y
            curr_pose.position.z = 0.05
            curr_pose.position.z = obj.index
            new_obj_poses.poses.append(curr_pose)
        print(new_obj_poses)
        self.obj_pos_pub.publish(new_obj_poses)
           
    def img_callback(self, msg_img):
        if not self.exploration:
            self.annotated_img_pub.publish(msg_img)
            return
        elif not self.check:
            return
        
        trans = self.tf_buffer.lookup_transform(
            self.target_frame_topic,
            self.source_frame_topic, 
            rospy.Time()
            )
        
        new_obj_poses = PoseArray()
        bridge = CvBridge()
        image_cv = bridge.compressed_imgmsg_to_cv2(msg_img)

        # print(image_cv.shape)

        for obj in self.obj_arr:

            if not obj.available:
                continue
            pose_staemped = PoseStamped()

            curr_pose = Pose()
            curr_pose.position.x = obj.position.x
            curr_pose.position.y = obj.position.y
            curr_pose.position.z = 0.05

            pose_staemped.pose = curr_pose
            obj_pose_camera = tf2_geometry_msgs.do_transform_pose(pose_staemped, trans)
            

            x = obj_pose_camera.pose.position.x
            y = obj_pose_camera.pose.position.y
            z = obj_pose_camera.pose.position.z

            pixel = self.camera_model.project3dToPixel((x, y, z))
            overlay = image_cv.copy()


            if  0 < pixel[0] < 640 and 0 < pixel[1] < 480:
                cv2.drawMarker(image_cv, (int(pixel[0]), int(pixel[1])), obj.color, cv2.MARKER_CROSS, 20, 2, 8)

                cv2.circle(overlay, (int(pixel[0]), int(pixel[1])), 30, obj.color, -1)

                print(pixel)
                curr_pose.position.z = obj.index
                new_obj_poses.poses.append(curr_pose)
                obj.pixel_coor = (pixel[0], pixel[1])
            else:
                obj.pixel_coor = None
            alpha = 0.3
            image_cv = cv2.addWeighted(overlay, alpha, image_cv, 1 - alpha, 0)


        
        ros_img = bridge.cv2_to_compressed_imgmsg(image_cv)
        self.annotated_img_pub.publish(ros_img)
        self.obj_pos_pub.publish(new_obj_poses)
        self.check = False
    
    def status_callback(self, msg):
        for obj in self.obj_arr:
            if round(msg.x, 2) == obj.position.x and round(msg.y, 2) == obj.position.y:
                obj.available = False

    def pixel_check_callback(self, msg):
        current_obj = None
        # print("OK")
        global RADIUS
        for obj in objects_array:
            if obj.pixel_coor:
                if((msg.x - obj.pixel_coor[0]) * (msg.x - obj.pixel_coor[0])) + ((msg.y - obj.pixel_coor[1]) * (msg.y - obj.pixel_coor[1])) <= RADIUS * RADIUS:
                    print(obj.index)
                    current_obj = obj
                    break
        if not current_obj:
            return
        # Service object
        rospy.wait_for_service("position_service")
        try:
            position_service = rospy.ServiceProxy("position_service", PositionService)
            request_position = current_obj.position
            request_position.z = 0
            respond = position_service(request_position)
            self.respond_service(respond)
        except:
            print("unable to request service")

    def respond_service(self, res):
        if res.feedback.data.upper() == "PICK":
            self.ready_pub.publish("PICK")
        else:
            self.feedback_pub.publish(res.feedback.data)
        


        

if __name__ == '__main__':
    rospy.init_node('transform_obj')

    # Hard coded object position. 

    obj_A = Object((0,255,255),position=Vector3(0.47, 0, 0.165), available=True, index=0)
    obj_B = Object((0, 144, 0), position=Vector3(0.37, -0.33, 0.165), available=True, index=1)
    obj_C = Object((255, 128, 0), position=Vector3(0.42, 0.42, 0.165), available=True, index=2)
    objects_array = [obj_A, obj_B, obj_C]

    transform_image = TransformObjectPos(objects_array)
    # i = 0
    # while True:
    #     transform_image.trial()
    #     rospy.sleep(2)

    print("Publishing object poses in camera frame...")
    rospy.spin()