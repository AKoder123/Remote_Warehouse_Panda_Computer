#!/usr/bin/python

import rospy
import franka_gripper.msg
import actionlib

def move():
    client = actionlib.SimpleActionClient("/franka_gripper/move", franka_gripper.msg.MoveAction)
    client.wait_for_server()
    # widths
    # 0.1 - fully open
    # 0.06 - 4x4 rubiks cube
    # 
    # 0.05 - scenario cube
    # goal = franka_gripper.msg.MoveGoal(width=0.05, speed=1.0)
    goal = franka_gripper.msg.MoveGoal(width=0.1, speed=1.0)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

if __name__ == "__main__":
    rospy.init_node("yeet_gripper")
    result = move()
    print(result)
