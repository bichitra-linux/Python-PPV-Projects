import os
import time


splash = """

 Built for Educational and testing Purposes only
 Built By [Bichitra-Linux]

 support the Project on:
 https://github.com/bichitra-linux
"""
print(splash)
time.sleep(3)
os.system("cd core && bash setup.sh")
time.sleep(1)
os.system("clear")
print(splash)
op=str(input("Did you already initialize it(Y/n) :"))
if((op=="N") or (op=="n")):
 os.system("cd core && bash init.sh")
else:
 pass
os.system("cd core && bash vpn.sh")