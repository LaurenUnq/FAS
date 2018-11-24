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

	def run(self):
		t = time.time()
		while t + self.temps > time.time():
			try:
				e = grovepi.digitalRead(button1)
				if e == 1:
					return 1
				time.sleep(0.5)
				print("43")

			except IOError:
				print("Problème lecture bouton 1")
		return 0


# bouton validation
#def validerUneOperation(value):


# changer l'affichage sur le lcd
#def changermessageLCD():


t = Button1(20)
val = t.start()
t.join()
if val == 1:
	print("ok")
else :
	print(val)
	print("non")