@title 自动更新电费
chcp 65001
start python elec.py
timeout /t 5
git add .
git commit -m %date:~8,2%/%date:~11,2%" Auto Update"
git push origin master