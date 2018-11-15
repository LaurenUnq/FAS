#import Internet
#import LED
#import bouton
#Import Buzzer
#Import EcranLCD
import RPi.GPIO as GPIO
import time

# Initialiser
def initialiserFC(pin):
  GPIO.setup(pin,GPIO.IN)

def mesurerFC():

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
