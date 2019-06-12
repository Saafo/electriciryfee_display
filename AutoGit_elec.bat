@title 自动更新电费
chcp 65001
start python elec.py
timeout /t 5
git add .
git commit -m %date:~0,4%/%date:~5,2%/%date:~8,2%AutoUpdate
git push origin master