import pandas as pd
df = pd.read_csv(r'D:\Me_py\data\DataAnalyst.csv',encoding='gb2312')

#定义一个取最低薪资和最高薪资的函数
def cut_word(word,method):
    match = word.find('-')
    length = len(word)
    if match != -1:
        bottomSalary = word[:match-1]
        topSalary = word[match+1:length-1]
    else:
        bottomSalary = word[:word.upper().find('K')]
        topSalary = bottomSalary
    if method == 'bottom':
        return bottomSalary
    else:
        return topSalary

df['bottomSalary'] = df.salary.apply(cut_word,method = 'bottom').astype('int')      #最低薪资
df['topSalary'] = df.salary.apply(cut_word,method = 'top').astype('int')            #最高薪资
df['avgSalary'] = (df.bottomSalary+df.topSalary)/2                                  #平均薪资

print(df.city.value_counts())       #计算每个地市招聘数量
print(df.groupby(['city','education']).count().avgSalary.unstack())     #计算每个地市每个学历需要的人数
#按公司名称计算招聘岗位数量和平均工资，并按照count排序
print(df.groupby('companyShortName').avgSalary.agg(['count','mean']).sort_values(by='count',ascending = False))

#计算出不同城市，招聘数据分析师需求前n的数据
def topN(df,n):
    counts = df.value_counts()
    return counts.sort_values(ascending=False)[:n]

print(df.groupby('city').companyShortName.apply(topN,2))    #城市和公司维度
print(df.groupby('city').positionName.apply(topN,2))    #城市和岗位维度
#str方法允许我们针对列中的元素，进行字符串相关的处理
word = df.positionLables.str[1:-1].str.replace(' ','')
