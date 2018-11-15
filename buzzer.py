#ajouter les imports
from gpiozero import Buzzer
from time import sleep

#initialiser le buzzer
def initialiserBuzzer(pin)
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  buzzer = Buzzer(pin)

#Fonction qui acive le buzzer avec une intensité précise
#def buzzer(intensite):
def buzzer():
  while True:
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(1)
    GPIO.output(buzzer,GPIO.LOW)
    sleep(1)

def arretBuzzer():
  GPIO.output(buzzer,GPIO.LOW)
  GPIO.cleanup()
