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
		buzz = buzzer.Buzzer(10,0) #on modifiera le 0 plus tard
		ecran = lcd.Lcd("Hydratez-vous et appuyer sur le bouton 1!",20)
		ledr = led.Led(20,0.5)
		bt1 = bouton.Button1(20)
		bt1.start()
		buzz.start()
		ecran.start()
		ledr.start()
		self.ret = bt1.join()
		if self.ret == True:
			ecran.stop()
			ledr.stop()
			buzz.stop()
		ecran.join()
		ledr.join()
		buzz.join()

	def join(self):
		if self.ret == True:
			return 0
		else :
			return 1
  

class MesurerH(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.t = 0
		self.cpt = 0
		self.temp = 0
		self.humidity = 0 
		self.ret = 1
		self.r = Rappel()

	
	def run(self):
		#time.sleep(120)
		while True:
			try:
				[self.temp,self.humidity] = grovepi.dht(SENSOR,BLUE)
				# si la temperature est superieur ou egale a 25° on stocke l'heure
				if self.temp>=20 and self.t == 0 :
					self.t = time.time()
				# sinon on met l'heure à 0 et le compteur à 0
				if self.temp<20:
					self.t = 0
					self.cpt = 0


				if time.time() > self.t + 10 and self.t != 0:
					self.cpt = self.cpt + 1
					try :
						self.r.start()
					except:
							pass
					try :
						self.ret = self.r.join()
					except:
						pass
					if self.ret == 0:
						self.t = time.time()
						self.cpt = 0
					else:
						if self.cpt == 2:
							message.envoyerMailProches("Ce message vous est envoye car votre proche n'a pas confirme son hydration")
						if self.cpt == 4:
							message.envoyerMailSecours("Une personne est possiblement en situation de deshydration depuis plus d'une heure! Secours necessaires.")
		        # pause de 15 min
				mess = str(self.temp) + "  degres celsius"
				ecran = lcd.Lcd(mess,30)
				ecran.start()
				ecran.stop()
				time.sleep(30)
			except IOError:
				print ("Erreur lors de la mesure")

m = MesurerH()
m.start()
m.join()