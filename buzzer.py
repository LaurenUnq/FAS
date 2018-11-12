#ajouter les imports
from gpiozero import Buzzer
from time import sleep

#s'il est connecté au port 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = Buzzer(17)

#Fonction qui acive le buzzer avec une intensité précise
def buzzer(intensite):)
  while True:
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(1)
    GPIO.output(buzzer,GPIO.LOW)
    sleep(1)

def arretBuzzer():
  GPIO.output(buzzer,GPIO.LOW)
  GPIO.cleanup()
