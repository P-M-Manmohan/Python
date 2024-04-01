import subprocess
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

def login(conf,userID,passID,button):#extra login required for college wifi login 
    driver=webdriver.Firefox()
    #get login details and url to enter details
    url=conf['Student_user']['url']
    user=conf['Student_user']['id']
    pas=conf['Student_user']['password']
    driver.get(url)#open webpage
    driver.find_element(by=By.ID,value=userID).send_keys(user)#enter userid
    driver.find_element(by=By.ID,value=passID).send_keys(pas)#enter password
    driver.find_element(by=By.ID,value=button).click()#click login

def getNetworkdata(cmd,filter1,filter2,part):
    wifi=subprocess.check_output(cmd)#get all available networks
    data=wifi.decode('utf-8')
    info=data.split(part)#make list out of each network
    req_info=[]
    for i in info:
        if (filter1 in i) or (filter2 in i):
            req_info.append(i)#new list with only two networks that matter
    return req_info


def wifilogin(conf):
    hotspot=conf['Wifi']['hotspot']#get hotspot name
    wifi=conf['Wifi']['hostel']#get college wifi name
    Networks=getNetworkdata(['netsh', 'wlan', 'show', 'networks'],wifi,hotspot,'SSID')#get hotspot and wifi is available
    #for i in AvailableNetworks:
    #    print(i)
    AvailableNetworks=" "
    for i in Networks:
        AvailableNetworks+=i #create single strign to make it easier to search
    if (hotspot not in AvailableNetworks) and (wifi in AvailableNetworks):#if hotspot not available but wifi is
        os.system(f'netsh wlan connect name="{wifi}"')#run command to connect to wifi
        login(conf,"username","password","loginbutton")
        print("connected to student")
    elif hotspot in AvailableNetworks:
        os.system(f'netsh wlan connect name="{hotspot}"')# connec to hotspot
        print("connected to hotspot")
    else:
        print("nothing happened")#if neither are availabel exit
        exit()

if __name__=="__main__":
    time.sleep(15) #wait 15 seconds after boot
    with open('C:\\Users\\manu6\\OneDrive\\Documents\\scripts\\make_life_easier\\details.yml','r') as details:
        conf=yaml.load(details,Loader=yaml.FullLoader)#open yaml file with login info and wifi names
    wifilogin(conf)
