#!/usr/bin/python

import sys
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Vector3
from std_msgs.msg import String, Bool
import franka_gripper.msg
import actionlib
from niryo_moveit.srv import PositionService, PositionServiceRequest, PositionServiceResponse
from enum import Enum


class GripperState(Enum):
   Open = 0
   Closed = 1

class ObjectTypes(Enum):
   Objects = 0
   DropBox = 1

class GripperWidths(Enum):
   FullyOpen = 0.09
   Rubiks4x4 = 0.06
   # Rubiks3x3 = 0.05 (using old gripper padding)
   Rubiks3x3 = 0.05

PROCESS_SEM = 0

def ready():
   """
   Go to ready position using cartesian path
   """
   

   waypoints = []

   wpose = move_group.get_current_pose().pose

   waypoints.append(copy.deepcopy(wpose))

   # hard coded ready position 
#   wpose.position.x = 0.508441655856
#   wpose.position.y = 0.000285314360859
#   wpose.position.z = 0.589967571678
#   wpose.orientation.x = -0.923914304259
#   wpose.orientation.y = 0.382579657528
#   wpose.orientation.z = -0.00346098525941
#   wpose.orientation.w = 0.00178482843911
  
  # Ready
   wpose.position.x = 0.307196150415
   wpose.position.y = -2.30921906614e-05
   wpose.position.z = 0.590343754286
   wpose.orientation.x = -0.923993725024
   wpose.orientation.y = 0.382406853779
   wpose.orientation.z = -0.000661632966833
   wpose.orientation.w = 0.000395652329983

   waypoints.append(copy.deepcopy(wpose))

   (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

   move_group.execute(plan, wait = True)
   rospy.sleep(0.5)
   global PROCESS_SEM
   PROCESS_SEM = 1

   
def ready_joint():
   """
   Ready position using joint values.
   This helps ensure that the robot joint is not exceeding joint limit.
   Sometimes when using cartesian path, the position is reached but the joint value is colose to joint limit
   """
   ready = [1.2608034320238504e-05, -0.7849912622149987, -0.00010200676340890865, -2.3561573313997664, 0.00014997490218633571, 1.5726829244560665, 0.7847366398258588]
   joint_goal = move_group.get_current_joint_values()
   for i in range(len(ready)):
      joint_goal[i] = ready[i]

   move_group.go(joint_goal, wait=True)

   # Calling ``stop()`` ensures that there is no residual movement
   move_group.stop()


def gripper_open():
   """
   Function to open the gripper using action library

   :return: true if gripper width is reached(sucess), false other wise
   :rtype: Boolean
   """
   client = actionlib.SimpleActionClient("/franka_gripper/move", franka_gripper.msg.MoveAction)
   client.wait_for_server()
   goal = franka_gripper.msg.MoveGoal(width=GripperWidths.FullyOpen.value, speed=1.0)
   client.send_goal(goal)
   client.wait_for_result()
   return client.get_result()

def gripper_close():
   """
   Function to close the gripper using action library

   :return: true if gripper width is reached(sucess), false other wise
   :rtype: Boolean
   """
   client = actionlib.SimpleActionClient("/franka_gripper/move", franka_gripper.msg.MoveAction)
   client.wait_for_server()
   goal = franka_gripper.msg.MoveGoal(width=GripperWidths.Rubiks3x3.value, speed=1.0)
   client.send_goal(goal)
   client.wait_for_result()
   return client.get_result()


def mover_helper(position):
   """
   Move the robot end-effector to the taget position usign cartesian path

   :param position: taget position
   :type position: Vector3
   """
   # Append current position
   waypoints = []
   wpose = move_group.get_current_pose().pose
   waypoints.append(copy.deepcopy(wpose))

   # Append target position, keeping the orientation of eef the same
   wpose.position.x = position.x
   wpose.position.y = position.y
   wpose.position.z = position.z  
   waypoints.append(copy.deepcopy(wpose))

   # Plan and execute
   (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)
   move_group.execute(plan, wait = True)


def gripper_helper(state, position):
   """
   Helper function for the gripper movement

   :param state: target state of the gripper (open/close)
   :type state: GripperState
   :param position: position of the object to be picked
   :type position: Vector3
   :return: string feedback of the state
   :rtype: string
   """
   if state == GripperState.Open:
      result = gripper_open()
      print(result)
      return "PLACE"
   else:
      result = gripper_close()
      # When an object is picked, we need to set its availibity to false
      # To make sure that it can't be picked twice (not shown in VR as virtual objects)
      obj_status_pub.publish(position)
      print(result)
      return "PICK"

       

def callback(req):
   # Feedback string
   res = String()

   global PROCESS_SEM

   if PROCESS_SEM == 1:
      PROCESS_SEM = 0
   else:
      res.data = "Unable to process request while robot is in motion"
      return PositionServiceResponse(res)
   # Joint value treshold for gripper. If lower than this, gripper is closed
   GRIPER_JOINT_TRESHOLD = 0.038

   PRE_PICK_Z = 0.2 # right above the cube
   PICK_HEIGHT = 0.165 # for cube on 2 blue ruko marker blocks (4x4), and 3 markers block for 3x3
   DROP_HEIGHT = 0.2

   position = req.position
   joint_values = hand_move_group.get_current_joint_values()

   # Get the current state of the gripper
   if joint_values[0] < GRIPER_JOINT_TRESHOLD:
      curr_grip = GripperState.Closed
   else:
      curr_grip = GripperState.Open

   # 0 means object and 1 means drop box
   if position.z == 0:
      object_type = ObjectTypes.Objects
   elif position.z == 1:
      object_type = ObjectTypes.DropBox

   if object_type == ObjectTypes.Objects:
      if curr_grip == GripperState.Closed:
         # If another box is selected whle the robot is still grasping an object, do not proceed.
         res.data = "Cannot pick another object!"
         PROCESS_SEM = 1
         return PositionServiceResponse(res)
      else:
         # Disable exploration while picking an object
         exploration_pub.publish(False)
         # Ready using joint values to make sure robot joint is in place
         ready_joint()

         # This is done to make sure the robot eef does not hit the object while moving into position
         position.z = PRE_PICK_Z 
         mover_helper(position)
         rospy.sleep(0.2)
         # Lower the eef to pick object up
         position.z = PICK_HEIGHT
         mover_helper(position)
         rospy.sleep(0.5)
         # Close the gripper to pick
         res.data = gripper_helper(GripperState.Closed, position)
         rospy.sleep(0.5)

         return PositionServiceResponse(res)
   elif object_type == ObjectTypes.DropBox:
      if curr_grip == GripperState.Open:
         # Drop zone is selected but no object is gripped
         res.data = "Select an object to drop"
         PROCESS_SEM = 1
         return PositionServiceResponse(res)
      else:
         # Drop object
         ready_joint()
         position.z = DROP_HEIGHT
         mover_helper(position)
         rospy.sleep(0.5)
         # Open the gripper to drop
         res.data = gripper_helper(GripperState.Open, position)
         rospy.sleep(0.5)
         return PositionServiceResponse(res)
  
def ready_callback(msg):
   ready()
   
   if msg.data == "PLACE":
      # Check for object to spawn
      check_obj_pub.publish("check")
      # Enable exploration
      exploration_pub.publish(True)


if __name__ == "__main__":
   moveit_commander.roscpp_initialize(sys.argv)
   rospy.init_node("position_service_server", anonymous=True)

   # Service for to pick and rop object
   srv = rospy.Service('position_service', PositionService, callback)
   # Subscriber for when object is sucessfully attached and detached from eef in unity
   ready_subscriber = rospy.Subscriber("/ready_topic", String, ready_callback, queue_size=1)
   # Publisher to update object status
   obj_status_pub = rospy.Publisher("/object_status", Vector3, queue_size=1)
   check_obj_pub = rospy.Publisher("/check_objects", String, queue_size=1)

   # Publisher to enable and disbale exploration
   exploration_pub = rospy.Publisher("/exploration_topic", Bool, queue_size=1)

   robot = moveit_commander.RobotCommander()

   scene = moveit_commander.PlanningSceneInterface()

   group_name = "panda_arm"
   move_group = moveit_commander.MoveGroupCommander(group_name)

   hand_group_name = "hand"
   hand_move_group = moveit_commander.MoveGroupCommander(hand_group_name)

   ready()
   check_obj_pub.publish("check")
#  rospy.sleep(0.5)
#  print(move_group.get_current_pose().pose)

   rospy.spin()