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
  compteur = 1
  e = grovepi.digitalRead(button1)
  if e == 1:
    self._return = True
    mesurerFC(2,20)
    compteur = 0
    time.sleep(0.5)
  else :
    time.sleep(900) #on attends 15 min avant de relancer un rappel
    f = rappelFC()
    f.start()
    f.join()
    compteur = compteur +1

  if compteur == 4 :
    compteur = 0
    m=message.MailProches("Ce message vous est envoyé car votre proche n'a pas confirmé sa prise d efréquence cardiaque")
    m.start()
    m.join()
 
  mesurerH()

