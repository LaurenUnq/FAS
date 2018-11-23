import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MDP = "Comp3Glf"
EXPEDITEUR = "compagnie3G@gmail.com"

def envoyerMailProches(text):
	DESTINATAIRE = "fsmague@gmail.com"

	message = MIMEMultipart()
	message['From'] = "Compagnie3G"
	message['To'] = DESTINATAIRE
	message['Subject'] = "Alerte avec votre proche"

	corp = text

	message.attach(MIMEText(corp.encode('utf-8'),'plain','utf-8'))

	serveur = smtplib.SMTP('smtp.gmail.com',587)
	serveur.starttls()
	serveur.login(EXPEDITEUR,MDP)
	mail = message.as_string().encode('utf-8')

	serveur.sendmail(EXPEDITEUR,DESTINATAIRE,mail)

	serveur.quit()


def envoyerMailSecours(text):
	DESTINATAIRE = "fsmague@gmail.com"

	message = MIMEMultipart()
	message['From'] = "Compagnie3G"
	message['To'] = DESTINATAIRE
	message['Subject'] = "Alerte demande de secours"

	corp = text

	message.attach(MIMEText(corp.encode('utf-8'),'plain','utf-8'))

	serveur = smtplib.SMTP('smtp.gmail.com',587)
	serveur.starttls()
	serveur.login(EXPEDITEUR,MDP)
	mail = message.as_string().encode('utf-8')

	serveur.sendmail(EXPEDITEUR,DESTINATAIRE,mail)

	serveur.quit()

