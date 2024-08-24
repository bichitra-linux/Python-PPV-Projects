import sys
import os
import random
from selenium import webdriver
import requests
import time

splash = """

 Built for Educational and testing Purposes only
 Built By [Bichitra-Linux]

 support the Project on:
 https://github.com/bichitra-linux
"""

print(splash)
time.sleep(10)

def request(target_url, timeo, stay_time):
    try:
        driver=webdriver.Chrome()
        driver.set_page_load_timeout(timeo)
        driver.get(target_url)
        time.sleep(stay_time)
        driver.close()
    except:
        print("Error Occured")
        print("Please check your internet connection")
        print("Please check your target url")
        print("Please check your time out")
        print("Please check your stay time")

target=str(input("\033[1;33;40mEnter The Target Website URL :"))
timeout=int(input("\033[1;33;40mEnter The Time Out(In Seconds) :"))
stay=int(input("\033[1;33;40mEnter The Stay Time(In Seconds) :"))

while True:
	request(target,timeout,stay)
	print("\033[1;32;40mSleeping For 5 Seconds")
	time.sleep(5)