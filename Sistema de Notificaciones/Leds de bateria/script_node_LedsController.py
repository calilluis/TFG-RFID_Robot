#to execute: sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python pub_subs_batteryStatus.py

import roslib
import rospy
from kobuki_msgs.msg import SensorState
from std_msgs.msg import String
import time
from neopixel import *
import argparse


class ActivateLeds():
    def __init__(self):
        self.LED_COUNT      = 4      # Number of LED pixels.
        self.LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        self.args = self.parser.parse_args()

        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ,
        self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)# Crea un objeto NeoPixel con la configuración apropiada.
        self.strip.begin()  # Inicializa la libreria


        rospy.Subscriber("battery_status",String, self.f_act_leds)

    def colorWipe(strip, color, number):
        for i in range(number):
            strip.setPixelColor(i, color)
            strip.show()

    def f_act_leds(self, data):
        data=data.split()
        data=data[1] #message type is like "Status: charging". We just grab the last part.
        if data == "critical_battery":
            colorWipe(self.strip, Color(255, 0 , 0), 1)  # Red wipe.
            time.sleep(500/1000.0) # make it blink, if it takes to long to recieve next msg, implement a bucle.
        elif data == "low_battery":
            colorWipe(self.strip, Color(0, 255, 0), 2)  # green wipe
        elif data == "medium_battery":
            colorWipe(self.strip, Color(0, 255, 0), 3)
        elif data == "high_battery":
            colorWipe(self.strip, Color(0, 255, 0), 4)
        elif data == "charging":
            colorWipe(self.strip, Color(0, 255, 0), 4)
            time.sleep(500/1000.0) #make it blink, if it takes to long implement a bucle.



if __name__ == '__main__':
	try:
        rospy.init_node("LedsController")
		al= ActivateLeds()
	    except rospy.ROSInterruptException:
		rospy.loginfo("exception")
