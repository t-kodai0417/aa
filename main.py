#+++++++++++"IMPORT"++++++++++++++++++
import requests
import tkinter
import os
import urllib.request
import random

#++++++Try+++++++++++
try:
  import dehook as dk
  import pcolor
except:
  print("IMPORT ERROR")
  
#++++++++++++++++++++

import threading
import random
import time

#++++++++++++++++++++++++++++++++++++

def dos():
  r = urllib.request.urlopen('https://api').read().decode('utf-8')
  f = open("bd.txt", 'a', encoding='utf-8', newline='\n')
  f.write(r)
  f.close()
  
  for proxy in res: proxies.append("https://" + proxy)
    res=requests.get(r"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000").text.splitlines()
    print(res)
  
  t=random.choice(res)
  print(f"t={t}")
  proxies = {
    'https': f"https://{t}"
  }
  try:
    a=requests.get("m.kuku.lu",proxies=proxies,timeout=(3.0, 7.5))
    status=a.status_code
  except:
    print("")
  
dos()


