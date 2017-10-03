#!/usr/bin/env python
from evakit import *

if __name__ == '__main__':
    try:
        rospy.init_node('example_node', anonymous=True)
        rate = rospy.Rate(10)  # 1hz

        my_bumper = bumper()
        my_ir0 = ir(0)
        my_ir1 = ir(1)
        my_sonar0 = sonar(0)
        my_sonar1 = sonar(1)
        my_motor = motor()
        my_odometer = odom()
        
        my_motor.set_linear_speed(0.3)
        my_motor.set_angular_speed(0.5)
        my_motor.run()
        #my_motor.stop() if you want to stop motors

        while not rospy.is_shutdown():
            rospy.loginfo("---------------------------------")
            # ir0 functions and their usage
            range_ir0 = my_ir0.get_range()
            min_range_ir0 = my_ir0.get_min_range()
            max_range_ir0 = my_ir0.get_max_range()
            rospy.loginfo("range of ir0 =" + str(range_ir0))
            rospy.loginfo("minimum range of ir0 =" + str(min_range_ir0))
            rospy.loginfo("maximum range of ir0" + str (max_range_ir0))
            # ir1 functions and their usage
            range_ir1 = my_ir1.get_range()
            min_range_ir1 = my_ir1.get_min_range()
            max_range_ir1 = my_ir1.get_max_range()
            rospy.loginfo("range of ir1 =" + str(range_ir1))
            rospy.loginfo("minimum range of ir1 =" + str(min_range_ir1))
            rospy.loginfo("maximum range of ir1" + str(max_range_ir1))
            # sonar0 functions and their usage
            range_sonar0 = my_sonar0.get_range()
            min_range_sonar0 = my_sonar0.get_min_range()
            max_range_sonar0 = my_sonar0.get_max_range()
            rospy.loginfo("range of sonar0 =" + str(range_sonar0))
            rospy.loginfo("minimum range of sonar0 =" + str(min_range_sonar0))
            rospy.loginfo("maximum range of sonar0" + str(max_range_sonar0))
            # sonar1 functions and their usages
            range_sonar1 = my_sonar1.get_range()
            min_range_sonar1 = my_sonar1.get_min_range()
            max_range_sonar1 = my_sonar1.get_max_range()
            rospy.loginfo("range of sonar1 =" + str(range_sonar1))
            rospy.loginfo("minimum range of sonar1 =" + str(min_range_sonar1))
            rospy.loginfo("maximum range of sonar1" + str(max_range_sonar1))
            # bumper function and its usage
            state_bumper0 = my_bumper.get_state()
            rospy.loginfo("state of bumper=" + str(state_bumper0))
            # odom functions and their usage
            odometer_pos_x = my_odometer.get_pos_x()
            odometer_pos_y = my_odometer.get_pos_y()
            odometer_vel_x = my_odometer.get_vel_x()
            odometer_vel_z = my_odometer.get_vel_z()
            rospy.loginfo("x position of robot=" + str(odometer_pos_x))
            rospy.loginfo("y position of robot=" + str(odometer_pos_y))
            rospy.loginfo("x velocity of robot=" + str(odometer_vel_x))
            rospy.loginfo("z velocity of robot=" + str(odometer_vel_z))
            rospy.loginfo("---------------------------------")
            rate.sleep()

    except rospy.ROSInterruptException:
        pass