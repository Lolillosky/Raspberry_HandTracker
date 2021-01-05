# This file tests servo control with PCA9685 servo controller
from time import sleep
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

#kit.servo[7].angle = 180

#kit.servo[7].set_pulse_width_range(800, 2100)

#print(kit.servo[7].actuation_range)

for i in range(3):
    for ang in range(0,180):
        kit.servo[15].angle = ang
        sleep(0.01)