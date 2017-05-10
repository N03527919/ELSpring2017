#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys
import Adafruit_DHT

# This function uses an Adafruit DHT22 digital temperature and humidity sensor to detect
#  the temperature in degrees Celsius, and percent humidity. The temperature is converted
#  to Fahrenheit. Both measurements are returned along with the time and date of the measurement
def readTemp():
  humidity, temperature = Adafruit_DHT.read_retry(22,27) # DHT type 22, GPIO port pin #27
  humidity = round(humidity, 2)
  temperature = round( (temperature * 9/5.0000 + 32),2 )
  currentDate = time.strftime('%x')
  currentTime = time.strftime('%X %Z')
  
  return [currentDate, currentTime, temperature, humidity]

# This function calls readTemp and stores the time and temperature data into
#   a database. 
def logTemperature():
  con = mydb.connect('/home/pi/Project/retrieveData2.db')
  with con:
    try:
      [d,t,T,h]=readTemp()
      cur = con.cursor()
      cur.execute('insert into data_collection values(?,?,?,?)',(d,t,T,h))
    except:
      print "Error!!"

logTemperature()
