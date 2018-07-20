from http import cookiejar
from urllib import request

cookie=cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener=request.build_opener(handler)
url="http://qdtest.faxuan.net/"
resp=opener.open(url)
for item in cookie:
    print(type(item))



