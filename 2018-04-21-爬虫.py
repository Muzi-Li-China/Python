import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
#爬取智联招聘信息
newsurl = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%95%BF%E6%B2%99&kw=%E6%95%B0%E6%8D%AE&isadv=0&sg=5fc28c0630444389bd5b8682cacc853c&p=1'
def wangzhua(url):
#请求
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
#返回
    response = urllib.request.urlopen(req)
    html = response.read()
    bsObj = BeautifulSoup(html, "html.parser")
#标题
    zwmc = [i.text for i in bsObj.select('.zwmc a')]
    gsmc = [x for x in [i.text for i in bsObj.select('.gsmc a')] if len(x) >0]
    zwyx = [i.text for i in bsObj.select('.zwyx')][1:]
    gzdd = [i.text for i in bsObj.select('.gzdd')][1:]
    newlist_deatil_two = [i.text for i in bsObj.select('.newlist_deatil_two')]
    xueli = []
    for i in newlist_deatil_two:
        if i.find('职位月薪')-i.find('学历')+3 >0:
            xueli.append(i[i.find('学历')+3:i.find('职位月薪')])
        else:
            xueli.append("不限")
    df = pd.DataFrame({'职位名称':zwmc,
                       '公司名称':gsmc,
                       '工作地点':gzdd,
                       '学历要求':xueli,
                       '职位月薪':zwyx})
    return df
df = []
for i in range(10):
    newsurl = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%95%BF%E6%B2%99&kw=%E6%95%B0%E6%8D%AE&isadv=0&sg=5fc28c0630444389bd5b8682cacc853c&p='+str(i)
    df.append(wangzhua(newsurl))
pd.concat(df).to_excel('2018-04-21.xlsx',index=False)

