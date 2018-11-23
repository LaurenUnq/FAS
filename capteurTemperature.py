#Import buzzer
#Import lcd
#Import internet
#import led
#Import bouton
#Import alerter
import time
import grovepi
import math
import lcd

SENSOR = 4 
BLUE = 0    # The Blue colored sensor.     

def rappelH():
	lcd.ecrireMessage("Hydratez-vous et appuyer sur le bouton bleu!")
  #ecrireMessage("Rappel : Hydratez-vous !")      #utilisation de la fonction depuis lcd
  #buzzer()     #utilisation de la fonction depuis buzzer
  #clignoterLED()      #utilisation de la fonction depuis led
  #time.sleep(5)
  #clearEcran()      #utilisation de la fonction depuis lcd
  #arretBuzzer()     #utilisation de la fonction depuis buzzer
  
def mesurerH():
  t=0
  while True:
    try:
    	ta = time.clock()
    	print("ici")
    	print(ta)
        [temp,humidity] = grovepi.dht(SENSOR,BLUE)
        if temp<=25 and t==0 :
        	t = ta
        if temp>25:
        	t = 0
        if ta > t + 60:
        	rappelH()
        	t=t+5
        time.sleep(20)
    except IOError:
        print ("Erreur lors de la mesure")


#def alerteProcheH():
  #if (temp >= 25):
    #alerterProche(msg)
  
#def alerterSecoursH():
mesurerH()