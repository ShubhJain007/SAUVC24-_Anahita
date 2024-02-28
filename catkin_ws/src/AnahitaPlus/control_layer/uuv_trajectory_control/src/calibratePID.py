#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Wrench
from scipy.optimize import minimize
from itertools import product

def calibrate_publisher():
    # Initialize the ROS node
    rospy.init_node('calibrate_publisher', anonymous=True)

    # Create a publisher for the "calibrate" topic with custom message type
    pub = rospy.Publisher('calibrate', Float32MultiArray, queue_size=10)

    # Create a subscriber for the "/anahita/thruster_manager/input_stamped" topic
    def wrench_callback(msg):
        # Extract .force.x value
        force_x_value = msg.force.x  # Update the value in the list

        # Print for visualization (optional)
        rospy.loginfo("Received force.x value: %s", force_x_value[0])

    rospy.Subscriber("/anahita/thruster_manager/input_stamped", Wrench, wrench_callback)

    # Set the loop rate
    rate = rospy.Rate(100)  # 1 Hz

    def objective_function(variables):
        # This function returns the value that needs to be minimized
        return abs(force_x_value)  # variables[0] represents x

    def callback_update(arr):
        # Update the message data with the optimized variables
        message.data = arr
    curr = 99999
    # Try all combinations of three values for the initial guess
    for initial_guess in product(range(100), repeat=3):
        # Minimize the objective function for the current initial guess
        result = minimize(objective_function, initial_guess, method='BFGS', callback=callback_update)

        # Extract the optimal variables
        optimal_variables = result.x
        if(result < curr):
            curr=result          
        # Print the result
        print("Initial guess:", initial_guess)
        print("Optimal variables:", optimal_variables)
        print("Minimum value of the target function:", result.fun)
         
        # Message to be published (an array of size 3 with float values)
        message.data = optimal_variables

        # Publish the message on the "calibrate" topic
        pub.publish(message)

        # Sleep to maintain the loop rate
        rate.sleep()
    print(curr)

if __name__ == '__main__':
    force_x_value = 9999999  # Initial value as a list
    message = Float32MultiArray()

    try:
        calibrate_publisher()
    except rospy.ROSInterruptException:
        pass

