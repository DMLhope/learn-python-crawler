#-- coding:UTF-8 --
import  urllib.request
import urllib.parse
import string

def load_baidu():
    url = "http://www.baidu.com"

    #创建请求对象
    request = urllib.request.Request(url)
    #请求网络数据
    response = urllib.request.urlopen(request)
    #响应头
    print(response.headers)
    data = response.read().decode("utf-8")


    #获取请求头信息
    request_headers = request.headers
    print(request_headers)

    with open("02header.html","w")as file:
        file.write(data)
load_baidu()