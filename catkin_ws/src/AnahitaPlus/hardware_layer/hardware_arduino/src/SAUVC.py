#!/usr/bin/env python

import rospy
from anahita_msgs.msg import Thrust

def collect_thruster_values1():
    pwm_msg = Thrust()

    pwm_msg.sideward_front = sideward_front=250
    pwm_msg.sideward_back = sideward_back = 0
    pwm_msg.forward_left = forward_left = -230
    pwm_msg.forward_right = forward_right = 230
    pwm_msg.upward_north_east = upward_north_east = 30
    pwm_msg.upward_north_west = upward_north_west = 0
    pwm_msg.upward_south_east = upward_south_east = 250
    pwm_msg.upward_south_west = upward_south_west = 0
    return pwm_msg
def collect_thruster_valuesstable():
    pwm_msg = Thrust()

    pwm_msg.sideward_front = sideward_front=105
    pwm_msg.sideward_back = sideward_back = 0
    pwm_msg.forward_left = forward_left = -85
    pwm_msg.forward_right = forward_right = 85
    pwm_msg.upward_north_east = upward_north_east = 33
    pwm_msg.upward_north_west = upward_north_west = -50
    pwm_msg.upward_south_east = upward_south_east = 105
    pwm_msg.upward_south_west = upward_south_west = -60
    return pwm_msg
def collect_thruster_valuesstableforward():
    pwm_msg = Thrust()

    pwm_msg.sideward_front = sideward_front=105
    pwm_msg.sideward_back = sideward_back = 0
    pwm_msg.forward_left = forward_left = -85
    pwm_msg.forward_right = forward_right = 85
    pwm_msg.upward_north_east = upward_north_east = 40
    pwm_msg.upward_north_west = upward_north_west = 100
    pwm_msg.upward_south_east = upward_south_east = 105
    pwm_msg.upward_south_west = upward_south_west = 140
    return pwm_msg
def collect_thruster_valuesstableyaw():
    pwm_msg = Thrust()

    pwm_msg.sideward_front = sideward_front=105
    pwm_msg.sideward_back = sideward_back = 0
    pwm_msg.forward_left = forward_left = -85
    pwm_msg.forward_right = forward_right = 85
    pwm_msg.upward_north_east = upward_north_east = 53
    pwm_msg.upward_north_west = upward_north_west = -100
    pwm_msg.upward_south_east = upward_south_east = 105
    pwm_msg.upward_south_west = upward_south_west = 100
    return pwm_msg
def collect_thruster_values4():
    pwm_msg = Thrust()

    pwm_msg.sideward_front = sideward_front=250
    pwm_msg.sideward_back = sideward_back =0
    pwm_msg.forward_left = forward_left = -200
    pwm_msg.forward_right = forward_right =200
    pwm_msg.upward_north_east = upward_north_east = 53
    pwm_msg.upward_north_west = upward_north_west = 100
    pwm_msg.upward_south_east = upward_south_east = 250
    pwm_msg.upward_south_west = upward_south_west =100
    return pwm_msg

def collect_thruster_values5():
    pwm_msg = Thrust()

    pwm_msg.sideward_front = sideward_front=250
    pwm_msg.sideward_back = sideward_back =0
    pwm_msg.forward_left = forward_left = -200
    pwm_msg.forward_right = forward_right =200
    pwm_msg.upward_north_east = upward_north_east = 56
    pwm_msg.upward_north_west = upward_north_west =0
    pwm_msg.upward_south_east = upward_south_east = 250
    pwm_msg.upward_south_west = upward_south_west =0
    return pwm_msg

def collect_thruster_values6():
    pwm_msg = Thrust()

    pwm_msg.sideward_front = sideward_front=0
    pwm_msg.sideward_back = sideward_back=0
    pwm_msg.forward_left = forward_left = 0
    pwm_msg.forward_right = forward_right =0
    pwm_msg.upward_north_east = upward_north_east = 0
    pwm_msg.upward_north_west = upward_north_west =0
    pwm_msg.upward_south_east = upward_south_east = 00
    pwm_msg.upward_south_west = upward_south_west =0 
    return pwm_msg



def collect_thruster_values2():
    pwm_msg = Thrust()

    sideward_front = int(input("Enter value for sideward_front thruster: "))
    sideward_back = int(input("Enter value for sideward_back thruster: "))
    forward_left = int(input("Enter value for forward_left thruster: "))
    forward_right = int(input("Enter value for forwarright thruster: "))
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

def collect_thruster_values3():
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
	    
	    #rospy.sleep(60)
            pwm_msg = collect_thruster_values1()
            pose_cmd_pub.publish(pwm_msg)
            rospy.loginfo("Published the message: " + str(pwm_msg))
            # Introduce a time delay here (e.g., 1 second)
            rospy.sleep(2)  # Delay for 1 second
            pwm_msg = collect_thruster_valuesstable()
            pose_cmd_pub.publish(pwm_msg)	    
	    rospy.sleep(10)
            pwm_msg = collect_thruster_valuesstableforward()
            pose_cmd_pub.publish(pwm_msg)
            rospy.sleep(30)
            pwm_msg = collect_thruster_valuesstableyaw()
            pose_cmd_pub.publish(pwm_msg)
            rospy.sleep(2)
            pwm_msg = collect_thruster_valuesstable()
            rospy.sleep(5)
            pwm_msg = collect_thruster_valuesstableforward()
            rospy.sleep(10)
            pwm_msg = collect_thruster_values6()
            pose_cmd_pub.publish(pwm_msg)
    except rospy.ROSInterruptException:
        print("ROS Interrupted.")
    except Exception as e:
        print("Error in file:", str(e))

