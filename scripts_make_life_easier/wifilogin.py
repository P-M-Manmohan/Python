import subprocess
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

def login(conf,userID,passID,button):
    driver=webdriver.Firefox()
    url=conf['Student_user']['url']
    user=conf['Student_user']['id']
    pas=conf['Student_user']['password']
    driver.get(url)
    driver.find_element(by=By.ID,value=userID).send_keys(user)
    driver.find_element(by=By.ID,value=passID).send_keys(pas)
    driver.find_element(by=By.ID,value=button).click()

def getNetworkdata(cmd,filter1,filter2,part):
    wifi=subprocess.check_output(cmd)
    data=wifi.decode('utf-8')
    info=data.split(part)
    req_info=[]
    for i in info:
        if (filter1 in i) or (filter2 in i):
            req_info.append(i)
    return req_info


def wifilogin(conf):
    hotspot=conf['Wifi']['hotspot']
    wifi=conf['Wifi']['hostel']
    Networks=getNetworkdata(['netsh', 'wlan', 'show', 'networks'],wifi,hotspot,'SSID')
    #for i in AvailableNetworks:
    #    print(i)
    AvailableNetworks=" "
    for i in Networks:
        AvailableNetworks+=i
    if (hotspot not in AvailableNetworks) and (wifi in AvailableNetworks):
        os.system(f'netsh wlan connect name="{wifi}"')
        login(conf,"username","password","loginbutton")
        print("connected to student")
    elif hotspot in AvailableNetworks:
        os.system(f'netsh wlan connect name="{hotspot}"')
        print("connected to hotspot")
    else:
        print("nothing happened")
        exit()

if __name__=="__main__":
    time.sleep(15)
    with open('C:\\Users\\manu6\\OneDrive\\Documents\\scripts\\make_life_easier\\details.yml','r') as details:
        conf=yaml.load(details,Loader=yaml.FullLoader)
    wifilogin(conf)