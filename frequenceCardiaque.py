#import Internet
#import LED
#import bouton
#Import Buzzer
#Import EcranLCD
import RPi.GPIO as GPIO
from grovepi import *
import time

# Initialiser
def initialiserFC(pin):
  GPIO.setup(pin,GPIO.IN)

#Le capteur renvoie0 quand il sent pas de batement, et 1 quand il y en a
def mesurerFC(pin,timeInt): #pin est le pin sur lequel est le capteur, time et le temps pendant lequel on prend la fréquence (ex:20sec)
	pinMode(pin,"INPUT") #plus le temps time est grand plus ce sera précis
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

	return btm

def rappelFC():
  #ecrireMessage("Rappel : prendre FC !")      #utilisation de la fonction depuis lcd
  #buzzer()     #utilisation de la fonction depuis buzzer
  #clignoterLED()      #utilisation de la fonction depuis led
  #time.sleep(10)
  #clearEcran()      #utilisation de la fonction depuis lcd
  #arretBuzzer()     #utilisation de la fonction depuis buzzer

#envoyer un mail au proche
def alerteProcheFC():
  #msg="ALERTE ! Il semblerait que Mr ou MMe X rencontre des difficultés au niveau de la fréquence cardiaque ..."
  #if (temp >= 25):
    #alerterProche(msg)
    
   
#def alerterSecoursFC():

def sauvegarderFC(): #Mettre dans la bd
