#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# This program causes an LED to blink 3 times rapidly followed by a
#   5 second pause. The LED then blinks 4 times rapidly followed
#   by another 5 second pause. This loops indefinitely.
def Blink():
  blinks = 3
  while(1):
    for i in range(0, blinks):
      print "blink #" + str(i+1)
      GPIO.output(17,True)
      time.sleep(.1)	
      GPIO.output(17,False)
      time.sleep(.1)
    for i in range(0, 5):
      time.sleep(1)
    blinks = 7 - blinks

Blink()
            

