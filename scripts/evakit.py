#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Range
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from im_msgs.msg import Battery
class ir:
    def __init__(self,id_no):
        self.id_no = id_no
        self.count=0
        self.range_value = float(0)
        self.max_range = float (0)
        self.min_range = float (0)
        self.sub = rospy.Subscriber('ir'+str(id_no), Range, self.ir_callback)

    def ir_callback(self, msg):
        self.range_value = msg.range
        self.max_range = msg.max_range
        self.min_range =msg.min_range
        if((self.range_value >= 0.05) and (self.range_value <=0.75) and self.count<=4):
            self.count=self.count+1
    def get_range(self):
        return self.range_value

    def get_min_range(self):
        return self.min_range

    def get_max_range(self):
        return self.max_range
    def is_it_work(self):
        if (self.count >= 3):
            return True
        else:
            return False
class sonar:
    def __init__(self,id_no):
        self.id_no = id_no
        self.count= 0
        self.range_value = float (0)
        self.max_range = float (0)
        self.min_range = float (0)
        self.sub = rospy.Subscriber('sonar'+str(id_no), Range, self.sonar_callback)
    
    def sonar_callback(self, msg):
        self.range_value = msg.range
        self.max_range = msg.max_range
        self.min_range =msg.min_range
        if((self.range_value >= 0.05) and (self.range_value <=4.95) and self.count<=4):
            self.count=self.count+1
    def is_it_work(self):
        if (self.count >= 3):
            return True
        else:
            return False

    def get_range(self):
        return self.range_value

    def get_min_range(self):
        return self.min_range

    def get_max_range(self):
        return self.max_range

class odom:
    def __init__(self):
        self.pos_x = float (0)
        self.pos_y = float (0)
        self.pos_z = float (0)
        self.ori_z = float (0)
        self.ori_w = float (0)
        self.vel_x = float (0)
        self.vel_z = float (0)
        self.sub = rospy.Subscriber('odom', Odometry, self.odom_callback)

    def odom_callback(self, msg):
        self.pos_x = msg.pose.pose.position.x
        self.pos_y = msg.pose.pose.position.y
        self.pos_z = msg.pose.pose.position.z
        self.vel_x = msg.twist.twist.linear.x
        self.vel_z = msg.twist.twist.angular.z
        self.ori_z = msg.pose.pose.orientation.z
        self.ori_w = msg.pose.pose.orientation.w


    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_pos_z(self):
        return self.pos_z

    def get_vel_x(self):
        return self.vel_x

    def get_vel_z(self):
        return self.vel_z

    def get_ori_z(self):
        return self.ori_z

    def get_ori_w(self):
        return self.ori_w

class motor:
    def __init__(self):
        self.speed = Twist()
        self.speed.linear.x = float(0)
        self.speed.angular.z = float(0)
        self.pub = rospy.Publisher('cmd_vel',Twist, queue_size=100)
        self.pub.publish(self.speed)

    def set_linear_speed(self, linear_speed):
        self.speed.linear.x = float(linear_speed)

    def set_angular_speed(self, angular_speed):
        self.speed.angular.z = float(angular_speed)

    def run(self):
        self.pub.publish(self.speed)

    def stop(self):
        stop_variable = Twist()
        stop_variable.linear.x = float(0)
        stop_variable.angular.z = float(0)
        self.pub.publish(stop_variable)

class bumper:
    def __init__(self):
        self.state = Bool()
        self.state.data = False
        self.sub=rospy.Subscriber('bumper',Bool,self.bumper_callback)

    def bumper_callback(self, msg):
        self.state.data=msg.data

    def get_state(self):
        return self.state.data

class battery:
    def __init__(self):
        self.voltage = 0.0
        self.sub=rospy.Subscriber('battery',Battery,self.bumper_callback)

    def bumper_callback(self, msg):
        self.voltage=msg.voltage

    def get_voltage(self):
        return self.voltage















