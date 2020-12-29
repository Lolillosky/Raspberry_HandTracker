# The following code will help us control a servo motor an to set its angle to a desired value.
# This will help us mount the pan-tilt mechanism

import RPi.GPIO as GPIO
import time


def set_servo_angle(angle, servo_pin):


    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(servo_pin, GPIO.OUT)

    pwm=GPIO.PWM(servo_pin, 50)

    pwm.start(1.5)

    time.sleep(3)

    pwm.ChangeDutyCycle(5)
    time.sleep(0.5)



    pwm.stop()

    GPIO.cleanup()



set_servo_angle(0, 3)

