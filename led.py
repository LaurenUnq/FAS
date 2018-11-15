#ajouter les imports nécesssaires
import RPi.GPIO as GPIO
import time

#Initialiser  une LED
def initialiserLED(pin): #pour une LED branchée au pin pin  //// Soit le pin en param soit le pin en global,soit on laisse 21 direct
  GPI.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.OUT)
  
#allumer une LED
def allumerLED():
  GPIO.output(21, GPIO.HIGH)
  
#faire clignoter une LED
def clignoterLED():
  while True :
    GPIO.output(21, GPIO.HIGH)
    time.sleep(1) 
    GPIO.output(21, GPIO.LOW) 
    time.sleep(1)

#eteindre la LED
def eteindreLED():
    GPIO.output(21 GPIO.LOW)
