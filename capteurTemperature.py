#Import buzzer
#Import lcd
#Import internet
#import led
#Import bouton
#Import alerter
Import time
import grovepi
import math

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND

def  initialiserH(pin):
  sensor = pin # The Sensor goes on digital port "pin".
  # temp_humidity_sensor_type
  # Grove Base Kit comes with the blue sensor.
  blue = 0    # The Blue colored sensor.      #N'est ce pas l'inverse pour le 0 ou 1 ??
  white = 1   # The White colored sensor.

def rappelH():
  #ecrireMessage("Rappel : Hydratez-vous !")      #utilisation de la fonction depuis lcd
  #buzzer()     #utilisation de la fonction depuis buzzer
  #clignoterLED()      #utilisation de la fonction depuis led
  #time.sleep(10)
  #clearEcran()      #utilisation de la fonction depuis lcd
  #arretBuzzer()     #utilisation de la fonction depuis buzzer
  
#def mesurerH(temp):
def mesurerH():
  while True:
    try:
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor,blue)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
            #ecrireMessage("temp = %.02f C humidity =%.02f%%"%(temp, humidity))     #/// Via lcd

    except IOError:
        print ("Error")

def arretH

def alerteProcheH():
  #msg="ALERTE ! Il semblerait que Mr ou MMe X rencontre des difficultés ..."
  #if (temp >= 25):
    #alerterProche(msg)
  
#def alerterSecoursH():

