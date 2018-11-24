import sys
from threading import Thread
import time
from grovepi import *

class Led(Thread):
	def __init__(self, tempsC, vitC):
		Thread.__init__(self)		
		self.led = 7
		self.tempsC = tempsC
		self.vitC = vitC
		pinMode(self.led,"OUTPUT")
		time.sleep(1)

	#allumer une LED
	def allumerLED(self, temps):
		digitalWrite(self.led,1)
		time.sleep(temps)

	#eteindre la LED
	def eteindreLED(self, temps):
		digitalWrite(self.led,0)
		time.sleep(temps)

	def run(self):
		tf = time.time()
	  	while time.time()< tf+self.tempsC :
	  		self.allumerLED(self.vitC)
	  		self.eteindreLED(self.vitC)

	def stop(self):
		self.running = False

	  

#thread_1 = Led(10,0.5)

#thread_1.start()

#thread_1.join()