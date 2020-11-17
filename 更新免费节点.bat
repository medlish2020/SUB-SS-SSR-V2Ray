@echo off
git pull

python input_host.py

git add .
git commit -m "Daily Update !"
git push

@pause