#-- coding:UTF-8 --
import  urllib.request
import urllib.parse
import string
import random

def proxy_user():
    proxy_list = [
        {"https":"https://58.253.153.221:9999"},
        {"https":"https://49.70.32.192:9999"},
        {"https":"https://61.145.48.137:9999"},
        {"http":"http://61.131.249.217:9006"},
        {"http":"http://58.253.152.37:9999"}
    ]

    for proxy in proxy_list:
        print(proxy)
        #利用遍历出来的ip创建handler
        proxy_handler = urllib.request.ProxyHandler(proxy)
        #创建opener
        opener = urllib.request.build_opener(proxy_handler)
        #考虑代理ip不可用的情况
        try:
            opener.open("https://www.baidu.com",timeout=2)
            print("ok")
        except Exception as error:
            print(error)

proxy_user()
