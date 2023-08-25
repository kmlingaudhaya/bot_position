#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from tutorials.msg import Position

def callback(data):
    rospy.loginfo("%s x: %f y: %f",data.message, data.x, data.y)  


def listener(): 
    # initialising the subscriber node
    rospy.init_node("Subscriber_Node", anonymous = True)
    rospy.Subscriber('talking_topic', Position, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass