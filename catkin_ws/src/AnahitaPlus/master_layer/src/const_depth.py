#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from anahita_utils import *

cmd_vel_pub = rospy.Publisher('/anahita/cmd_vel', Twist, queue_size=10)
depth_msg = Float32()

def has_reached_depth(target_depth, current_depth, depth_threshold):
    return abs(target_depth - current_depth) <= depth_threshold

def maintain_constant_depth_execute(target_depth):
    rospy.loginfo("Maintaining constant depth: {} meters".format(target_depth))
    while not has_reached_depth(target_depth, depth_msg.data, 0.1) and not rospy.is_shutdown():
        velocity_cmd = Twist()
        velocity_cmd.linear.z = 0.1  # Set the desired linear velocity in the z-direction
        cmd_vel_pub.publish(velocity_cmd)
        rospy.sleep(0.1)

def depth_callback(msg):
    global depth_msg
    depth_msg = msg

if _name_ == '_main_':
    rospy.init_node('maintain_constant_depth')
    
    sub_depth = rospy.Subscriber('/anahita/depth', Float32, depth_callback)
    
    rospy.loginfo('Maintain constant depth node initialized')
    rospy.sleep(2)  # Allow time for subscribers to initialize
    
    target_depth = 5.0  # Set the target depth in meters
    maintain_constant_depth_execute(target_depth)
