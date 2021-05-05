import requests
import json
import time
import sys
import random
import pywhatkit as kit
import datetime
import subprocess
import pandas as pd

# replace all path '/home/ubuntu/BigData/Projects/COWIN/avail.csv' with your value
subprocess.check_output("echo -n '' > /home/ubuntu/BigData/Projects/COWIN/avail.csv 2>&1",shell=True)

#for intrval in range(1,200):  -->Enable it when want to check periodically, and change the indentation accordingly
for i in range(int(str(datetime.datetime.now().date())[-1]),int(str(datetime.datetime.now().date())[-1])+1):
    #below range's start and end value is for pincode list, for example if looking for availability pincodes between 462022 to 462030
    for pin in range(462022,462030):
        max_try,cde=(5,1)
        while max_try != 0 and cde != 200 :
            resp = requests.get\
            (f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={str(pin)}&date={i:0=2d}-05-2021')
            if resp.status_code == 200 :
                op=resp.json()
                if len(op['centers']) > 0 :
                    df=pd.json_normalize(op['centers'],'sessions',['name','pincode'])
                    df_avail=df[(df.available_capacity > 0)]
                    df_avail[['date','pincode','name','available_capacity']].sort_values('date').to_csv('/home/ubuntu/BigData/Projects/COWIN/avail.csv',mode='a',header=False, index=False, sep='~')
            else:
                sys.stdout.flush()
                time.sleep(random.randint(0,5))
            max_try=max_try-1
            cde=resp.status_code
    ping_body=subprocess.check_output('cat /home/ubuntu/BigData/Projects/COWIN/avail.csv', shell=True)
    #Mention here mobile number with +91-MobNo, where want to receive the notification
    #make sure to link web.whatsapp.com with other account on the device running this code
    kit.sendwhatmsg("+91XXXXxxxxxx",ping_body.decode("utf-8"),datetime.datetime.now().hour,datetime.datetime.now().minute+1,30)
#time.sleep(600) --> By enabling line number 13 and this line, it will check the availability after evey 10 minutes

#Or Can schedule above script using your favourite scheduler/airflow/crontab  without enabling line 13 & 36, with your schedule
