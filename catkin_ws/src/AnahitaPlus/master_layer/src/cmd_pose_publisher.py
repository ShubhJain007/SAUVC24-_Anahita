#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose, Quaternion, Point
import math

def euler_to_quaternion(roll, pitch, yaw):
    # Convert Euler angles to quaternion
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    q = Quaternion()
    q.w = cy * cp * cr + sy * sp * sr
    q.x = cy * cp * sr - sy * sp * cr
    q.y = sy * cp * sr + cy * sp * cr
    q.z = sy * cp * cr - cy * sp * sr
    return q

def publish_cmd_pose(roll, pitch, yaw, x, y, z):
    # Create a publisher for the '/anahita/cmd_pose' topic with message type Pose
    cmd_pose_publisher = rospy.Publisher('/anahita/cmd_pose', Pose, queue_size=10)

    # Set the publishing rate (e.g., 1 Hz)
#    rate = rospy.Rate(15)

    while not rospy.is_shutdown():
        # Convert Euler angles to quaternion
        quaternion = euler_to_quaternion(roll, pitch, yaw)

        # Create a Pose message and set its orientation and position
        pose_msg = Pose()
        pose_msg.orientation = quaternion
        pose_msg.position = Point(x, y, z)

        # Publish the Pose message
        cmd_pose_publisher.publish(pose_msg)

        # Log the published values
        rospy.loginfo("Published quaternion orientation: %s", quaternion)
        rospy.loginfo("Published position: x=%f, y=%f, z=%f", x, y, z)

        # Sleep to maintain the desired publishing rate
#        rate.sleep()

if __name__ == '__main__':
    try:
        # Initialize the ROS node with a unique name
        rospy.init_node('pose_publisher_node', anonymous=True)

        # Read Euler angles from the command line
        roll = float(raw_input("Enter roll angle (in degrees): "))
        pitch = float(raw_input("Enter pitch angle (in degrees): "))
        yaw = float(raw_input("Enter yaw angle (in degrees): "))

        # Read position values from the command line
        x = float(raw_input("Enter x position: "))
        y = float(raw_input("Enter y position: "))
        z = float(raw_input("Enter z position: "))

        # Convert degrees to radians
        roll = math.radians(roll)
        pitch = math.radians(pitch)
        yaw = math.radians(yaw)

        # Call the publish_cmd_pose function with the provided values
        publish_cmd_pose(roll, pitch, yaw, x, y, z)

    except rospy.ROSInterruptException:
        pass

