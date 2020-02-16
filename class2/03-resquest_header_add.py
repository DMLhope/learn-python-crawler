#-- coding:UTF-8 --
import  urllib.request
import urllib.parse
import string

def load_baidu():
    url = "http://www.baidu.com"
    #添加请求头的信息
    header = {
        #浏览器的版本
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
    }

    #创建请求对象
    #request = urllib.request.Request(url,headers=header)
    #动态的添加head信息
    request = urllib.request.Request(url)
    request.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36")
    #请求网络数据 （不能在urlopen这里添加请求头的信息，因为系统没有提供参数）
    response = urllib.request.urlopen(request)
    #响应头
    #print(response.headers)
    data = response.read().decode("utf-8")

    #获取到完整的url
    return_url = request.get_full_url()
    print(return_url)

    #获取请求头信息（所有的请求头的信息）
    #request_headers = request.headers
    #print(request_headers)
    #第二种方式打印headers信息
    #注意：这种方式打印时候要和字段名一一对应，而且首字母需要大写，其他字母小写
    request_headers = request.get_header("User-agent")
    print(request_headers)
    #with open("02header.html","w")as file:
    #   file.write(data)
load_baidu()