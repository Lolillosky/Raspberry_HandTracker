# This file tests servo control with PCA9685 servo controller
from time import sleep
from adafruit_servokit import ServoKit
import numpy as np



kit = ServoKit(channels=16)

#kit.servo[7].angle = 180

#kit.servo[15].set_pulse_width_range(800, 2200)

#print(kit.servo[7].actuation_range)

angles_0 = np.linspace(0,180,100)
angles_1 = np.linspace(30,150,100)



for i in range(3):
   

    for ang_0, ang_1 in zip(angles_0, angles_1):
        kit.servo[0].angle = ang_0
        kit.servo[1].angle = ang_1
        kit.servo[7].angle = ang_0
        kit.servo[15].angle = ang_1
        sleep(0.005)

    sleep(0.3)
    kit.servo[1].angle = 30 
    sleep(0.3)

    for ang_0, ang_1 in zip(angles_0[::-1], angles_1):
        kit.servo[0].angle = ang_0
        kit.servo[1].angle = ang_1
        kit.servo[7].angle = ang_0
        kit.servo[15].angle = ang_1
        sleep(0.005)

    sleep(0.3)
    kit.servo[1].angle = 30
    sleep(0.3)

kit.servo[0].angle = 90
kit.servo[1].angle = 90
kit.servo[7].angle = 90
kit.servo[15].angle = 90


'''
    for ang in range(180,-10,-10):
        kit.servo[0].angle = ang
        sleep(0.05)'''