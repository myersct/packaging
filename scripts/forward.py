#!/usr/bin/env python

"""
Author: Colin Myers
"""

import rospy

from geometry_msgs.msg import Twist

class ForwardNode(object):
    def __init__(self):
           rospy.init_node('forward')
           self.forward_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=1)

    def run(self):
           rate = rospy.Rate(10)
           twistMessage = Twist()
           while not rospy.is_shutdown():
                twistMessage.linear.x = 0.2
                self.forward_pub.publish(twistMessage)
                
if __name__ == "__main__":
    node = ForwardNode()
    node.run()
           
