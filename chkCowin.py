import requests
import json
import datetime
import time
import sys
import os
import random
import pywhatkit as kit

ping_body=""
#Can change here the value in range from 6 to any number, depending on time.sleep() at last line in below code and for how long want to check the slots
for turn in range(1,6):
    ping_body=""
    for i in range(int(str(datetime.datetime.now().date())[-1]),int(str(datetime.datetime.now().date())[-1])+7):
      #below range's start and end value is for pincode, I wanted to check availability for all pincodes between 452022 to 462030
        for pin in range(462022,462030):
            max_try,cde=(5,1)
            while max_try != 0 and cde != 200 :
                resp = requests.get\
                (f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={str(pin)}&date={i:0=2d}-05-2021')
                if resp.status_code == 200 :
                    op=resp.json()
                    if len(op['centers']) > 0 :
                        tName=op['centers'][0]
                        tVac=tName['sessions']
                        isAvail=tVac[0]['available_capacity']
                        if isAvail > 0:
                            ping_body+='{}~{}~{}~{} \n'.format(tVac[0]['date'],tName['pincode'],tName['name'],tVac[0]['available_capacity'])                       
                else:
                    sys.stdout.flush()
                    #time.sleep(random.randint(0,3))
                max_try=max_try-1
                cde=resp.status_code
    #Mention here mobile number with +91-MobNo, where want to receive the notification
    #make sure to link web.whatsapp.com with other account on the device running this code
    kit.sendwhatmsg("+911234567890",ping_body,datetime.datetime.now().hour,datetime.datetime.now().minute+1)
    time.sleep(600)
