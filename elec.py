import requests
import json
import time

from pyecharts.charts import Line
from pyecharts import options as opts
url = 'http://wx.uestc.edu.cn/power/oneCartoon/list'
body = {'roomCode': '120612'}
response = requests.post(url,data = body)
raw_dic = json.loads(response.text)
sydl = raw_dic['data']['sydl']
syje = raw_dic['data']['syje']
time = time.strftime("%m-%d %H:%M:%S",time.localtime(int(raw_dic['timestamp']/1000)))

f1 = open('120612.txt','a+')
f1.writelines(time+'\t'+sydl+'\t'+syje+'\n')
f1.close()

f2 = open('120612.txt','r')
lines = f2.readlines()
f2.close()
if len(lines) > 15:
    lines = lines[-15:]
tm = []
je = []
for file_line in lines:
    tm.append(file_line[0:5])
    je.append(float(file_line[-6:]))
line = (
    Line(init_opts=opts.InitOpts(page_title='电费使用情况'))
    .add_xaxis(tm)
    .add_yaxis("612",je, is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title='电费使用情况'))
)
line.render('index.html')
