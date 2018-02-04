# -*- coding:utf-8 -*-
# date:2017-7-15
# author:Alex

'''
前程无忧网招聘信息爬虫
'''

import re
import time
import requests
from bs4 import BeautifulSoup
from urllib import quote
from citynum import city_to_num
# from savedata import get_mysql
import smtplib,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def send_email(text):
    # text = self.claw_content()
    # open('b.txt', 'w').write(str(text[1]) + '\n' + str(text[0]) + '\n')
    username = '15623863340@163.com'  # input("请输入账号:")
    password = '133499cug'  # input("请输入密码:")
    username = 'lsl_cug@126.com'  # input("请输入账号:")
    password = '123456lsl'
    #username = 'lishulincug@126.com'  # input("请输入账号:")
    #password = '133499cug'
    sender = username
    # sender=''
    receiver = ['760140853@qq.com','2696231685@qq.com']  # '760140853@qq.com','xxxxxxxxxx@qq.com','xxxxxxxxxx@126.com','994992333@qq.com','1847725033@qq.com','1847725033@qq.com','849281511@qq.com'
    if sender == '':
        username = str(raw_input("Please Input Sender Email Address,for example:xxxxxxxxxx@126.com \n"))
        sender = username
        password = str(raw_input("Please Input Sender Password \n"))
        receiver.append(str(raw_input("Please Input Receiver Address,for example:xxxxxxxxxx@qq.com \n")))
    iRec = 1
    while iRec > 0:
        CmdRec = ''  # raw_input("Whether you want to add another Receiver Address(default n)? \n")
        if CmdRec == 'y' or CmdRec == 'yes':
            iRec = 1
            receiver.append(str(raw_input("Please Input Receiver Address,for example:xxxxxxxxxx@qq.com \n")))
        else:
            iRec = 0

    ConfirmRec = ''  # raw_input("Confirm? \n")
    if ConfirmRec == 'n' or ConfirmRec == 'no':
        print("What Do You Want? Maybe run this program again.\n")
        exit(1)
    else:
        for rece in receiver:
            print("OK \n" + username + " sendto " + rece)
            # 创建一个带附件的实例
    msg = MIMEMultipart()
    # msg = MIMEText(str(text), 'plain', 'utf-8')
    msg['From'] = formataddr(['user', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = ",".join(receiver)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    subject_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    subject = '筛选后招聘信息'
    msg['Subject'] = subject

    # 邮件正文内容
    # print str(text[0])
    realText = text  # sendmsg #str(text)  #'\n'+str(subject_time)+'：主人，有人来招人啦！^—^\n'+ '海投网：'+str(text[1])+'.'#+str(text[0])#'地大就业网招聘公告：'+str(text1[1])+'地大就业网gis等招聘信息：'+str(text2[1])+'.'#+str(text1[0])+'\n'+str(text2[1])+'\n'+str(text2[0])
    print realText
    msg.attach(MIMEText(realText, 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    # att1 = MIMEApplication(open('b.txt', 'rb').read())
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1.add_header('Content-Disposition', 'attachment', filename='hjx.txt')
    # msg.attach(att1)
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
        smtp = smtplib.SMTP(smtpserver, 25)
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
            smtp = smtplib.SMTP(smtpserver, 25)
            smtp.starttls()
            smtp.login(username, password)
            for jj in receiver:
                smtp.sendmail(sender, jj, msg.as_string())
                time.sleep(35)
            smtp.quit()
            print(u"邮件发送成功")
        except smtplib.SMTPException, e1:
            print(u"Error: 无法发送邮件:" + str(e1))
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
                smtp = smtplib.SMTP(smtpserver, 25)
                smtp.starttls()
                smtp.login(username, password)
                smtp.sendmail(sender, receiver, msg.as_string())
                smtp.quit()
                print(u"邮件发送成功")
            except smtplib.SMTPException, e2:
                print(u"Error: 无法发送邮件:" + str(e2))
                smtp.quit()
class Myspider(object):
    def __init__(self,dbname,mykey,mycitys):
        '''链接数据库并自动生成一个表格'''
        self.dbname = dbname
        self.key = mykey
        self.citys = mycitys
        self.Headers ={
            "Host": "search.51job.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
        }
        # 获取城市代码
        citynum = city_to_num.get_citynum(self.citys)
        # 起始链接，其中城市要用城市代码
        # self.start_url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea={}&keyword={}&keywordtype" \
        #                  "=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9".format(quote(citynum),quote(self.key))
        self.start_url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea={}&keyword={}&keywordtype" \
                         "=2,06%252C07%252C08%252C09%252C10,&lang=c&stype=1&postchannel=0000&workyear=99&cotype=04%2C08%2C10&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(quote(citynum),
                                                                                             quote(self.key))
        self.start_url='http://search.51job.com/list/{},000000,0000,00,2,06%252C07%252C08%252C09%252C10,{},2%252C06%25252C07%25252C08%25252C09%25252C10%252C,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=04%2C08%2C10&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(quote(citynum), quote(self.key).replace('%','%25'))
        # self.start_url='http://search.51job.com/list/{},000000,0000,00,2,06,{},2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(quote(citynum), quote(self.key).replace('%','%25'))
        if(self.key=='外贸'):
            self.start_url ='http://search.51job.com/list/{},000000,0000,00,2,06%252C07%252C08%252C09%252C10,%25E5%25A4%2596%25E8%25B4%25B8,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=04%2C08%2C10&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(quote(citynum))
        elif (self.key == '银行'):
            self.start_url ='http://search.51job.com/list/{},000000,0000,00,2,06,%25E9%2593%25B6%25E8%25A1%258C,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(quote(citynum))
        elif(self.key=='经理'):
            self.start_url='http://search.51job.com/list/{},000000,0000,00,2,06%252C07%252C08%252C09%252C10,%25E7%25BB%258F%25E7%2590%2586,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=01%2C04%2C08%2C10&degreefrom=04&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(quote(citynum))
        # self.mysql = get_mysql(self.dbname,self.key,self.citys)

    def get_one_page(self,url):
        '''从第一页开始，获取信息，并判断是否有下一页，如若有则继续爬虫，递归翻页'''
        print url
        # req = requests.get(url,headers=self.Headers)
        req = requests.get(url)
        req.encoding = "gbk"
        soup = BeautifulSoup(req.text,"lxml")
        # 获取所有职位信息，第一条是标题
        jobs = soup.select("#resultList > div.el")[1:]
        alldata=[]
        for job in jobs:
            data = {}
            data["job_name"] = job.select("p.t1")[0].text.strip()
            data["job_link"] = job.select("p.t1 > span > a")[0].get("href")
            data["gs_name"] = job.select("span.t2")[0].text.strip()
            data["gs_link"] = job.select("span.t2 > a")[0].get("href")
            data["job_site"] = job.select("span.t3")[0].text.strip()
            data["salary"] = job.select("span.t4")[0].text.strip()
            data["create_date"] = job.select("span.t5")[0].text.strip()
            print(data)
            alldata.append(data)
            # self.mysql.insert_data(data)

        try:
            next_url = soup.select("li.bk")[-1].select("a")[0].get("href")
            pagenum = re.findall(",(\d+)\.html",next_url)[0]
            if(pagenum<=2):
                print("获取下一页的链接，开始爬取第{}页的信息".format(pagenum))
                self.get_one_page(next_url)
        except:
            print("无法获取下一页的链接，想必已经爬到了最后一页了，爬虫即将结束")
        return alldata

    def main(self):
        '''尝试爬信息并保存到数据库，若爬虫失败也要关闭数据库连接'''
        getdata=[]
        try:
            getdata=self.get_one_page(spider.start_url)
            # getdata
        except Exception as e:
            print(e)
        finally:
            # self.mysql.close_mytable()
            if (getdata !=None):
                return getdata

if __name__ == '__main__':
    t = time.time()
    dbname = "51job"
    KEYs = ['银行','外贸','经理']
    # 城市使用一个列表，因为前程无忧可以一次多选城市查询
    CITYS = ["深圳","南宁","广州"]
    sendmsg ='招聘信息\n'
    for CITY in CITYS:
        for KEY in KEYs:
            spider = Myspider(dbname,KEY,CITYS)
            #resu=spider.main()
            sendmsg +=str(CITY)+str(KEY)+': '+str(spider.start_url) +'\n'
            #for imsg in resu[:6]:
            #    for j in imsg:
            #        sendmsg += imsg[j]+" "
            #    sendmsg +='\n'
    send_email(sendmsg)
    print("耗时：{:.2f}秒".format(float(time.time() - t)))
    # self.start_url='http://search.51job.com/list/040000,000000,0000,00,9,99,%25E5%25A4%2596%25E8%25B4%25B8,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='#外贸
    # 'http://search.51job.com/list/040000,000000,0000,00,9,99,%25E9%2593%25B6%25E8%25A1%258C,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='#银行
    # 'http://search.51job.com/list/040000,000000,0000,00,9,06%252C07%252C08%252C09%252C10,%25E7%25BB%258F%25E7%2590%2586,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=01%2C04%2C08%2C10&degreefrom=04&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=7&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='#经理





