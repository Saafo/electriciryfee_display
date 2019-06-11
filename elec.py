import requests
import json
import time
# import string
from pyecharts.charts import Line
from pyecharts import options as opts
url = 'http://wx.uestc.edu.cn/oneCartoon/list'
#url2 = 'http://wx.uestc.edu.cn/oneCartoon/index.html?code=02c5eb30b86a5bff65c78009db777cb8&account=2018091619017'
body = {'roomCode': '120612'}
# headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Connection': 'keep-alive',
# 'Content-Length': '15',
# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# #'Cookie': 'UM_distinctid=16a12044602106-0dc2375d00a92-e323069-144000-16a12044603482; __utma=108824541.36559883.1558533169.1558533169.1558533169.1; __utmz=108824541.1558533169.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
# 'Host': 'wx.uestc.edu.cn',
# 'Origin': 'http://wx.uestc.edu.cn',
# 'Referer': 'http://wx.uestc.edu.cn/oneCartoon/index.html?code=02c5eb30b86a5bff65c78009db777cb8&account=2018091619017',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
# 'X-Requested-With': 'XMLHttpRequest'}
response = requests.post(url,data = body)
raw_dic = json.loads(response.text)
# print(response.text)
sydl = raw_dic['data']['sydl']
syje = raw_dic['data']['syje']
time = time.strftime("%m-%d %H:%M:%S",time.localtime(int(raw_dic['timestamp']/1000)))
# print(time)
f1 = open('120612.txt','a+')
f1.writelines(time+'\t'+sydl+'\t'+syje+'\n')
f1.close()

f2 = open('120612.txt','r')
lines = f2.readlines()
f2.close()
if len(lines) > 15:
    lines = lines[-16:]
tm = []
je = []
for file_line in lines:
    tm.append(file_line[0:11])
    je.append(float(file_line[-6:]))
line = (
    Line()
    .add_xaxis(tm)
    .add_yaxis("612",je, is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title='612电费使用情况'))
)
# line = Line("612电费使用情况")
# line.add("612",tm,je, is_smooth = True)
line.render('index.html')
