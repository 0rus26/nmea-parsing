#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import pynmea2

serialStream = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=3.0)
print "go"
while True:
	sentence = serialStream.readline()
	if sentence.find('GGA') > 0:
		data = pynmea2.parse(sentence)
		print "{time}: {lat},{lon}".format(time=data.timestamp,lat=data.latitude,lon=data.longitude)