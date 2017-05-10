#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys

# The function uses a temperature sensor to detect the temperature is degrees
#  Celsius. The temperature is convered to Fahrenheit. Both measurements are
#  returned along with the time of the measurement
def readTemp():
  tempfile = open("/sys/bus/w1/devices/28-000008ab85a7/w1_slave")
  tempfile_text = tempfile.read()
  currentTime = time.strftime('%x %X %Z')
  tempfile.close()
  tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
  tempF=tempC*9.0/5.0+32.0
  return [currentTime, tempC, tempF]

# This function calls readTemp and stores the time and temperature data into
#   a database. The function records 20 total measurements, pausing for 30
#   seconds in between each. 
def logTemperature():
  con = mydb.connect('/home/pi/Assignments/Temp_Sensor2/TempData.db')
  with con:
    for i in range(0,20):
      try:
        [t,C,F]=readTemp()
        print "Measurement: " + str(i+1) + " = %s F" %F
        cur = con.cursor()
        cur.execute('insert into TempData values(?,?,?)',(t,C,F))
        print "Temperature logged"
      except:
        print "Error!!"
      time.sleep(30)


logTemperature()
