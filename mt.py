#_*_ coding:utf-8 _*_
import multiprocessing
from multiprocessing import Process as ps
from bs4 import BeautifulSoup as bs
import requests as rq
import lxml
import re

def process(a):
    
    url = "https://www.dy2018.com/i/101" + str(a)  +".html"
    print(url)
    x = rq.get(url)
    x.encoding = 'gb2312'
    xt = x.text
    y = bs(xt,"lxml")
    yt = y.find('title')
    yt = yt.text
    # yt= yt.split('《')
    # yt = yt[1]
    # yt = yt.split("》")
    # yt = yt[0]
    # print(yt)
    # yd = y.find_all('a')
    # for ya in yd:
    #     # print(ya['href'])
    #     yf = ya['href']
    #     if yf[:6] == 'magnet':
    #         print(yt)
    
    
 
if __name__ == '__main__':
    
    
    for i in range(000, 999):
        p = multiprocessing.Process(target=process, args=(i, ))
        p.start()
        # p.join()
    
    
