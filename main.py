#definir les imports..
import time
import frequenceCardiaque
import capteurTemperature
import buzzer
import led
import lcd
import message

def main():
	print("bonjour0")
    while true :
    print("bonjour")
   # if time.strftime('%H')==8 :
    f = frequenceCardiaque.RappelFC()
    f.start()
    f.join()
    compteur = 1
    e = bouton.Button1(60)
    e.start()
    res = e.join()
    if res == 1:
      frequenceCardiaque.mesurerFC(2,20)
      compteur = 0
      time.sleep(0.5)
    else :
      time.sleep(900) #on attends 15 min avant de relancer un rappel
      f = frequenceCardiaque.RappelFC()
      f.start()
      f.join()
      compteur = compteur +1

    if compteur == 4 :
      compteur = 0
      m=message.MailProches("Ce message vous est envoye car votre proche n a pas confirme sa prise de frequence cardiaque")
      m.start()
      m.join()

    capteurTemperature.mesurerH()

main()
