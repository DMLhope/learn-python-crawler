#-- coding:UTF-8 --
import  urllib.request

def create_proxy_handler():
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"

    #添加代理
    proxy = {
        # 免费代理写法
        "http":"http://58.253.155.110:0000"
        #付费代理的写法
        #"http":"账号":"123@..."
    }
    #代理的处理器
    proxy_hander = urllib.request.ProxyHandler(proxy)

    #创建自己的opener(用处理器创建opener)
    opener = urllib.request.build_opener(proxy_hander)

    #拿着代理ip去发送
    data = opener.open(url).read()
    print(data)

create_proxy_handler()