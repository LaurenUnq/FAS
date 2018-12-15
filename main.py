#définir les imports..
import time
import frequenceCardiaque
import capteurTemperature
import buzzer
import led
import lcd
import message

while true :
  if time.strftime('%H')==8 :
    f = rappelFC()
    f.start()
    f.join()
  
	e = grovepi.digitalRead(button1)
	if e == 1:
  	self._return = True
		time.sleep(0.5)
    mesurerFC(2,20)
 
  mesurerH()

