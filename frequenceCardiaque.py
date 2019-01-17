import sys
from threading import Thread
import RPi.GPIO as GPIO
from grovepi import *
import time
import lcd

SENSOR = 2

def analyseFreq(btm):
	if btm > 40 and btm < 220:
		return True
	return False


def demanderMesure():
	l2 = lcd.Lcd("Patientez",30)
	l2.start()
	res = mesurerFC(30)
	l2.stop()
	l2.join()
	message = str(res) + " btm/min"
	lcd.ecrireMessage(message,30)
	return res

#Le capteur renvoie0 quand il sent pas de batement, et 1 quand il y en a
def mesurerFC(timeInt): #pin est le pin sur lequel est le capteur, time et le temps pendant lequel on prend la frequence (ex:20sec)
	pinMode(SENSOR,"INPUT") #plus le temps time est grand plus ce sera precis
	current = time.time()
	prec = 0
	count = 0
	sec = current
	while sec < current + timeInt  :
		lec = digitalRead(SENSOR)
		if not prec and lec :
			count += 1
		prec = lec

		sec = time.time()

	btm = count * (60/timeInt)
	print(btm)
	return btm

def sauvegarderFC(btm): #Mettre dans la bd
	data = {"entry.1030626618":btm}
	r = requests.post("https://docs.google.com/forms/d/1IeL0W_QLm2Ql0AfngbanobwUrZ-fFM1BQp2d9MdAR3Y/formResponse?", data = data)
