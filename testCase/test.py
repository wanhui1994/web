# coding=utf-8
import requests
i=1
while int(i) < 10:
  url="http://ifaxuan.cn/KaiXinPuFa/index.php/Home/Problem/addXiTi/problemcontent/%D9%89%20%C2%AB%D8%A6%D8%A7%D8%B3%D8%A7%D8%B3%D9%89%D9%8A%20%D9%82%D8%A7%D9%86%DB%87%D9%86%D9%89%C2%BB%20(%20%20%20%20)-%D9%8A%D9%89%D9%84%D9%89%D9%89%D8%AF%D8%A7%20%D9%85%D8%A7%D9%82%DB%87%D9%84%D9%84%D8%A7%D9%86%D8%BA%D8%A7%D9%86./problemclass/wanhui/answercontent/[%22%D8%AA%DB%87%D8%B1%D8%A7%D9%84%D8%BA%DB%87%D8%B3%D9%89%D8%BA%D8%A7%20%DA%86%DB%90%D9%82%D9%89%D9%84%D9%85%22,%22%D8%AC%D9%89%D8%B3%DB%95%D9%86%D9%84%D9%89%D9%83%D9%89%22,%22%D8%AC%D8%B3%20%D9%84%D9%89%22,%22%D8%AC%D9%89%D8%BA%D8%A7%20%DA%86%DB%90%D9%82%D9%89%D9%84%D9%89%22]/rightkey/D/analysis/%E6%AD%A3%E7%A1%AE%E7%AD%94%E6%A1%88%EF%BC%9AD/lv/1/operator/admin/ismust/1"
  requests.get(url)
  i+=1


# m=a[a.rfind("values('")+7:a.rfind(",'56")]
# print(m)




