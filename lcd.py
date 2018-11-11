#ajouter les imports nécessaires
#sudo pip install RPLCD
from RPLCD import CharLCD
import time

# effacer l'ecran
def clearEcran():
  lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
  lcd.write_string(u'Espace RaspberryFrancais')
  time.sleep(5)
  lcd.clear()

#ecrire sur l'ecran
def ecrireMessage(texte):
  lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
  lcd.write_string(texte)
