#! /usr/bin/env python3
import rospy
import sys

rospy.init_node('python{}'.format(sys.version[0]))

rospy.loginfo('python{}'.format(sys.version[0]))

rospy.spin()
