import rospy
from std_msgs.msg import String

def publish_to_topic(msg):
    pub = rospy.Publisher('/rossay', String, queue_size=10)
    tx = String()
    tx.data = msg
    pub.publish(tx)


def logdebug(msg, *args, **kwargs):
    rospy.logdebug(msg, *args, **kwargs)
    publish_to_topic(msg)

def loginfo(msg, *args, **kwargs):
    rospy.loginfo(msg, *args, **kwargs)
    publish_to_topic(msg)

def logwarn(msg, *args, **kwargs):
    rospy.logwarn(msg, *args, **kwargs)
    publish_to_topic(msg)

def logerr(msg, *args, **kwargs):
    rospy.logerr(msg, *args, **kwargs)
    publish_to_topic(msg)

def logfatal(msg, *args, **kwargs): 
    rospy.logfatal(msg, *args, **kwargs)
    publish_to_topic(msg)


