#import Internet
#import LED
#import bouton
#Import Buzzer
#Import EcranLCD
import sys
from threading import Thread
import RPi.GPIO as GPIO
from grovepi import *
import time

SENSOR = 4 
BLUE = 0    # The Blue colored sensor. 

# Initialiser
def initialiserFC(pin):
  GPIO.setup(pin,GPIO.IN)    

class RappelFC(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.ret = False

	def run(self):
		buzzer = buzzer.Buzzer(10,0) #on modifiera le 0 plus tard
		ecran = lcd.Lcd("C est l heure de prendre votre frequence cardiaque !",60)
		ledr = led.Led(60,0.5)
		bt1 = bouton.Button1(60)
		bt1.start()
		buzzer.start()
		ecran.start()
		ledr.start()
		self.ret = bt1.join()
		if self.ret == True:
			ecran.stop()
			ledr.stop()
			buzzer.stop()
		ecran.join()
		ledr.join()
		buzzer.join()
  		#buzzer()     #utilisation de la fonction depuis buzzer
  		#arretBuzzer()     #utilisation de la fonction depuis buzzer

  	def join(self):
  		if self.ret == True:
  			return 0
  		else :
  			return 1


#Le capteur renvoie0 quand il sent pas de batement, et 1 quand il y en a
def mesurerFC(pin,timeInt): #pin est le pin sur lequel est le capteur, time et le temps pendant lequel on prend la frequence (ex:20sec)
	pinMode(pin,"INPUT") #plus le temps time est grand plus ce sera precis
	current = time.time()
	prec = 0
	count = 0
	sec = current
	while sec < current + timeInt  :
		lec = digitalRead(pin)
		if not prec and lec :
			count += 1
		prec = lec

		sec = time.time()

	btm = count * (60/timeInt)
	print(btm)
	return btm

#def rappelFC():
  #ecrireMessage("Rappel : prendre FC !")      #utilisation de la fonction depuis lcd
  #buzzer()     #utilisation de la fonction depuis buzzer
  #clignoterLED()      #utilisation de la fonction depuis led
  #time.sleep(10)
  #clearEcran()      #utilisation de la fonction depuis lcd
  #arretBuzzer()     #utilisation de la fonction depuis buzzer

#envoyer un mail au proche
#def alerteProcheFC():
  #msg="ALERTE ! Il semblerait que Mr ou MMe X rencontre des difficultes au niveau de la frequence cardiaque ..."
  #if (temp >= 25):
    #alerterProche(msg)
    
   
#def alerterSecoursFC():

#def sauvegarderFC(): #Mettre dans la bd

mesurerFC(2,20)
