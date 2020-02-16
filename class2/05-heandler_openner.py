#-- coding:UTF-8 --
import  urllib.request
import urllib.parse
import string
import random

#handler 处理程序

def handler_openner():
#系统的urlopen并没有添加代理的功能所以需要自定义该功能
#安全套接层 ssl  第三方的ca数字证书
#http用80端口https用443端口
#urlopen为何可以请求数据  handler处理器
#使用自己的opener请求数据
#urllib.request.urlopen()
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"
    #创建自己的处理器
    handler = urllib.request.HTTPHandler()
    #创建自己的opener
    opener = urllib.request.build_opener(handler)
    #用自己创建的opener来调用open请求
    response = opener.open(url)
    data = response.read().decode("utf-8")
    print(response)
    print(data)

handler_openner()

