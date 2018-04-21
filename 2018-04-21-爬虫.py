import urllib.request
import re
import pandas as pd
url = 'https://www.zhipin.com/c101250100/h_101250100/?query=%E6%95%B0%E6%8D%AE&page=1&ka=page-1'
def request(url):
    data = urllib.request.urlopen(urllib.request.Request(url)).read()
    data = data.decode('utf-8')
    # # 公司名称
    # corporate_name_re = re.compile('target="_blank">(.+)</a></h3>')
    # corporate_name_list = corporate_name_re(data)
    #岗位
    jobsre = re.compile('<div class="job-title">(.+)</div>')
    jobslist = jobsre.findall(data)
    #薪资
    salaryre = re.compile('<span class="red">(.+)</span>')
    salarylist = salaryre.findall(data)
    #细节
    detailre = re.compile('<p>(.+)  <em class="vline"></em>(.+)<em class="vline"></em>(.+)</p>')
    detaillist = detailre.findall(data)
    zonelist = [] #地区
    experiencelist = [] #经验
    formallist = [] #学历
    for i in detaillist:
        zonelist.append(i[0])
        experiencelist.append(i[1])
        formallist.append(i[2])
    df = pd.DataFrame({'zone':zonelist,
                       'jobs':jobslist,
                       'salary':salarylist,
                       'experience':experiencelist,
                       'formal':formallist})
    return df
datalist = []
for i in range(10):
    url = 'https://www.zhipin.com/c101250100/h_101250100/?query=%E6%95%B0%E6%8D%AE&page='+str(i)+'&ka=page-1'
    datalist.append(request(url))
print()

