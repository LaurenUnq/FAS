import sys
from threading import Thread
import smbus
import time

class Lcd(Thread):
	
	def __init__(self, message, duree):
		Thread.__init__(self)
		self.message = message
		self.duree = duree
		self.running = True
		self.bus = smbus.SMBus(1)
		self.DISPLAY_RGB_ADDR = 0x62
		self.DISPLAY_TEXT_ADDR = 0x3e
		self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x00,0x00)
		self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x01,0x00)
		self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x02,0x00)
		self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x03,0xFE)
		self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x04,0x4C)
		self.bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x08,0xAA)
		time.sleep(0.25)
		self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,0x01)
		time.sleep(0.25)
		self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,0x0F)
		time.sleep(0.25)
		self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,0x38)
		time.sleep(0.25)

	# effacer l'ecran
	def clearEcran(self):
		self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,0x01)
		self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,0x0F)
		self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,0x38)

	def afficherMessage(self, texte):
		self.clearEcran()
		lg = len(texte)
		i = 0
		while i < lg and self.running == True:
			c = texte[i]
			self.bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x40,ord(c))
			i = i+1

	def defilerMessage(self, texte, duree):
		self.clearEcran()
		t = time.time()
		c = 15
		message = []
		while time.time() < t + duree and self.running == True:
			if c > 0:
				for i in range(c):
					message.append(" ")
				c = c-1
			j = len(message)
			if len(message)>0:
				j = j-1
				d = 0 
			else:
				d= d+1
			i=d
			while j < 16:
				message.append(texte[i])
				j = j+1
				i = i+1
			if c == 0 and i == len(texte):
				c = 15
			self.afficherMessage(message)
			time.sleep(0.5)
			message =[]
		self.clearEcran()

	#ecrire sur l'ecran
	def run(self):
		self.clearEcran()
		if len(self.message)<=15:
			self.afficherMessage(self.message)
			time.sleep(self.duree)
		else:
			self.defilerMessage(self.message,self.duree)
		self.clearEcran()

	def stop(self):
		self.running = False


#code non thread

bus = smbus.SMBus(1)
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e 

def initLCD():
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,0xFE)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,0x4C)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xAA)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x01)
	time.sleep(0.5)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x0F)
	time.sleep(0.5)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x38)
	time.sleep(0.5)


# effacer l'ecran
def clearEcran():
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x01)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x0F)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x38)

def afficherMessage(texte):
	lg = len(texte)
	i = 0
	while i < lg:
		c = texte[i]
		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
		i = i+1

def defilerMessage(texte,temps):
	t = time.time()
	c = 15
	message = []
	while time.time() < t + temps :
		if c > 0:
			for i in range(c):
				message.append(" ")
			c = c-1
		j = len(message)
		if len(message)>0:
			j = j-1
			d = 0 
		else:
			d= d+1
		i=d
		while j < 16:
			message.append(texte[i])
			j = j+1
			i = i+1
		if c == 0 and i == len(texte):
			c = 15
		afficherMessage(message)
		time.sleep(0.5)
		message =[]
		clearEcran()

#ecrire sur l'ecran
def ecrireMessage(texte,temps):
	initLCD()
	if len(texte)<=15:
		afficherMessage(texte)
		time.sleep(temps)
		clearEcran()
	else:
		defilerMessage(texte,temps)
		clearEcran()
