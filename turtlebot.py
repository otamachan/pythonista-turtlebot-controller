import os

import geometry_msgs.msg
import rospy
import socket
import ui

def get_localip():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.google.com', 80))
    return s.getsockname()[0]

def timer(event):
    pub.publish(geometry_msgs.msg.Twist(
        linear=geometry_msgs.msg.Vector3(x=x),
        angular=geometry_msgs.msg.Vector3(z=th)))

def connect(sender):
    global x, th, pub
    sender.superview['stop'].enabled = True
    sender.superview['x'].value = 0.5
    x = 0
    sender.superview['th'].value = 0.5
    th = 0
    if not rospy.core.is_initialized():
        os.environ['ROS_MASTER_URI'] = 'http://' + sender.superview['ip'].text + ':11311'
        os.environ['ROS_IP'] = get_localip()
        os.environ['ROS_PYTHON_LOG_CONFIG_FILE'] = ''
        rospy.init_node('turlebot_controller', disable_signals=True)
        pub = rospy.Publisher('test', geometry_msgs.msg.Twist, queue_size=10)
        rospy.Timer(rospy.Duration(0.5), timer)

def stop(sender):
    global x, th
    sender.superview['x'].value = 0.5
    x = 0
    sender.superview['th'].value = 0.5
    th = 0
    timer(None)  # send immediately

def slide_x(sender):
    global x
    x = sender.superview['x'].value - 0.5
    print(x)

def slide_th(sender):
    global th
    th = sender.superview['th'].value - 0.5
    print(th)

x = 0
th = 0

w, h = ui.get_screen_size()

view = ui.View(name='TurtleBot3 Controller', background_color='white')
view.add_subview(ui.Label(name='l1', text='Robot IP', alignment=ui.ALIGN_RIGHT))
view['l1'].frame = (10, 10, w/2-20, 30)
view.add_subview(ui.TextField(name='ip', alignment=ui.ALIGN_CENTER))
view['ip'].frame = (w/2+10, 10, w/2-20, 30)
view.add_subview(ui.Button(name='connect', title='CONNECT', border_width=1, border_color='black', action=connect))
view['connect'].frame = (w/2-60, 60, 120, 40)
view.add_subview(ui.Button(name='stop', title='STOP', border_width=1, border_color='black', background_color='red', enabled=False, action=stop))
view['stop'].frame = (w/2-60, 150, 120, 40)
view.add_subview(ui.Label(name='l2', text='X', alignment=ui.ALIGN_CENTER))
view['l2'].frame = (w/2-50, 230, 100, 30)
view.add_subview(ui.Slider(name='x', continuous=True, value=0.5, action=slide_x))
view['x'].frame = (20, 270, w-40, 30)
view.add_subview(ui.Label(name='l3', text='Theta', alignment=ui.ALIGN_CENTER))
view['l3'].frame = (w/2-50, 310, 100, 30)
view.add_subview(ui.Slider(name='th', continuous=True, value=0.5, action=slide_th))
view['th'].frame = (20, 350, w-40, 30)
view.present()
