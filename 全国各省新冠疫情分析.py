import json
import requests
import time
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)#实时
data = json.loads(requests.get(url=url).json()['data'])
# 统计各省数据
num = data['areaTree'][0]['children']
# 治愈率
healRate_data = {}
for item in num:
    if item['name'] not in healRate_data:
        healRate_data.update({item['name']:0})
    healRate_data[item['name']] = item['total']['healRate']
# 存储数据
names = list(healRate_data.keys())          # 省份名称
num1 = list(healRate_data.values())
# 获取当前日期
n = time.strftime("%Y-%m-%d") + "-gz-4db.csv"
f = open(n, 'w', encoding='utf-8')
f.write('province,type,data\n')
i = 0
while i<len(names):
    f.write(names[i]+',治愈率(%),'+str(num1[i])+'\n')
    i = i + 1
else:
    f.close()
# Seaborn绘图
import matplotlib
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# 读取数据
n = time.strftime("%Y-%m-%d") + "-gz-4db.csv"
data = pd.read_csv(n)
# 设置窗口
fig, ax = plt.subplots(1,1)
print(data['province'])
# 设置风格、字体
sns.set_style("whitegrid",{'font.sans-serif':['simhei','Arial']})
# 绘柱状图
g = sns.barplot(x="province", y="data", hue="type", data=data, ax=ax,
            palette=sns.color_palette("hls", 8))
# 设置Axes标题
ax.set_title('全国各省疫情最新情况')
# 设置坐标轴文字
ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)
# 设置坐标轴刻度的字体
ax.tick_params(axis='x',labelsize=8)
ax.tick_params(axis='y',labelsize=8)
plt.show()    #看图时可以调上限和下限，观察更清楚
