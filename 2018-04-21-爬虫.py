import urllib.request
import re
import os
import urllib.error as error
import pandas as pd
url = 'https://www.zhipin.com/c101250100/h_101250100/?query=%E6%95%B0%E6%8D%AE&page=1'  #网址
request = urllib.request.Request(url)   #请求

#爬取结果
response = urllib.request.urlopen(request)
data = response.read()
#设置解码方式
data = data.decode('utf-8')
jobs = re.compile('<div class="job-title">(.+)</div>')  #岗位
salary = re.compile('<span class="red">(.+)</span>')    #薪资
regions = re.compile(r"""<p>(.+)  <em class="vline"></em>(.+)<em class="vline"></em>(.+)</p>
                                    </div>""")          #地区，经验，学历
# company = re.compile('<h3 class="name"><a href="/gongsi/ae4fb0fe63278c8c1nZ53dq6FQ~~.html" ka="search_list_company_31_custompage" target="_blank">(.+)</a></h3>')
jobslist = jobs.findall(data)       #岗位
salarylist = salary.findall(data)   #薪资
regionlist = regions.findall(data)   #地区，经验，学历
# companylist = company.findall(data) #公司
# print(companylist)
region =[]
experience = []
education = []
for i in regionlist:
    region.append(i[0])
    experience.append(i[1])
    education.append(i[2])
df = pd.DataFrame({'region':region,
                   'Salary':salarylist,
                   'Jobs':jobslist,
                   'experience':experience,
                   'education':education,
                   })
print(df)


