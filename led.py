#ajouter les imports nécesssaires
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

#broche21
#allumer une LED
def allumerLED():
  GPIO.output(21, GPIO.HIGH)
  
#faire clignoter une LED
def clignoterLED():
  while True :
    GPIO.output(25, GPIO.HIGH)
    time.sleep(1) 
    GPIO.output(25, GPIO.LOW) 
    time.sleep(1)

#eteindre la LED
def eteindreLED():
    GPIO.output(25 GPIO.LOW)
