import rospy
import baxter_interface
import time
import numpy as np
import matplotlib.pyplot as plt

f = open('monitor_efforts.log', 'w')

f.write("time,w0,w1,w2,e0,e1,s0,s2\n")

def makeFig():
   line_s0, = plt.plot(x,y_s0)
   line_s1, = plt.plot(x,y_s1)
   line_e0, = plt.plot(x,y_e0)
   line_e1, = plt.plot(x,y_e1)
   line_w0, = plt.plot(x,y_w0)
   line_w1, = plt.plot(x,y_w1)
   line_w2, = plt.plot(x,y_w2)

   plt.legend( [line_s0, line_s1, line_e0, line_e1, line_w0, line_w1, line_w2], ['S0', 'S1', 'E0', 'E1', 'W0', 'W1', 'W2' ] )

x = list()
y_s0 = list()
y_s1 = list()
y_e0 = list()
y_e1 = list()
y_w0 = list()
y_w1 = list()
y_w2 = list()

plt.ion()
plt.show()
plt.gca().set_color_cycle(['red', 'green', 'blue', 'purple', 'orange', 'pink', 'grey'])

i = 0L
rospy.init_node('Hello_Baxter')
while not rospy.is_shutdown():
    i = i + 1
    limb_left = baxter_interface.Limb('left')
    efforts = limb_left.joint_efforts()
    print("w0[%4.2f] w1[%4.2f] w2[%4.2f] e0[%4.2f] e1[%4.2f] s0[%4.2f] s1[%4.2f]" % ( efforts['left_w0'], efforts['left_w1'], efforts['left_w2'], efforts['left_e0'], efforts['left_e1'], efforts['left_s0'], efforts['left_s1']) )
    f.write("%.2f %4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %4.2f\n" % ( time.time(), efforts['left_w0'], efforts['left_w1'], efforts['left_w2'], efforts['left_e0'], efforts['left_e1'], efforts['left_s0'], efforts['left_s1']) )
    x.append(i)
    y_s0.append( efforts['left_s0'] )
    y_s1.append( efforts['left_s1'] )
    y_e0.append( efforts['left_e0'] )
    y_e1.append( efforts['left_e1'] )
    y_w0.append( efforts['left_w0'] )
    y_w1.append( efforts['left_w1'] )
    y_w2.append( efforts['left_w2'] )
    makeFig(); plt.draw()
    rospy.sleep(0.2)
    if i > 101:
        del x[i-101]
        del y_s0[i-101]
        del y_s1[i-101]
        del y_e0[i-101]
        del y_e1[i-101]
        del y_w0[i-101]
        del y_w1[i-101]
        del y_w2[i-101]

    plt.axis([i, i-100, -30, 30])

f.close()
