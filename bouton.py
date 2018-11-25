# -*- coding: utf-8 -*
import sys
from threading import Thread
import time
import grovepi

button1 = 3
grovepi.pinMode(button1,"INPUT")


class Button1(Thread):

	def __init__(self, temps):
		Thread.__init__(self)
		self.temps = temps
		self._return  = False

	def run(self):
		t = time.time()
		while t + self.temps > time.time():
			try:
				e = grovepi.digitalRead(button1)
				if e == 1:
					self._return = True
					return
				time.sleep(0.5)

			except IOError:
				print("Problème lecture bouton 1")

	def join(self):
		Thread.join(self)
		return self._return

# bouton validation
#def validerUneOperation(value):


# changer l'affichage sur le lcd
#def changermessageLCD():
