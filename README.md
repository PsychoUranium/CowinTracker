# CowinTracker
For range of pincodes, get the prompt notification on whatsapp for available COVID vaccination slots 

# OS
Linux

# Prerequisites
Install Anaconda on your machine as most of the required libraries comes with it /or/ install the required packages using pip, imported in code

Example:
install pywhatkit using command:
pip install pywhatkit

# link web.whatsapp.com 
go to https://web.whatsapp.com/ and link this by scanning QR code 
Please don't use the whatsapp account where looking to receive the notification, using same account won't prompt notification

# Notification screenshot:
![image](https://user-images.githubusercontent.com/83650379/117111245-ee593e80-ada4-11eb-925d-676481c39641.png)
![image](https://user-images.githubusercontent.com/83650379/117111157-d4b7f700-ada4-11eb-83db-b4a6c65b5c54.png)

# To check it for every 10 min interval 
run command on unix terminal: bash interval_10.sh

and 

open new window of terminal using Ctrl+Alt+T, and run command:

cd /path_to_your_dir_where_fil_"interval_10.sh"_is_present/
cat ./temp.txt
tail -f !$
