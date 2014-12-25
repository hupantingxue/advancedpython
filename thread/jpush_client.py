#/usr/bin/env python
#-*- coding:utf-8 -*-

from threading import Thread
import requests
import json

appkey = '5a0fe3d99d1d89a25d73b0a4'
master_secret = '8cc1233226324ee29af559d2'

url = 'https://api.jpush.cn/v3/push'
payload = {"platform":["android"],"audience":"all", "options":{"time_to_live":"0", "sendno":0}, "notification":{"alert":"Hi,JPush!"}}
headers = {}
headers['content-type'] = 'application/json;charset:utf-8'

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def mypush(sendno):
    payload["options"]["sendno"] = sendno
    #print("payload: %r" %(payload))
    r = requests.post(url, data=json.dumps(payload), headers=headers, auth=(appkey, master_secret))
    print "sendno[%r] response[%r]" %(sendno, r.text)

def main():
    sendno_list = [ii+1 for ii in range(100)]
    threads = []
    for ii in range(len(sendno_list)):
        t = Thread(
                target=ThreadFunc(mypush, (sendno_list[ii], ), mypush.__name__))
        threads.append(t)
        
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if "__main__" == __name__:
    main()
