#!/usr/bin/python3

import pigpio
import DHT22
import datetime
import time

pi = pigpio.pi()
s = DHT22.sensor(pi, 4)
f = open("templog.csv","a", 1)

while True:
  s.trigger()
  time.sleep(0.2)
  temp = s.temperature() * 9/5.0 + 32 
  now = datetime.datetime.now()
  f.write ("{},{:.2f},{:.2f}\r\n".format(
    now.strftime("%Y-%m-%d %H:%M:%S"),s.humidity(), temp ))
  f.flush
  time.sleep(59.8)
