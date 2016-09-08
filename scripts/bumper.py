#!/usr/bin/env python

"""
Author: Colin Myers
"""

import rospy

from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

class ForwardNode(object):
    def __init__(self):
           rospy.init_node('forward')
           self.bumperState = 0
           self.forward_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=1)
           rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.bumperEvent)
           
    def bumperEvent(self, BumperEvent):
        self.bumperState = BumperEvent.state
        
    def run(self):
           rate = rospy.Rate(10)
           twistMessage = Twist()
           while not rospy.is_shutdown():
                if  self.bumperState == 1: 
                    twistMessage.linear.x = 0.0
                    self.forward_pub.publish(twistMessage)
                else:
                    twistMessage.linear.x = 0.2
                    self.forward_pub.publish(twistMessage)
                    
if __name__ == "__main__":
    node = ForwardNode()
    node.run()
           
