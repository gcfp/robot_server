# Create a program that automates the movement of the rasptank robot and using the ultrasonic sensor to detect obstacles and avoid them.

# Import the necessary libraries
import RPi.GPIO as GPIO
import time
import sys

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins for the ultrasonic sensor
TRIG = 23
ECHO = 24

# Set the GPIO pins for the motors
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 10

# Set the GPIO pins for the ultrasonic sensor
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Set the GPIO pins for the motors
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Set the GPIO pins for the ultrasonic sensor
GPIO.output(TRIG, False)

# Set the GPIO pins for the motors
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# Set the GPIO pins for the ultrasonic sensor
time.sleep(2)

# Set the GPIO pins for the motors
time.sleep(2)

# Set the GPIO pins for the ultrasonic sensor
def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

# Set the GPIO pins for the motors
def forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

# Set the GPIO pins for the ultrasonic sensor
def backward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

# Set the GPIO pins for the motors
def left():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

# Set the GPIO pins for the ultrasonic sensor
def right():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

# Set the GPIO pins for the motors
def stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

# Set the GPIO pins for the ultrasonic sensor
def main():
    try:
        while True:
            dist = distance()
            print "Distance:", dist, "cm"
            if dist > 30:
                forward()
            elif dist <= 30:
                stop()
                time.sleep(1)
                left()
                time.sleep(1)
                stop()
                time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

# Set the GPIO pins for the motors
if __name__ == '__main__':
    main()