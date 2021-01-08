#!/usr/bin/python
import base64
import time
import sys,os
import socket
from qqwry import QQwry
q = QQwry()
q.load_file('qqwry/qqwry.dat')

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

import re

def isIP(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False


myStr = "255.255.abc.255"

#ToBase64("./desk.jpg",'desk_base64.txt')  # 文件转换为base64
#ToFile("./desk_base64.txt",'desk_cp_by_base64.jpg')  # base64编码转换为二进制文件

t=0
count = len(open(configfilepath+'host-V2Ray.txt','r',encoding='UTF-8', errors='ignore').readlines())
# f = open('../gui-config.json','w')
#f = open('Url_Vmess.txt','w',encoding='UTF-8', errors='ignore')
file_object = open(configfilepath+'host-V2Ray.txt','r',encoding='UTF-8', errors='ignore')

lineStr64=''
try: 
    for line in file_object:
        line=line.strip('\n')
        data=line.split('\t')
        
        numofproxy = str(t+1).zfill(3)
        
        if isIP(data[1]):
            server_ip = data[1]
 #           print(data[1],"is a IP!")
        else:
            server_name = socket.getaddrinfo(data[1], None)
            server_ip=server_name[0][4][0]
#            print(data[1], "is not a IP!")        
#        server_name = socket.getaddrinfo(data[1], None)
#        server_ip=server_name[0][4][0]
 
        location=q.lookup(server_ip)
        country=location[0]    
       
        lineStr='{\n'
        lineStr=lineStr+'  "v": "2",\n'
        if (len(data)>1):
            lineStr=lineStr+'  "ps": "'+country+'-V2Ray-'+numofproxy+'",\n'
        else:
            lineStr=lineStr+'  "ps": "",\n'
        if (len(data)>1):
            lineStr=lineStr+'  "add": "'+data[1]+'",\n'
        else:
            lineStr=lineStr+'  "add": "",\n'
        if (len(data)>2):
            lineStr=lineStr+'  "port": "'+data[2]+'",\n'
        else:
            lineStr=lineStr+'  "port": "",\n'
        if (len(data)>3):
            lineStr=lineStr+'  "id": "'+data[3]+'",\n'
        else:
            lineStr=lineStr+'  "id": "",\n'
        lineStr=lineStr+'  "aid": "0",\n'
        if (len(data)>4):
            lineStr=lineStr+'  "net": "'+data[4]+'",\n'
        else:
            lineStr=lineStr+'  "net": "",\n'
        lineStr=lineStr+'  "type": "none",\n'
        lineStr=lineStr+'  "host": "",\n'
        if (len(data)>5):
            lineStr=lineStr+'  "path": "'+data[5]+'",\n'
        else:
            lineStr=lineStr+'  "path": "",\n'
        if (len(data)>6):
            lineStr=lineStr+'  "tls": "'+data[6]+'"\n'
        else:
            lineStr=lineStr+'  "tls": ""\n'
        lineStr=lineStr+'}\n'
        
        lineStr64=lineStr64+'vmess://'+str(base64.b64encode(lineStr.encode("utf-8")), "utf-8")+'\n'
#        print (lineStr)
        t=t+1
except socket.gaierror:
        print(data[1])
        pass
finally:

    #添加自建服务器vmess链接至订阅文件
    file_ownerurl = open(configfilepath+'owner_url_v2ray.txt','r',encoding='UTF-8', errors='ignore')
    line_ownerurl = ''
    for line in file_ownerurl:
        line_ownerurl = line_ownerurl+line        
    lineStr64 = line_ownerurl+lineStr64
    #End

    #转换自建服务器至base64格式
    ToBase64(configfilepath+'owner_url_v2ray.txt',configfilepath+'base64_owner_url_v2ray.txt')
    #End

    #links_file = 'Url_Vmess_links_{}.txt'.format(time.strftime('%Y-%m-%d_%H-%M-%S'))
    links_file=configfilepath+'url_v2ray.txt'
    
    if os.path.exists(links_file):
        if os.path.exists(links_file+'.bak'):
            os.remove(links_file+'.bak')
        os.rename(links_file,links_file+'.bak')
    f = open(links_file,'w',encoding='UTF-8', errors='ignore')
    f.write(lineStr64)
    f.close()
    file_object.close()
    file_ownerurl.close()
    
    #生成指定文件名的base64文件
    base64file_v2ray=configfilepath+'base64_v2ray.txt'
    ToBase64(links_file,base64file_v2ray)
    
    print('\n免费V2Ray节点订阅更新完成！\n')