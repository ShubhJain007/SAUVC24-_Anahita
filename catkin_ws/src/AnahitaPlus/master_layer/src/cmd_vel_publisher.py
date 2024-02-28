#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def publish_cmd_vel(linear_x, linear_y, linear_z, angular_x, angular_y, angular_z):
    # Create a publisher for the '/anahita/cmd_vel' topic with message type Twist
    cmd_vel_publisher = rospy.Publisher('/anahita/cmd_vel', Twist, queue_size=10)

    # Set the publishing rate (e.g., 1 Hz)
    rate = rospy.Rate(15)

    while not rospy.is_shutdown():
        # Create a Twist message and set its linear and angular values
        twist_msg = Twist()
        twist_msg.linear.x = linear_x
        twist_msg.linear.y = linear_y
        twist_msg.linear.z = linear_z
        twist_msg.angular.x = angular_x
        twist_msg.angular.y = angular_y
        twist_msg.angular.z = angular_z

        # Publish the Twist message
        cmd_vel_publisher.publish(twist_msg)

        # Log the published values
        rospy.loginfo("Linear: (%.2f, %.2f, %.2f), Angular: (%.2f, %.2f, %.2f)",
                      linear_x, linear_y, linear_z, angular_x, angular_y, angular_z)

        # Sleep to maintain the desired publishing rate
        #rate.sleep()

if __name__ == '__main__':
    try:
        # Initialize the ROS node with a unique name
        rospy.init_node('cmd_vel_publisher_node', anonymous=True)

        # Read linear and angular values from the command line
        linear_x = float(raw_input("Enter linear velocity in x direction: "))
        linear_y = float(raw_input("Enter linear velocity in y direction: "))
        linear_z = float(raw_input("Enter linear velocity in z direction: "))
        angular_x = float(raw_input("Enter angular velocity around x axis: "))
        angular_y = float(raw_input("Enter angular velocity around y axis: "))
        angular_z = float(raw_input("Enter angular velocity around z axis: "))

        # Call the publish_cmd_vel function with the provided values
        publish_cmd_vel(linear_x, linear_y, linear_z, angular_x, angular_y, angular_z)

    except rospy.ROSInterruptException:
        pass

