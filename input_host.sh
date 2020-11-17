#!/bin/bash

cd /root/SUB-SS-SSR-V2Ray

git pull

./input_host.py

git add .
git commit -m "Daily Update !"
git push

