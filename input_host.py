#!/usr/bin/python
import sys

configfilepath='configfile/'

print('\n请粘贴SS及SSR账号内容，粘贴内容完毕后按回车后，按组合键ctrl+D保存提交内容:')
lines=sys.stdin.readlines()
links_file=configfilepath+'host-SS.txt'
if lines:
    line_temp=''
    for line in lines:
        line_temp=line_temp+line
    line_temp=line_temp.strip()
    if len(line_temp) > 0:
        fileObject = open(links_file,'w',encoding='UTF-8', errors='ignore')
        fileObject.write(line_temp)
        fileObject.close()
        print('\n SS及SSR账号内容已保存！\n')
    else:
        print('\n\033[1;31m 提交SS及SSR账号内容为空，原SS及SSR账号内容未修改！\033[0m\n')
else:
    print('\n\033[1;31m 未提交SS及SSR账号内容，原SS及SSR账号内容未修改！\033[0m\n')

print('请粘贴V2Ray账号内容，粘贴内容完毕后按回车后，按组合键ctrl+D保存提交内容:')
lines=sys.stdin.readlines()
links_file=configfilepath+'host-V2Ray.txt'
if lines:
    line_temp=''
    for line in lines:
        line_temp=line_temp+line
    line_temp=line_temp.strip()
    if len(line_temp) > 0:
        fileObject = open(links_file,'w',encoding='UTF-8', errors='ignore')
        fileObject.write(line_temp)
        fileObject.close()
        print('\n V2Ray账号内容已保存！\n')
    else:
        print('\n\033[1;31m 提交V2Ray账号内容为空，原V2Ray账号内容未修改！\033[0m\n')
else:
    print('\n\033[1;31m 未提交V2Ray账号内容，原V2Ray账号内容未修改！\033[0m\n')

print('请粘贴自建节点账号内容，粘贴内容完毕后按回车后，按组合键ctrl+D保存提交内容:')
lines=sys.stdin.readlines()
links_file=configfilepath+'owner_url_v2ray.txt'
if lines:
    line_temp=''
    for line in lines:
        line_temp=line_temp+line
    line_temp=line_temp.strip()
    if len(line_temp) > 0:
        fileObject = open(links_file,'w',encoding='UTF-8', errors='ignore')
        fileObject.write(line_temp)
        fileObject.close()
        print('\n 自建节点账号内容已保存！\n')
    else:
        print('\n\033[1;31m 提交自建节点V2Ray账号内容为空，原自建节点V2Ray账号内容未修改！\033[0m\n')
else:
    print('\n\033[1;31m 未提交自建节点V2Ray账号内容，原自建节点V2Ray账号内容未修改！\033[0m\n')