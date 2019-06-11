@title 自动更新电费
chcp 65001
cd F:\Coding\Git_Space\electricityfee_display
f:
start python elec.py
timeout /t 8
git add .
git commit -m %date:~5,2%/%date:~8,2%AutoUpdate
git push origin master