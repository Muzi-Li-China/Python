import time                     #时间模块
import requests                 #请求网页
from bs4 import BeautifulSoup   #解析网页
from pymongo import MongoClient #MongoDB模块

def get_kugou(url):
    reurl = requests.get(url,headers=headers)           #请求网页
    soup = BeautifulSoup(reurl.text,'lxml')             #解析网页
    ranks = soup.select('.pc_temp_num')                 #排名list
    names = soup.select('.pc_temp_songname')            #歌手+歌曲list
    times = soup.select('.pc_temp_time')                #歌曲时间list
    for rank,name,time in zip(ranks,names,times):       #循环list
        try:
            data = {                                        #将信息存放在一个字典中
                "rank":rank.text.strip(),                   #排名
                "singer":name.text.split('-')[0].strip(),   #歌手
                "name": name.text.split('-')[1].strip(),    #歌名
                "time":time.text.strip()                    #歌曲时间
            }
        except:
            continue
        song = songs.insert(data)  #将data插入到数据库中
        print(song)
        print('-'*20)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}   #模拟浏览器

urls = ['http://www.kugou.com/yy/rank/home/%d-8888.html'%x for x in range(1,24)]   #网址

MC = MongoClient()   #连接MongoDB
songs = MC.My_db.kugou  #新建一个My_db的数据库，并在数据库中新建一个kugou集

for i in urls:
    get_kugou(i)    #循环调用函数
    time.sleep(1)   #每调用一次，休息1秒
