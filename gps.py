#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import pynmea2
import math

def toDegree(value): # calculate (lan or lat) from DegreeMinutes to Degree
	degree = float(str(value)[:2])
	minutes = float(str(value)[2:])
	mindeg = minutes/60
	return degree+mindeg


#Formel: θ = atan2(sin(Δlong).cos(lat2), cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
# input: pA Array [lat, lon], pB Array [lat, lon]
def compass(pointA, pointB):
	if (type(pointA) != tuple) or (type(pointB) != tuple):
		raise TypeError("Only tuples, GPS online?")
	lat1 = math.radians(pointA[0])
	lat2 = math.radians(pointB[0])

	diffLong = math.radians(pointB[1] - pointA[1])

	x = math.sin(diffLong) * math.cos(lat2)
	y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)* math.cos(lat2) * math.cos(diffLong))

	initial_bearing = math.atan2(x, y)
	initial_bearing = math.degrees(initial_bearing)
	compass_bearing = (initial_bearing + 360) % 360
	return compass_bearing

def getOrientation(data):
	arr = str(data).split(",")
	return arr[8]

serialStream = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=3.0)
print "---→ start"
# set Aimpoints
aim = (47.67130103854597, 9.181145131587984)

while True:
	sentence = serialStream.readline()
	if sentence.find('GPRMC') > 0:
		data = pynmea2.parse(sentence)
		#print "{time}: {lat},{lon}".format(time=data.timestamp,lat=data.latitude,lon=data.longitude)
		loc  = (data.latitude, data.longitude)
		print compass(loc, aim)
		print "ME:", getOrientation(data)
