#!/usr/bin/python
import sys

configfilepath='configfile/'

print('\n请粘贴SS及SSR账号内容，粘贴内容完毕后按回车后，按组合键ctrl+D保存提交内容:')
lines=sys.stdin.readlines()
links_file=configfilepath+'host-SS.txt'

if lines:
    fileObject = open(links_file,'w',encoding='UTF-8', errors='ignore')
    for line in lines:
        fileObject.write(line)
    print('\nSS及SSR账号已保存！\n')
    fileObject.close()
else:
    print('\n未输入SS及SSR账号，原SS及SSR账号内容未修改！\n')

print('请粘贴V2Ray账号内容，粘贴内容完毕后按回车后，按组合键ctrl+D保存提交内容:')
lines=sys.stdin.readlines()
links_file=configfilepath+'host-V2Ray.txt'
fileObject = open(links_file,'w',encoding='UTF-8', errors='ignore')

for line in lines:
    fileObject.write(line)
print('\nV2Ray账号已保存！\n')
fileObject.close()

print('请粘贴V2Ray账号内容，粘贴内容完毕后按回车后，按组合键ctrl+D保存提交内容:')
lines=sys.stdin.readlines()
links_file=configfilepath+'host-V2Ray.txt'
fileObject = open(links_file,'w',encoding='UTF-8', errors='ignore')

for line in lines:
    fileObject.write(line)
print('\nV2Ray账号已保存！\n')
fileObject.close()
