import datetime
import pywhatkit
import random
from plyer import notification
with open('links.txt','r') as file:
    content = file.read().split('\n')
hour = int(input("Enter the hour to set for alarm :"))
minute = int(input("Enter the minute to set for the alarm : "))
amorpm = input('Am or Pm : ')
link = input("Enter a youtube link to play music :")
content.append(link)
newcontent = random.choice(content)
if amorpm == 'Pm':
    hour = hour+12
while True:
    if datetime.datetime.now().hour == hour and datetime.datetime.now().minute == minute:
        notification.notify(title="Alarm Notfication",
                            message="Alarm time is live",
                            timeout=16)
        pywhatkit.playonyt(newcontent)
        break
