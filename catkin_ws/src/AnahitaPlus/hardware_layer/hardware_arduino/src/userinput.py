#!/usr/bin/env python

import rospy
from anahita_msgs.msg import Thrust


def collect_thruster_values():
	pwm_msg = Thrust()

	sideward_front = int(input("Enter value for sideward_front thruster: "))
	sideward_back = int(input("Enter value for sideward_back thruster: "))
	forward_left = int(input("Enter value for forward_left thruster: "))
	forward_right = int(input("Enter value for forward_right thruster: "))
	upward_north_east = int(input("Enter value for upward_north_east thruster: "))
	upward_north_west = int(input("Enter value for upward_north_west thruster: "))
	upward_south_east = int(input("Enter value for upward_south_east thruster: "))
	upward_south_west = int(input("Enter value for upward_south_west thruster: "))
	pwm_msg.sideward_front = sideward_front
	pwm_msg.sideward_back = sideward_back
	pwm_msg.forward_left = forward_left
	pwm_msg.forward_right = forward_right
	pwm_msg.upward_north_east = upward_north_east
	pwm_msg.upward_north_west = upward_north_west
	pwm_msg.upward_south_east = upward_south_east
	pwm_msg.upward_south_west = upward_south_west
	return pwm_msg

if __name__ == '__main__':
	rospy.init_node('tester_arduino')
	pose_cmd_pub = rospy.Publisher('/pwm', Thrust, queue_size=10)

	try:
		while not rospy.is_shutdown():
			pwm_msg = collect_thruster_values()	
			pose_cmd_pub.publish(pwm_msg)	
			rospy.loginfo("Published the message: " + str(pwm_msg))
	except rospy.ROSInterruptException:
		print("ROS Interrupted.")
	except Exception as e:
		print("Error in file:", str(e))
