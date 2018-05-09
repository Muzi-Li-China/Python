import re                           #正则模块
import time                         #时间模块
import requests                     #请求网页
from bs4 import BeautifulSoup       #解析网页
from pymongo import MongoClient     #MongoDB数据库
from multiprocessing import Pool    #多进程

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    }   #请求头

client = MongoClient()  # 连接MongoDB
song = client.My_db.zhaopin  # 在数据库中新建类

def get_zhaopin(url):
    '''爬取BOSS直聘网，数据岗位'''

    res = requests.get(url, headers=headers)            #请求网页
    soup = BeautifulSoup(res.text, 'lxml')              #解析网页

    #使用CSS选择器，获取数据
    titles = soup.select('.job-title')                  #工作岗位 list
    companys = soup.select('.company-text > h3 > a')    #公司名称 list
    reds = soup.select('.red')                          #工资月薪 list
    infos = soup.select('.info-primary > p')            #获取工作地点，要求经验和学历 list
    company_infos = soup.select('.company-text > p')    #获取公司类型，投资，人数 list

    #循环获取的list
    for title, company, red, info, company_info in zip(titles, companys, reds, infos, company_infos):
        #使用正则获取info和company里面的信息
        re_info = re.findall('<p>(.*)  <em class="vline"></em>(.*)<em class="vline"></em>(.*)</p>', str(info))
        re_company = re.findall('<p>(.*)<em class="vline"></em>(.*)<em class="vline"></em>(.*)</p>', str(company_info))
        #将数据存放在data中
        try:
            data = {
                '工作岗位': title.text.strip(),
                '公司名称': company.text.strip(),
                '工资': red.text.strip(),
                '工作地点': re_info[0][0],
                '工作经历': re_info[0][1],
                '学历要求': re_info[0][2],
                '公司类型': re_company[0][0],
                '公司投资': re_company[0][1],
                '公司人数': re_company[0][2]
            }
        except:
            continue
        song_id = song.insert(data)     #将data添加到数据库中
        print(song_id)
        print('-'*50)

if __name__ == '__main__':

    urls = ['https://www.zhipin.com/c100010000/h_100010000/?query=%E6%95%B0%E6%8D%AE&page={}'.format(str(i)) for i in range(1,51)]  #网页

    pool = Pool(processes=4)    #设置4线程
    pool.map(get_zhaopin,urls)
