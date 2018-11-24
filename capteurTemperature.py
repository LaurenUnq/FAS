# -*- coding: utf-8 -*
#Import buzzer
#Import lcd
#Import internet
#import led
#Import bouton
#Import alerter
import sys
from threading import Thread
import time
import grovepi
import math
import lcd
import led
import message

SENSOR = 4 
BLUE = 0    # The Blue colored sensor.     

class Rappel(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		ecran = lcd.Lcd("Hydratez-vous et appuyer sur le bouton bleu!",60)
		ledr = led.Led(60,0.5)
		ecran.start()
		ledr.start()
		ecran.join()
		ledr.join()
  		#buzzer()     #utilisation de la fonction depuis buzzer
  		#arretBuzzer()     #utilisation de la fonction depuis buzzer
  

def mesurerH():
	t=0
	cpt = 0
	while True:
		try:
	        	[temp,humidity] = grovepi.dht(SENSOR,BLUE)
			print("la temperature est : ", temp)
	        	if temp>=25 and t==0 :
	        		t = time.time()
	        	if temp<25:
	        		t = 0
	        		cpt = 0
	        	if ta.time() > t + 60 and t!=0:
	        		cpt = cpt + 1
	        		if cpt == 5 :
	        			r = Rappel()
	        			m = message.MailProches("Ce message vous est envoyé car votre proche n'a pas confirmé son hydration")
					r.start()
					m.start()
					r.join()
					m.join()


	        		t=t+5
	        	time.sleep(3600)
		except IOError:
        		print ("Erreur lors de la mesure")


#def alerteProcheH():
  #if (temp >= 25):
    #alerterProche(msg)
  
#def alerterSecoursH():


