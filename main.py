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
  
  res=["45.167.253.129:999","222.218.122.22:9797","106.14.187.182:21673","49.233.173.151:9080","1.180.156.226:65001","98.12.195.129:443","89.205.35.229:8080","103.163.134.4:8181","103.123.246.54:8080","190.120.248.113:999","98.12.195.129:443","89.205.35.229:8080"]
  
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


