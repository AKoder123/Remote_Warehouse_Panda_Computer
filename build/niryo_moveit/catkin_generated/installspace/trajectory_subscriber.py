#!/usr/bin/env python2
"""
    Subscribes to SourceDestination topic.
    Uses MoveIt to compute a trajectory from the target to the destination.
    Trajectory is then published to PickAndPlaceTrajectory topic.
"""
import rospy

from niryo_moveit.msg import NiryoMoveitJoints


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard:\n%s", data)
    rospy.loginfo(data.joints)

def listener():
    rospy.init_node('Trajectory_Subscriber', anonymous=True)
    rospy.Subscriber("/niryo_joints", NiryoMoveitJoints, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
