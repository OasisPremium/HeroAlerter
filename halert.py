#!/usr/bin/env python3
import requests,sys,json,time
from playsound import playsound
from datetime import datetime
import os

WD = []
GW = []
BA = []     

def main():
    try:    
        os.system('cls||clear')
        cwd = os.path.dirname(os.path.realpath(__file__))
        print("#####################################################################")
        print("################# HeroMiners Crypto Worker Alerter###################")
        print("#####################################################################")
        print()
        
        CRYPTO = input("Please enter the full name of your CRYPTO. (e.g: aeon,haven,monero): ")
        
        URL = "https://" + CRYPTO + ".herominers.com/api/stats_address?address="
        ADDRESS = input("Please enter your crypto address:")
        URL = URL + ADDRESS + "&longpoll=false"
        intervalx = int(input("Please enter how many seconds do you want between each scans? (Recommended is 60 (1minute) or 600 (10minutes)): "))
        if(intervalx <= 10):
            intervalx = 10
        brange = int(input("How many times should the alert ring?:"))
        r = requests.get(url = URL)
        data = r.json()
        data = data['workers']
        for hr in data:
                if(WD.count(hr['name']) <= 0):
                    WD.append(hr['name'])
                    x = input("Do you want to add " + hr['name'] + " on the alert list ? Y or N: ")
                    if(x[0].upper() == "Y"):
                        BA.append(hr['name'])
        while 1:
            time.sleep(intervalx)
            r = requests.get(url = URL)
            data = r.json()
            data = data['workers']
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            now = datetime.now()
            now = now.strftime("%H:%M:%S")
            print("Time of scan: " + now)
            print("##################################################")
            for hr in data:
                if(WD.count(hr['name']) <= 0):
                    WD.append(hr['name'])
                    x = input("Do you want to add " + hr['name'] + " on the alert list ? Y or N: ")
                    if(x[0].upper() == "Y"):
                        BA.append(hr['name'])

                if(hr['hashrate'] == 0):
                    print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                    if(BA.count(hr['name']) >= 1):
                        for i in range(brange):
                            #print('\a')
                            #print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                            audio_file = cwd + '\\audio.wav'
                            playsound(audio_file)
                            
                        

                if(hr['hashrate'] >= 1):
                    print(hr['name'] + " IS OK.")
                    if(GW.count(hr['name']) <= 1):
                        GW.append(hr['name'])
                        

                
            print("##################################################")
            print()     
            #print(WD)
    except Exception as e: print(e)
        
        
if __name__ == "__main__":
    main()