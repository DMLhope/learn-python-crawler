import urllib.request
import urllib.parse
import string
def get_mothod_params():
   
    url = "http://www.baidu.com/s?wd="
    #拼接字符串（汉字）
    name  =  "火焰"
    final_url = url+name
    
    print(final_url)

    
    #代码虽然发送了请求但是网址里面包含中文 ascii不包含汉字
    #UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
    #python是解释性语言；解析器只支持 ascii 0-127
    #不支持中文
    #url需要转译
    #将包含汉字的网址进行转译
    encode_new = urllib.parse.quote(final_url,safe=string.printable)
    print(encode_new)
    
    #使用代码发送网络请求
    test = "https://blog.csdn.net/a506681571/article/details/78284589"
    response = urllib.request.urlopen(test)
    
    print(response)
    
    data = response.read().decode("utf-8")
    print(data)

    with open("baidu-fire.html","w",encoding="utf-8")as file:
        file.write(data)


get_mothod_params()