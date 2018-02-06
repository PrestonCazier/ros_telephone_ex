#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('student2', String, queue_size=10)
def callback(data):
	my_str = data.data
	pub.publish(my_str)
        
def listener():
    rospy.init_node('telephone1', anonymous=True)
    rospy.Subscriber("student1", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
