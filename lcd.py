import smbus
import time

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
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x0F)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x38)


# effacer l'ecran
def clearEcran():
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x01)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x0F)
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,0x38)

def afficherMessage(texte):
	clearEcran()
	lg = len(texte)
	i = 0
	while i < lg:
		c = texte[i]
		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
		i = i+1

def defilerMessage(texte):
	initLCD()
	t = time.clock()
	ta = t
	c = 15
	message = []
	print(t)
	while ta < t + 120:
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
		time.sleep(1)
		message =[]
		ta = ta + 1

#ecrire sur l'ecran
def ecrireMessage(texte):
	if len(texte)<=15:
		afficherMessage(texte)
		time.sleep(60)
	else:
		defilerMessage(texte)
	clearEcran()
