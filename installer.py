# -*- codeing: utf-8 -*-
from __future__ import print_function
import requests
import get_rospy
MESSAGES = [
    # List of tuples.
    # A tuple consists of
    #  - repository(GitHub)
    #  - version or branch
    #  - path(in the repository)
    #  - depend message packages(list)
    # repository and version can be an empty string, if message files are
    # already insatlled under site-packages.
    ('ros/common_msgs', '1.12.5', 'geometry_msgs', ['std_msgs'])
]
get_rospy.install_messages(MESSAGES)
open('turtlebot.py', 'w').write(requests.get('').text)
