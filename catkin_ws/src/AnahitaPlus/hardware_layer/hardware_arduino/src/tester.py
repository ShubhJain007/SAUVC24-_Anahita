#!/usr/bin/env python

import rospy
from anahita_msgs.msg import Thrust

looping = 1
pwm_msg = Thrust()

if __name__ == '__main__':

    rospy.init_node('tester_arduino')

    pose_cmd_pub = rospy.Publisher('/pwm', Thrust, queue_size=10, latch=True)

    try:
	while not rospy.is_shutdown():
		for i in range (-100,100,10):
			s=0
			pwm_msg.sideward_front =s
			pwm_msg.sideward_back =s #kharab
			pwm_msg.forward_left = s
			pwm_msg.forward_right = s
			pwm_msg.upward_north_east = s
			pwm_msg.upward_north_west = s
			pwm_msg.upward_south_east = s
			pwm_msg.upward_south_west = s #--
			i=i+10
					    #rospy.sleep(0.0001)
	 		pose_cmd_pub.publish(pwm_msg)
			rospy.loginfo("Published the message: " + str(pwm_msg))
			rospy.sleep(0.001)
		#for i in range (-400,400,10):
			#pwm_msg.forward_left = i
			#pwm_msg.upward_north_east = i
			#i=i+10
			#for j in range(-400,400,10):
				#pwm_msg.sideward_back = j
				#pwm_msg.upward_north_west = j
				#j= j+10
				#for k in range(-400,400,10):
				   # pwm_msg.sideward_front = k
				    #pwm_msg.upward_south_east = k
				    #k= k+10
				    #for l in range(-400,400,10):
					   # pwm_msg.forward_right = l
					   # pwm_msg.upward_south_west = l
					   # l = l+10

					    #pose_cmd_pub.publish(pwm_msg)
	                                    #rospy.loginfo("Published the message: " + str(pwm_msg))

												
	
    except:
	print("Error in file")
	exit()


 
    	
