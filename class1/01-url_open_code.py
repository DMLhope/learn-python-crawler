import urllib.request

def load_data():
    url = "http://www.baidu.com/"
    #get的请求
    #response:http响应的对象
    response = urllib.request.urlopen(url)
    print(response)
    #读取内容 bytes类型
    data = response.read()
    print(data)
    #将文件获取的内容转换成字符串
    str_data = data.decode("utf-8")
    print(str_data)
    #将数据写入文件
    with open("baidu.html","w",encoding="utf-8")as file:
        file.write(str_data)
    #将字符串类型转换成bytes
    str_name = "baidu"
    bytes_name = str_name.encode("utf-8")
    print(bytes_name)

    #python爬取的类型：str bytes
    #如果爬取回来是bytes类型，但是写入的时候需要字符串 decode（“utf-8”）
    #果爬取回来是str类型，但是写入的时候需要字符串 encode（“utf-8”）
load_data()