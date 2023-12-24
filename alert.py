import requests
import random
import datetime
import time
 
# Informations:
webhook_url = ""
pseudo_thm = ""

# Heures de notification
heures_verification = ["12:00", "15:00", "18:00", "20:00"]
 
phrases_motivation = ["Vas faire ton dailystreak sur tryhackme gros con !💻", "Rate pas ton dailystreak, sinon t'auras fais tout ça pour rien :( 💻"]
 
def motivation_roulette():
    message = random.choice(phrases_motivation)
    return message + "https://tryhackme.com/hacktivities?tab=search @everyone"
 
def envoyer_message_discord():
    payload = {
        "content": motivation_roulette()
    }
    requests.post(webhook_url, json=payload)
    print("Message envoyé!")
 
def verifier_date_presente():
    url = "https://tryhackme.com/api/user/activity-events?username=" + pseudo_thm
 
    response = requests.get(url)
 
    if response.status_code == 200:
        data = response.json()
 
        date_aujourdhui = datetime.date.today().strftime("%Y-%m-%d")
        
 
        # Vérifier si la date d'aujourd'hui figure dans les données JSON
        date_presente = False
        for item in data["data"]:
            date = f"{item['_id']['year']}-{item['_id']['month']}-{item['_id']['day']}"
            if date == date_aujourdhui:
                date_presente = True
                break
 
        if not date_presente:
            envoyer_message_discord()
    else:
        print("La requête n'a pas abouti. Code d'état :", response.status_code)
 
 
verifier_date_presente()
 
while True:
    heure_actuelle = datetime.datetime.now().strftime("%H:%M")
    if heure_actuelle in heures_verification:
        verifier_date_presente()
    time.sleep(50)
