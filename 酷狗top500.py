import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
songs = client.kugou_db.songs
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
def get_info(url):
    '''获取酷狗音乐TOP500信息'''
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    ranks = soup.select('.pc_temp_num') #排名
    titles = soup.select('.pc_temp_songname') #歌手和歌曲
    times = soup.select('.pc_temp_time') #歌曲时长
    for rank,title,time in zip(ranks,titles,times):
        try:
            data= {
                'rank':rank.text.strip(),
                'singer':title.text.split('-')[0].strip(),
                'name':title.text.split('-')[1].strip(),
                'time':time.text.strip()
            }
            print(data)
            song_id = songs.insert(data)
            print(song_id)
            print('-'*30)
        except:
            continue

if __name__ == '__main__':
    url = ['http://www.kugou.com/yy/rank/home/%d-8888.html'%x for x in range(1,23)]
    for i in url:
        get_info(i)
        time.sleep(1)
