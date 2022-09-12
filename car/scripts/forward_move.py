#!/usr/bin/env python3
import rospy
import time
import numpy as np
from geometry_msgs.msg import Twist
pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
vel_msg = Twist()
def move():
    time_sim=int(input("input the time of simulation"))
    lr= rospy.get_param("/cg_front")
    lf=rospy.get_param("/cg_back")
    speed = abs(float(input("Input your speed:")))
    steer_angle= float(input("input the steer angle:"))
    beta= np.arctan( ( lr/(lr+lf) )*np.tan(steer_angle) )
    vel_msg.linear.x=speed*np.cos(beta+steer_angle)
    vel_msg.linear.y=speed*np.sin(beta+steer_angle)
    vel_msg.angular.z=((speed/lr+lf))*np.cos(beta)*np.tan(steer_angle)
    while(time_sim!=0):
     steer_angle-=0.1*steer_angle
     vel_msg.linear.x=speed*np.cos(beta+steer_angle)
     vel_msg.linear.y=speed*np.sin(beta+steer_angle)
     vel_msg.angular.z=((speed/lr+lf))*np.cos(beta)*np.tan(steer_angle)
     pub.publish(vel_msg)
     time.sleep(1)
     time_sim=time_sim-1
    
    
def stop():
   vel_msg.linear.x=0
   vel_msg.linear.y=0
   vel_msg.angular.z=0
   pub.publish(vel_msg)


if __name__ == '__main__':
    try:
         rospy.init_node('car_node')
         rospy.loginfo('hello from controller_node')
         move()
         stop()
         
    except rospy.ROSInterruptException: pass