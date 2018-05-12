import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

def get_fulian3(url):
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    infos = soup.select('.comment')
    for i in infos:
        if 'allstar' in str(i):
            names = i.select('h3 span.comment-info a')  #姓名
            scores = i.select('h3 span.comment-info span[class^="allstar"]')  #评分
            titles = i.select('p')                      #评论
            votes = i.select('h3 span.comment-vote span.votes')
            for name,title,score,vote in zip(names,titles,scores,votes):
                data = {
                    '姓名':name.text.strip(),
                    '评分':score['title'],
                    '点赞': vote.text.strip(),
                    '评论':title.text.strip()
                }
                song_id = songs.insert(data)
                print(data)
                print('-'*50)
        else:
            pass

urls = ['https://movie.douban.com/subject/24773958/comments?start=%d'%x*20 for x in range(0,31)]
client = MongoClient()
songs = client.My_db.fulian3

# for url in urls:
#     get_fulian3(url)
#     time.sleep(1)

for i in songs.find():
    print(i)
