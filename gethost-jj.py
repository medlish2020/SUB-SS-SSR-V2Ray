#!/usr/bin/python
import requests
import base64
import chardet
import sys,os

configfilepath='configfile/'

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()

def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

#SS SSR
#url='https://jj-rss-01.best/link/hdgQoZAinkcQIqeD?sub=1'

#V2ray
url='https://jj-rss-01.best/link/hdgQoZAinkcQIqeD?sub=3'

links_file=configfilepath+'url_jj.txt'
base64_file=configfilepath+'base64_jj.txt'

r = requests.get(url, allow_redirects=True)  # to get content after redirection
#print(chardet.detect(r.content))
if chardet.detect(base64.b64decode(r.content))['encoding']=='ascii':
#if chardet.detect(r.content)['encoding']=='ascii':
    str_line=base64.b64decode(r.content).decode().split('\n')

    keys=['ss://','ssr://','vess://']
    for value in keys:
        if str_line[0].find(value)>=0:
           with open(base64_file, 'wb') as f:
               f.write(r.content)
               f.close
               print('\n几鸡订阅更新完成！\n')
           
    if os.path.exists(links_file):
        if os.path.exists(links_file+'.bak'):
            os.remove(links_file+'.bak')
        os.rename(links_file,links_file+'.bak')

    ToFile(base64_file,links_file)
else:
    print('\n几鸡订阅地址不可用或尝试关闭代理后更新！\n')