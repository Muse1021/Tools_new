# -*-coding: utf-8 -*-
import requests     # 导入requests模块
from bs4 import BeautifulSoup as bs # 从bs4 模块中导入BeautifulSoup模块并命名为bs
from Utils import *
def getapp():
    getlist = "adb shell pm list packages"
    Poplog = subprocess.Popen(getlist,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    A = Poplog.stdout.readlines()
    x = len(A)
    applist= {"":""}
    for s in range(x):
        s = A[s].split(":")[1].split("\r")[0]
        applist[s] = ""
    return applist
def getname_mi():
    lists = getapp()
    for s in lists.keys():
        url = "http://app.mi.com/details?id="+s
        res = requests.get(url)
        if res.url != "http://app.mi.com/":
            response = bs(res.text,'lxml')
            #print "%s:"%s+response.h3.string
            lists[s] = response.h3.string
        else:
            del lists[s]
    return lists
def getname_yyb():
    lists = getapp()
    for s in lists:
        url = "http://sj.qq.com/myapp/detail.htm?apkName="+s
        res = requests.get(url)
        response = bs(res.text,'lxml')
        if response.find('div',{'class':'det-name-int'}):
			print response.find('div',{'class':'det-name-int'}).text
print getname_mi()



