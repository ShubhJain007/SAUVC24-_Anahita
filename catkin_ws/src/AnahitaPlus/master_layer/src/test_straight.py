#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from anahita_utils import *

cmd_vel_pub = rospy.Publisher('/anahita/cmd_vel', Twist, queue_size=10)
odom_msg = Twist()

def has_reached(target_x, curr_x, pos_threshold):
    return abs(target_x - curr_x) <= pos_threshold

def move_forward_execute(target_x):
    rospy.loginfo("Moving forward to x-coordinate: {}".format(target_x))
    while not has_reached(target_x, odom_msg.pose.pose.position.x, 0.1) and not rospy.is_shutdown():
        velocity_cmd = Twist()
        velocity_cmd.linear.x = 0.1  # Set the desired linear velocity
        cmd_vel_pub.publish(velocity_cmd)
        rospy.sleep(0.1)

def odometry_callback (msg):
    global odom_msg
    odom_msg = msg

if _name_ == '_main_':
    rospy.init_node('move_to_x_coordinate')
    
    sub_odometry = rospy.Subscriber('/anahita/pose_gt', numpy_msg(Odometry), odometry_callback)
    
    rospy.loginfo('Move to x-coordinate node initialized')
    rospy.sleep(2)  # Allow time for subscribers to initialize
    
    target_x_coordinate = 10.0  # Set the target x-coordinate
    move_forward_execute(target_x_coordinate)
