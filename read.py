# Serial3.py

import serial

#port = "/dev/ttyAMA0"  # Raspberry Pi 2
port = "/dev/ttyS0"    # Raspberry Pi 3

ser = serial.Serial(port, baudrate = 38400, timeout = 0.5)
while True:
    data = ser.readline()
    print (data)
