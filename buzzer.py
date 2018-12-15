import sys
from threading import Thread
import time
from grovepi import *


class Buzzer(Thread):

  def __init__(self, tempsB, intensite):
    Thread.__init__(self)   
    self.buzzer = 5
    self.tempsB = tempsB
    self.intensite = intensite
    self.running =  True
    pinMode(self.buzzer,"OUTPUT")
    time.sleep(1)

  def run(self):
    t=time.time()
    while t + self.tempsB > time.time() and self.running == True:
      try:
        analogWrite(self.buzzer,self.intensite)
        time.sleep(1)
        analogWrite(self.buzzer,0)
        time.sleep(1)
      except KeyboardInterrupt:
        analogWrite(self.buzzer,0)
        break
      except IOError:
        print ("Error")

  def stop(self):
      self.running == False
