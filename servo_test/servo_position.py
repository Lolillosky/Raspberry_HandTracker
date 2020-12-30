# The following code will help us control a servo motor an to set its angle to a desired value.
# This will help us mount the pan-tilt mechanism

import RPi.GPIO as GPIO
import time

def single_motor_demo():

    # setup the GPIO pin for the servo
    servo_pin = 13
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin,GPIO.OUT)

    # setup PWM process
    pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)

    pwm.start(7) # start PWM by rotating to 90 degrees

    for ii in range(0,3):
        pwm.ChangeDutyCycle(2.0) # rotate to 0 degrees
        time.sleep(0.5)
        pwm.ChangeDutyCycle(12.0) # rotate to 180 degrees
        time.sleep(0.5)
        pwm.ChangeDutyCycle(7.0) # rotate to 90 degrees
        time.sleep(0.5)

    pwm.ChangeDutyCycle(0) # this prevents jitter
    pwm.stop() # stops the pwm on 13
    GPIO.cleanup() # good practice when finished using a pin

def start_servo(servo_pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin,GPIO.OUT)

    # setup PWM process
    pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)

    pwm.start(7) # start PWM by rotating to 90 degrees
    time.sleep(0.5)
    #pwm.ChangeDutyCycle(0)
    #pwm.stop() # stops the pwm on 13

    return pwm


def set_angle(pwm, angle):

    if (angle >= 0) and (angle <= 180):
    
        dutycycle = 2.0 + angle / 18
        print(dutycycle)
        pwm.ChangeDutyCycle(dutycycle)
        time.sleep(0.3) 
        #pwm.ChangeDutyCycle(0)


#single_motor_demo()

pwm = start_servo(13)

for i in range(5):
    for ang in range(0,190,10):
        set_angle(pwm, ang)

set_angle(pwm, 90)


pwm.ChangeDutyCycle(0) # this prevents jitter
pwm.stop() # stops the pwm on 13

GPIO.cleanup()

