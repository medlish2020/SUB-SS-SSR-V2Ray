#!/usr/bin/python
#发送邮件至指定邮箱
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
_user = "feitian1974@163.com"
_pwd  = "PVUTSPZWDJLBUTTC"
_to   = "feitian1974@163.com"
smtpserver="smtp.163.com" 
 
#如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"]="服务器订阅文件"
msg["From"]=_user
msg["To"]=_to

configfilepath='configfile/'
 
links_file=[configfilepath+'url_ss_ssr.txt',configfilepath+'url_v2ray.txt',configfilepath+'url_all.txt',configfilepath+'url_jj.txt',configfilepath+'base64_ss_ssr.txt',configfilepath+'base64_v2ray.txt',configfilepath+'base64_all.txt',configfilepath+'base64_jj.txt']
links_url=['免费SS-SSR订阅：\nhttps://zhuwei.netlify.com/base64_ss_ssr.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_ss_ssr.txt\n','免费V2Ray订阅：\nhttps://zhuwei.netlify.com/base64_v2ray.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_v2ray.txt\n','所有免费订阅：\nhttps://zhuwei.netlify.com/base64_all.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_all.txt\n','几鸡订阅：\nhttps://zhuwei.netlify.com/base64_jj.txt\nhttps://raw.githubusercontent.com/jaove/SUB-SS-SSR-V2Ray/master/base64_jj.txt']

#---文字部分---
url=''
for value in links_url:
    url=url+value+"\n"
part=MIMEText(url)
msg.attach(part)
 
#---附件部分---
#链接文件附件
for value in links_file:
    part=MIMEApplication(open(value,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=value)
    msg.attach(part)
 
#Base64编码后附件
#part=MIMEApplication(open(base64file_v2ray,'rb').read())
#part.add_header('Content-Disposition', 'attachment', filename=base64file_v2ray)
#msg.attach(part)
 
send = smtplib.SMTP(smtpserver, timeout=30)#连接smtp邮件服务器,端口默认是25
send.login(_user, _pwd)#登陆服务器
send.sendmail(_user, _to, msg.as_string())#发送邮件
send.close()
print('\n订阅文件发送邮箱完成！\n')