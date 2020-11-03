#!/bin/bash

git pull

./update_ip.py

git add .
git commit -m "Daily Update !"
git push
