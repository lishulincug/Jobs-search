#-*- coding:utf-8 -*-
import urllib2, json
import re
import chardet
from prettytable import PrettyTable
import smtplib
# from time import strftime,gmtime
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication
# import base64

# from PIL import Image,ImageFont,ImageDraw
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
tableHeader2 = ["职位名称",'单位名称', "工作地点",'发布日期']
username = 'lsl_cug@126.com'#input("请输入账号:")
password = '123456lsl'#input("请输入密码:")
sender = username
receiver = ['1627041882@qq.com','994992333@qq.com']# 'xxxxxxxxxx@qq.com','xxxxxxxxxx@126.com'
smtpserver = 'smtp.126.com'
keysword = ['GIS', '地理', '地图', '遥感','测绘', '数据', '机器学习','图像识别']
#keysword = ['物探', '地球物理', '勘查技术与工程','地球探测与信息技术']

# 一般网页关键词搜索匹配，返回存在的关键词
def cugjiuye_search( url, keys,decode):
    # url = ["http://cug.91wllm.com"]

    result = []
    # pt1 = PrettyTable(tableHeader1)
    # for key in keys:
    if url[0]=='':
        req = urllib2.Request(str(keys), headers=headers)
    else:
        req = urllib2.Request(url[0] + str(keys), headers=headers)
    if decode!='utf-8':
        # content = urllib2.urlopen(req).read()
        # char_type = chardet.detect(content)
        # pattern = re.compile(
        #     'content="text/html; charset=(.*?)" />',re.S)
        # itemdecode = re.findall(pattern, content)
        # if itemdecode!='':
        #     # content = urllib2.urlopen(req).read().decode(str(itemdecode[0]))
        #     content = urllib2.urlopen(req).read().decode(chardet["encoding"].lower())
        # else:
        content = urllib2.urlopen(req).read().decode(chardet["encoding"].lower())
    else:
        content = urllib2.urlopen(req).read().decode('utf-8')
    # pattern = re.compile(
    #     '<ul class="infoList">.*?<li class=.*?<a href="(.*?)" target="_blank">(.*?)</a></li>.*?">(.*?)</li>.*?">(.*?)</li>',re.S)
    # items1 = re.findall(pattern, content)
    for word in keysword:
        if word in content:
            result.append(word)
    return result

class Xiaozhao(object):
    # 海投网检索
    # |  2017-09-23 14:30  |   地大   |       上海数慧系统技术有限公司       |                    西区教三楼201                     |
    def claw_content(self):
        urls = ["https://xjh.haitou.cc/wh/uni-6/page-", 'https://xjh.haitou.cc/wh/uni-2/page-',
                'https://xjh.haitou.cc/wh/uni-1/page-', 'https://xjh.haitou.cc/wh/uni-3/page-']  # 海投网湖北
        haitou_url=['https://xjh.haitou.cc']
        tableHeader = ["日期",'专业', '学校', "公司", "宣讲地点",'链接']
        pt = PrettyTable(tableHeader)
        # pt3 = PrettyTable(tableHeader)
        urls1=[]
        now = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
        H=now[9:11]
        for url in urls:
            urls1.append(url+str(1))
            for page in range(1,3):#
                req = urllib2.Request(url+str(page), headers=headers)
                content = urllib2.urlopen(req).read().decode('utf-8')
                #print content
                pattern = re.compile('<tr data-key=.*?cxxt-title"><a href="(.*?)" title=.*?success company">(.*?)</div><span>(.*?)</span></a>.*?"hold-ymd">(.*?)</span>.*?<span class=.*?">\((.*?)\)</span></td><td class="text-ellipsis"><span title="(.*?)">.*?</a></td></tr>',re.S)
                items = re.findall(pattern, content)
                for item in items:
                    if "</span>" in item[2]:
                        del item
                    else:
                        pt.align["公司"] = "l"  # 以name字段左对齐
                        pt.padding_width = 2  # 填充宽度
                        if (item[4]==u'今天')or(item[4]==u'明天' and (int(H)<=24)and (int(H)>=21)):
                            time.sleep(0.4)
                            reword = cugjiuye_search(haitou_url, item[0],'utf-8')
                            if reword.__len__() >= 1:
                                pt.add_row([item[3],reword[0], item[2],item[1], item[5],haitou_url[0]+item[0]])#, item[4]
        return pt,urls1
    #地大就业网招聘公告检索
    def dida_ZhaopinGonggao(self):
        urls = ["http://cug.91wllm.com/campus/index?keyword=&range=&city=&time=&page="]
        cugurl=['http://cug.91wllm.com/']
        tableHeader1 = ['专业',"招聘公告", "工作城市", '发布时间','链接']
        pt1 = PrettyTable(tableHeader1)
        for url in urls:
          for page in range(1,10):#
            req = urllib2.Request(url+str(page), headers=headers)
            content = urllib2.urlopen(req).read().decode('utf-8')
            #print content
            pattern = re.compile('<ul class="infoList">.*?<li class=.*?<a href="(.*?)" target="_blank">(.*?)</a></li>.*?">(.*?)</li>.*?">(.*?)</li>',re.S)
            items1 = re.findall(pattern, content)
            for item1 in items1:
                if "</a>" in item1[0]:
                    del item1
                else:
                    time.sleep(0.5)
                    reword=cugjiuye_search(cugurl,item1[0],'utf-8')
                    if reword.__len__()>=1:
                        pt1.align["工作城市"] = "l"  # 以name字段左对齐
                        pt1.padding_width = 2  # 填充宽度
                        if len(item1[1])>=26:
                            pt1.add_row([reword[0],item1[1][0:26], item1[2], item1[3],cugurl[0]+item1[0]])  # , item1[4]
                        else:
                            pt1.add_row([reword[0],item1[1], item1[2],item1[3],cugurl[0]+item1[0]])#, item1[4]
                        # print [item1[1], item1[2],item1[3], item1[0]]
        return pt1,urls

    #地大就业网招聘信息&关键词职位搜索
    # GIS设计师 | 北方信息控制研究院集团有限公司 | 江苏省 | 2017 - 09 - 17
    def dida_ZhaopinXinxi_search(self):
        keys=keysword #['GIS','地理','地图','遥感','数据','机器学习']
        url = ['http://cug.91wllm.com/job/search?&title_type=1&d_industry=&d_skill=&city=&d_salary=&d_education=&time=&nature=150001%2C150007%2C150016%2C150015%2C150005&scale=&title=']
        pt1 = PrettyTable(tableHeader2)
        urls=[]
        for key in keys:
          ur = url[0] + str(key)
          urls.append(ur)
          for page in range(1,5):#
            req = urllib2.Request(url[0]+str(key)+'&page='+str(page), headers=headers)
            content = urllib2.urlopen(req).read().decode('utf-8')
            #print content
            pattern = re.compile('<ul class="infoList">.*?<li class=.*?<a href=.*?" title="(.*?)" target="_blank">(.*?)<b style="color:red;">(.*?)</b>(.*?)</a></li>.*?<a href=.*?">(.*?)</a></li>.*?">(.*?)</li>.*?">(.*?)</li>.*?">(.*?)</li>',re.S)
            items1 = re.findall(pattern, content)

            for item1 in items1:
                if "</a>" in item1[0]:
                    del item1
                else:
                    pt1.align["工作城市"] = "l"  # 以name字段左对齐
                    pt1.padding_width = 2  # 填充宽度
                    if len(item1[0])>=22:
                        pt1.add_row([item1[0][0:22], item1[4], item1[5], item1[7]])
                    else:
                        pt1.add_row([item1[0], item1[4],item1[5], item1[7]])#, item1[4]
                    # print [item1[1], item1[2],item1[3], item1[0]]
        return pt1,urls
    #地大研究生就业网搜索
    def dida_yanjiusheng_jiuye(self):
        urls=['http://yjsjy.cug.edu.cn/search.asp?PageNo=']
        cugurl = ['http://yjsjy.cug.edu.cn']
        tableHeader1 = ['专业', "招聘公告",  '发布时间', '链接']
        pt1 = PrettyTable(tableHeader1)
        for url in urls:
            for page in range(1, 5):  #
                req = urllib2.Request(url + str(page), headers=headers)
                content = urllib2.urlopen(req).read().decode('GBK')
                # print content
                # hjson = json.loads(content.read().decode('GBK'))
                pattern = re.compile(
                    '  <li>    <img src=".*?"><a href=".(.*?)"title=.*?" target="_blank">(.*?)</a></td> .*?<span class="date">(.*?)</span>  </li>', re.S)
                items1 = re.findall(pattern, content)
                for item1 in items1:
                    if "</a>" in item1[1]:
                        del item1
                    else:
                        time.sleep(0.5)
                        reword = cugjiuye_search(cugurl, item1[0],'GBK')
                        if reword.__len__() >= 1:
                            pt1.align["工作城市"] = "l"  # 以name字段左对齐
                            pt1.padding_width = 2  # 填充宽度
                            if len(item1[1]) >= 26:
                                pt1.add_row(
                                    [reword[0], item1[1][0:26], item1[2], cugurl[0] + item1[0]])  # , item1[4]
                            else:
                                pt1.add_row(
                                    [reword[0], item1[1], item1[2], cugurl[0] + item1[0]])  # , item1[4]
                                # print [item1[1], item1[2],item1[3], item1[0]]
        return pt1, urls

    #武大就业网招聘信息检索
    def wuda_jiuye(self):
        urls = ["http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/xjhxx_cxXjhForWeb.html#",'http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/zfjy!wzxx!whdx10486/xjhxx_ckXjhxx.html?sqbh=53f14d59c2e07b9af5d572797e50a67b'] #宣讲会
        urls1 = ['http://www.xsjy.whu.edu.cn/default.html'] #招聘信息
        urls2=["http://xsjy.whu.edu.cn/zftal-web/zfjy!wzxx!whdx10486/dwzpxx_cxWzDwzpxxNryEX.html#iframe"]

        url=['http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/xjhxx_cxXjhForWeb.html#iframe']
        wut_url=['http://xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/dwzpxx_cxWzDwzpxxNry.html?dwxxid=']
        urls=['http://xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/dwzpxx_cxWzDwzpxxNry.html?dwxxid=JG0015741']
        cugurl=['']
        tableHeader1 = ['专业',"招聘公告",'链接']
        pt1 = PrettyTable(tableHeader1)
        for url in urls1:
          for page in range(1,3):#
            req = urllib2.Request(url, headers=headers)
            content = urllib2.urlopen(req).read().decode('GBK')
            # print content
            pattern = re.compile('<li class="xwzd"><a href="(.*?)" target="_blank" title=(.*?)>.*?</a><span class=',re.S)
            pattern1 = re.compile('<li><a href="(.*?)" target="_blank" title=(.*?)>.*?</a><span class=',
                                 re.S)
            pattern2 = re.compile('<a href="(.*?)" target="_blank" >(.*?)</a>',
                                  re.S)
            items = re.findall(pattern1, content)
            items1 = re.findall(pattern, content)
            items2 = re.findall(pattern2, content)
            items1.extend(items)
            # items1.extend(items2)
            for item1 in items1:
                if "</a>" in item1[0]:
                    del item1
                else:
                    time.sleep(0.6)
                    print item1[0]
                    reword=cugjiuye_search(cugurl,item1[0],'GBK')
                    if reword.__len__()>=1:
                        pt1.align["工作城市"] = "l"  # 以name字段左对齐
                        pt1.padding_width = 2  # 填充宽度
                        if len(item1[1])>=26:
                            pt1.add_row([reword[0],item1[1][0:26],item1[0]])  # , item1[4]
                        else:
                            pt1.add_row([reword[0],item1[1], item1[0]])#, item1[4]
                        # print [item1[1], item1[2],item1[3], item1[0]]
        return pt1,urls

        # 华科就业网招聘信息检索
    def huake_jiuye(self):
        urls = ["http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/xjhxx_cxXjhForWeb.html#",
                'http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/zfjy!wzxx!whdx10486/xjhxx_ckXjhxx.html?sqbh=53f14d59c2e07b9af5d572797e50a67b']  # 宣讲会
        urls1 = ["http://job.hust.edu.cn/searchJob_"]  # 招聘信息

        url = ['http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/xjhxx_cxXjhForWeb.html#iframe']
        wut_url = ['http://xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/dwzpxx_cxWzDwzpxxNry.html?dwxxid=']
        urls = ['http://xsjy.whu.edu.cn/zftal-web/zfjy!wzxx/dwzpxx_cxWzDwzpxxNry.html?dwxxid=JG0015741']
        cugurl = ['http://job.hust.edu.cn']
        tableHeader1 = ['专业', "招聘公告",  '发布时间', '链接']
        pt1 = PrettyTable(tableHeader1)
        for url in urls1:
            for page in range(1, 5):  #
                req = urllib2.Request(url+str(page)+'.jspx?fbsj=&q=&type=2', headers=headers)
                content = urllib2.urlopen(req).read().decode('utf-8')
                # print content
                # hjson = json.loads(urllib2.urlopen(req).read().decode('utf-8'))
                pattern = re.compile('<td>.*?<a href=".*?<a href="(.*?)" title="(.*?)" target="_blank" class=.*?</a><br>.*?</td>.*?<td width=".*?" valign="top">(.*?)</td>',re.S) #<td>.*?<a href="(.*?)" title="(.*?)" target="_blank" class=''>.*?</a><br>.*?</td>.*?<td width=".*?" valign="top">.*?</td>
                items1 = re.findall(pattern, content)
                for item1 in items1:
                    if "</a>" in item1[0]:
                        del item1
                    else:
                        time.sleep(0.5)
                        reword = cugjiuye_search(cugurl, item1[0],'utf-8')
                        if reword.__len__() >= 1:
                            pt1.align["工作城市"] = "l"  # 以name字段左对齐
                            pt1.padding_width = 2  # 填充宽度
                            if len(item1[1]) >= 26:
                                pt1.add_row(
                                    [reword[0], item1[1][0:26], item1[2],  cugurl[0] + item1[0]])  # , item1[4]
                            else:
                                pt1.add_row(
                                    [reword[0], item1[1], item1[2],  cugurl[0] + item1[0]])  # , item1[4]
                                # print [item1[1], item1[2],item1[3], item1[0]]
        return pt1, urls

    def send_email(self):
        text = self.claw_content()
        open('b.txt', 'w').write(str(text[1]) + '\n' + str(text[0]) + '\n')
        username = 'lsl_cug@126.com'  # input("请输入账号:")
        password = '123456lsl'  # input("请输入密码:")
        sender = username
        # sender=''
        receiver = ['1627041882@qq.com']  # 'xxxxxxxxxx@qq.com','xxxxxxxxxx@126.com','994992333@qq.com','1847725033@qq.com','1847725033@qq.com','849281511@qq.com'
        if sender =='':
            username = str(raw_input("Please Input Sender Email Address,for example:xxxxxxxxxx@126.com \n"))
            sender = username
            password = str(raw_input("Please Input Sender Password \n"))
            receiver.append(str(raw_input("Please Input Receiver Address,for example:xxxxxxxxxx@qq.com \n")))
        iRec = 1
        while iRec>0:
            CmdRec = ''#raw_input("Whether you want to add another Receiver Address(default n)? \n")
            if CmdRec == 'y' or CmdRec == 'yes':
                iRec = 1
                receiver.append(str(raw_input("Please Input Receiver Address,for example:xxxxxxxxxx@qq.com \n")))
            else:
                iRec = 0

        ConfirmRec = ''#raw_input("Confirm? \n")
        if ConfirmRec == 'n' or ConfirmRec == 'no':
            print("What Do You Want? Maybe run this program again.\n")
            exit(1) 
        else:
            for rece in receiver:
                print("OK \n"+ username + " sendto " + rece)
       # 创建一个带附件的实例
        msg = MIMEMultipart()
        # msg = MIMEText(str(text), 'plain', 'utf-8')
        msg['From'] = formataddr(['user', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = ",".join(receiver) # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        subject_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        subject = '宣讲会信息'
        msg['Subject'] = subject

        # 邮件正文内容
        # print str(text[0])
        realText =  '\n'+str(subject_time)+'：主人，有人来招人啦！^—^\n'+ '海投网：'+str(text[1])+'.'#+str(text[0])#'地大就业网招聘公告：'+str(text1[1])+'地大就业网gis等招聘信息：'+str(text2[1])+'.'#+str(text1[0])+'\n'+str(text2[1])+'\n'+str(text2[0])
        print realText
        msg.attach(MIMEText(realText, 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEApplication(open('b.txt', 'rb').read())
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1.add_header('Content-Disposition', 'attachment', filename='hjx.txt')
        msg.attach(att1)
        # # 构造附件1，传送当前目录下的 test.txt 文件
        # att2 = MIMEApplication(open('b1.txt', 'rb').read())
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att2.add_header('Content-Disposition', 'attachment', filename='b1.txt')
        # msg.attach(att2)
        # att3 = MIMEApplication(open('b2.txt', 'rb').read())
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att3.add_header('Content-Disposition', 'attachment', filename='b2.txt')
        # msg.attach(att3)
        smtpserver = 'smtp.126.com'
        try:
            smtp = smtplib.SMTP(smtpserver,25)
            smtp.starttls()
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
            print(u"邮件发送成功")
        except smtplib.SMTPException, e:
            print(u"Error: 无法发送邮件:" + str(e))
            smtp.quit()
            try:
                username = 'lishulincug@163.com'  # input("请输入账号:")
                password = '123456lsl'  # input("请输入密码:")
                sender = username
                # sender=''
                # receiver = [ '1627041882@qq.com','994992333@qq.com','1847725033@qq.com']  # 'xxxxxxxxxx@qq.com','xxxxxxxxxx@126.com','994992333@qq.com','1847725033@qq.com'
                msg['From'] = formataddr(['lishulin', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['To'] = ",".join(receiver)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                smtpserver = 'smtp.163.com'
                smtp = smtplib.SMTP(smtpserver,25)
                smtp.starttls()
                smtp.login(username, password)
                smtp.sendmail(sender, receiver, msg.as_string())
                smtp.quit()
                print(u"邮件发送成功")
            except smtplib.SMTPException, e1:
                print(u"Error: 无法发送邮件:"+str(e1))
                smtp.quit()
                try:
                    username = '15623863340@sina.cn'  # input("请输入账号:")
                    password = '133499'  # input("请输入密码:")
                    sender = username
                    # sender=''
                    # receiver = [ '1627041882@qq.com','994992333@qq.com','1847725033@qq.com']  # 'xxxxxxxxxx@qq.com','xxxxxxxxxx@126.com','994992333@qq.com','1847725033@qq.com'
                    msg['From'] = formataddr(['15623863340@sina.cn', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                    msg['To'] = ",".join(receiver)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                    smtpserver = 'smtp.sina.cn'
                    smtp = smtplib.SMTP(smtpserver,25)
                    smtp.starttls()
                    smtp.login(username, password)
                    smtp.sendmail(sender, receiver, msg.as_string())
                    smtp.quit()
                    print(u"邮件发送成功")
                except smtplib.SMTPException, e2:
                    print(u"Error: 无法发送邮件:" + str(e2))
                    smtp.quit()

import sched
import time

s = sched.scheduler(time.time, time.sleep)

def deb_print():
    now = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
    H=now[9:11]
    M = now[12:14]
    S = now[15:]
    # print now
    print H,M, S
    return H,M, S

def check_time(H, M,S):
    #    list=deb_print()

    if (H == "17" and M == "52"and S == "00"
                                        "") or(H == "07" and M == "45"and S == "00")or(H == "13" and M == "06"and S == "18"):#
        xiaozhao = Xiaozhao()
        xiaozhao.send_email()
        s.enter(1, 1,check_time, deb_print())
def main():
    xiaozhao = Xiaozhao()
    output='gis2.txt'
    # text1 = xiaozhao.dida_ZhaopinGonggao()
    # open(output, 'w').write(str(text1[1]) + '\n' + str(text1[0]) + '\n')
    # text3 = xiaozhao.dida_yanjiusheng_jiuye()
    # open(output, 'a+').write(str(text3[1]) + '\n' + str(text3[0]) + '\n')
    #text2 = xiaozhao.dida_ZhaopinXinxi_search()
    #open(output, 'a+').write(str(text2[1]) + '\n' + str(text2[0]) + '\n')
    # text4=xiaozhao.wuda_jiuye()
    # open(output, 'a+').write(str(text4[1]) + '\n' + str(text4[0]) + '\n')
    #text5 = xiaozhao.huake_jiuye()
    #open(output, 'a+').write(str(text5[1]) + '\n' + str(text5[0]) + '\n')
    text = xiaozhao.claw_content()
    open('b.txt', 'w').write(str(text[1]) + '\n' + str(text[0]) + '\n')

    # xiaozhao.send_email()

    # f = open("demo_1.html", 'w')
    # message = """
    # <html>
    # <head></head>
    # <body>
    # <p>str(text1[1])</p>
    # <p>demo</p>
    # </body>
    # </html>"""
    #
    # f.write(message)
    # f.close()
    while True:
        #    print time.localtime()
        #    print time.strftime("%y-%m-%d %H:%M:%S",time.localtime())
        # xiaozhao = Xiaozhao()
        # xiaozhao.send_email()
        s.enter(1, 1, check_time, deb_print())
        s.run()
if __name__=='__main__':
    main()

# import win32gui
# import win32con
# import win32clipboard as w
#
# def getText():
#     """获取剪贴板文本"""
#     w.OpenClipboard()
#     d = w.GetClipboardData(win32con.CF_UNICODETEXT)
#     w.CloseClipboard()
#     return d
#
# def setText(aString):
#     """设置剪贴板文本"""
#     w.OpenClipboard()
#     w.EmptyClipboard()
#     w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
#     w.CloseClipboard()
#
# def send_qq(to_who, msg):
#     """发送qq消息
#     to_who：qq消息接收人
#     msg：需要发送的消息
#     """
#     # 将消息写到剪贴板
#     setText(msg)
#     # 获取qq窗口句柄
#     qq = win32gui.FindWindow(None, to_who)
#     # 投递剪贴板消息到QQ窗体
#     win32gui.SendMessage(qq, 258, 22, 2080193)
#     win32gui.SendMessage(qq, 770, 0, 0)
#     # 模拟按下回车键
#     win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
#     win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
#
#
# # 测试
# to_who='xxx'
# msg='这是测试消息'
# send_qq(to_who, msg)
# */