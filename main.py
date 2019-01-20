# -*- coding: utf-8 -*

import time
import frequenceCardiaque
import capteurTemperature
import buzzer
import led
import lcd
import bouton
import message

def main():
  d = 0
  lcd.ecrireMessage("Bonjour",3)
  lcd.clearEcran()
  t = capteurTemperature.MesurerH()
  day = int(time.strftime("%d")) - 1
  while True :
  #demande prise de frequence cardiaque
    if d == 0:
      if bouton.etatBt2() == 1:
        d = 1
        t = time.time()
        l = lcd.Lcd("Placer le capteur de frequence cardiaque et appuyer de nouveau sur le bouton 2",120)
        l.start()
        time.sleep(3)
    if d == 1:
      if bouton.etatBt2() == 1 and t + 120 > time.time():
        l.stop()
        l.join()
        prise(2,4)
        d = 0
      if t + 120 <= time.time():
        l.stop()
        l.join()
        d = 0

  #demande de frequence cardiaque quotidienne
    if day != time.strftime("%d") and int(time.strftime("%H")) >= 8:
      lcd.ecrireMessage("Bonjour",3)
      lcd.clearEcran()
      day = time.strftime("%d")
      freqQ = False
      while freqQ == False:
        ecran = lcd.Lcd("C est l heure de prendre votre frequence cardiaque! (appuyer sur le bouton 1)",60)
        buzz = buzzer.Buzzer(10,0) #on modifiera le 0 plus tard
        ledr = led.Led(60,0.5)
        bt1 = bouton.Button1(60)
        ecran.start()
        bt1.start()
        buzz.start()
        ledr.start()
        ret = bt1.join()
        if ret == True:
          ecran.stop()
          ledr.stop()
          buzz.stop()
          prise(2,4)
          freqQ = True    
        ecran.join()
        ledr.join()
        buzz.join()
  t.join()



def prise(e1, e2):
  btm = frequenceCardiaque.demanderMesure()
  essai = 1
  while frequenceCardiaque.analyseFreq(btm) == False:
    if essai == e1:
      message.envoyerMailProches("Un soucis a été detecté avec la fréquence cardiaque de votre proche. Dans 5 minutes, les secours seront prévenus.")
    if essai == e2:
      message.envoyerMailSecours("Alerte! Un soucis avec la fréquence cardiaque d'une personne à été detecté. Des secours sont nécessaires")
    frequenceCardiaque.sauvegarderFC(btm)
    essai = essai + 1
    lcd.ecrireMessage("Nouvel essai", 5)
    btm = frequenceCardiaque.demanderMesure()
  frequenceCardiaque.sauvegarderFC(btm)

main()




