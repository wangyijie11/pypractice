import urllib.request
import urllib.error
import urllib.response
import urllib.parse
import urllib.robotparser
from http import cookiejar

# 声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib.request.build_opener(handler)

try:
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open("http://www.baidu.com")
    for item in cookie:
        print("NAME = " + item.name)
        print("Value = " + item.value)
except urllib.error.HTTPError as ex:
    print(ex)
except urllib.error.URLError as ex:
    print(ex)
else:
    print("ok")