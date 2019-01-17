# -*- coding: utf-8 -*

import sys
from threading import Thread
import time
import grovepi
import math
import lcd
import led
import message
import bouton
import buzzer

SENSOR = 4 
BLUE = 0    # The Blue colored sensor.     

class Rappel(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.ret = False

	def run(self):
		buzzer = buzzer.Buzzer(10,0) #on modifiera le 0 plus tard
		ecran = lcd.Lcd("Hydratez-vous et appuyer sur le bouton bleu!",120)
		ledr = led.Led(120,0.5)
		bt1 = bouton.Button1(120)
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
  

class MesurerH(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.t=0
		self.cpt = 0
		self.temp = 0
		self.humidity = 0 
		self.ret = 1
		self.r = Rappel()

	
	def run(self):
		while True:
			try:
				[self.temp,self.humidity] = grovepi.dht(SENSOR,BLUE)
				# si la temperature est superieur ou egale a 25° on stocke l'heure
				if self.temp>=25 and t==0 :
					self.t = time.time()
				# sinon on met l'heure à 0 et le compteur à 0
				if self.temp<25:
					self.t = 0
					self.cpt = 0


				if time.time() > self.t + 60 and self.t!=0:
					self.cpt = self.cpt + 1
					self.r.start()
					self.ret = self.r.join()
					if self.ret == 0:
						self.t = time.time()
					else:
						if self.cpt == 2:
							message.envoyerMailProches("Ce message vous est envoyé car votre proche n'a pas confirmé son hydration")
						if self.cpt == 4:
							message.envoyerMailSecours("Une personne est possiblement en situation de déshydration depuis plus d'une heure! Secours nécessaires.")
		        # pause de 15 min
				time.sleep(900)
			except IOError:
				print ("Erreur lors de la mesure")


