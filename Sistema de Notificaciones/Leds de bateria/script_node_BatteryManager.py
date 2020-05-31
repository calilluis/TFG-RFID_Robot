#!/usr/bin/env python

import roslib
import rospy
from kobuki_msgs.msg import SensorState
from std_msgs.msg import String


def Avg(lst):
    return sum(lst) / len(lst)


class BatCommunication(): #here we will have both the publisher and the subscriber
    def __init__(self):
        self.batgroup=[]; #queue
        self.chargingStatus=False
        self.batstatus=["high_battery", "medium_battery", "low_battery", "critical_battery"]
        self.i=0
        self.highmed=150
        self.medlow=142
        self.lowcritical=138
        self.publish_rate = rospy.Rate(1)

        #subscriber
        rospy.Subscriber("/robot1/mobile_base/sensors/core", SensorState, self.f_bat_status)
        #publisher
        self.pub = rospy.Publisher('battery_status', String, queue_size=1)
        # publish status to leds. We just publish batstatus[i] and chargingStatus.
        # We will need a subscriber that will listen and change the leds.

    def f_bat_status(self, data):
        self.batgroup.append(float(data.battery))
        if(int(data.charger) > 0):
            self.chargingStatus = True
        else:
            self.chargingStatus = False #charging

        if len(self.batgroup)>200:
            self.batgroup.pop(0) #extract first element that entered
            if Avg(self.batgroup) == self.highmed:
                if self.i !=1:
                    self.i+=1
            elif Avg(self.batgroup) == self.medlow:
                if self.i!=2:
                    self.i+=1
            elif Avg(self.batgroup) == self.lowcritical:
                if self.i!=3:
                    self.i+=1

    def publish_data(self): #is called continuously
        if not self.chargingStatus:
            self.pub.publish("Status: " + self.batstatus[self.i])
        else:
            self.pub.publish("Status: charging")

if __name__ == '__main__':
    try:
        rospy.init_node("BatteryManager")
        bc = BatCommunication()
        while not rospy.is_shutdown():
            bc.publish_data()
            bc.publish_rate.sleep()
    except rospy.ROSInterruptException:
        rospy.loginfo("exception")
