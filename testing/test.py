"""
Listen to a topic in ROS and get the state of a robot

"""
#!/usr/bin/env python



## @package test
# @author Rohan Bhargava
# @version 0.1

import rospy

from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped



class Staterobot():
	"""
	Class for getting the state of a robot
	"""
	
	## @todo use doxypypy 
	
	def __init__(self,topic):
		"""
		Constructor for the class
		"""
		## A class variable
		self.state=PoseStamped()
		rospy.Subscriber(topic,Odometry,self.callback)
	## @param self object pointer
	## @param data Contains whatever is published on the topic
	def callback(self,data):
		"""
		Callback function for the Odometry topic. 
		
		This function will be called whenever a new message is published on a document
		"""
		
		self.state.pose=data.pose.pose
		
		self.state.header=data.header
	def getstate(self):
		"""
		Returns the state of a robot
		"""
		return self.state	
class testing(Staterobot):
	"""
	This is a class just for testing uml diagrams
	"""
	def __init__(self):
	  """The constructor"""
	  print 'constructor'
	  #obj=Staterobot('/test')
	  #print obj.state
	

if __name__=='__main__':
	obj=Staterobot('/ground_truth/state')
	rospy.init_node('spiri_state',anonymous=True)
	try:
		#print obj.position
		print obj.getstate()		
		rospy.spin()	
	except KeyboardInterrupt:
		print 'shutting down'
		
