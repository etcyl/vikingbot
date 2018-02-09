"""
Print sonic sensor values
"""

import ultrasonic as US

# create object for distance sensor
ultrasonicSensorBack = US.Ultrasonic()

#setup the distance sensor
ultrasonicSensorBack.setup_GPIO()

while(True):
#if distance is more than 10 cm. go back. Ig there is an obstacle stop
    ultrasonicSensorBack.get_distance
    GPIO.cleanup()
