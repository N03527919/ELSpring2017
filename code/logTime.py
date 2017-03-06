#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys

# The readTime function retrieves the current date and time in the specified format
def readTime():
  currentDate = time.strftime("%Y/%m/%d")
  currentTime = time.strftime("%H:%M:%S")
  return [currentDate, currentTime]

# The logTime function calls readTime and stores the formatted date and time
#  into a database. Successful execution will store the current date into the 
#  first column of the database and current time in the second column.
def logTime():
  con = mydb.connect('/home/pi/Assignments/sqlite_py/testTime.db')
  with con:
    try:
      [d, t] = readTime()
      cur = con.cursor()
      cur.execute('insert into testTime values(?,?)',(d,t))
      print "Date and Time logged"
    except:
      print "Error!!"

logTime()  
