#coding=utf-8
import re
import requests
import os
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='django',
        )
cur = conn.cursor()

def findimg(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
    f = requests.get(url)
    html = f.text


    pagecurrt=re.search('class="page-ch">.*?(\d+).*?</span>',html,re.S).group(1)  #获取总页数

    out1 = os.path.dirname(url)
    outurl = os.path.basename(url)
    filename = outurl.split("/")[-1].split(".")[0]
    pagecurrt=int(pagecurrt)
    findurlimg(url)
    for i in range(2,pagecurrt):
       nurl=re.sub(filename+'.html',filename+'_%d.html'%i,url,re.S)
       findurlimg(nurl)



def findurlimg(url):

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
    f = requests.get(url,headers=header)
    html = f.text
    contentpic = re.search('class="content-pic">.*?<img.*?src="(.*?)".*?/>', html, re.S).group(1)

    downloadimg(contentpic)


def downloadimg(url):
    print "download:" + url
    parram = 'http://.*?/'
    out = re.sub(parram,'', url)
    out="learn/static/"+out

    # 插入一条数据
    inset = cur.execute("insert into learn_fileimg(filename) values('"+out+"')")
    #cur.close()
    conn.commit()

    out1 = os.path.dirname(out)
    outurl = os.path.exists(out1)

    if not outurl:
         os.makedirs(out1)

    pic = requests.get(url)
    fp = open(out, 'wb')
    fp.write(pic.content)
    fp.close()

url="http://www.mm131.com/xiaohua/946.html"
findimg(url)
conn.close()