# -*- coding: utf-8 -*-
# @Time    : 2019-06-14 10:58
# @Author  : zyh
# @File    : eol_homework.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

link_list = []
url = 'http://202.121.66.141/meol/jpk/course/layout/newpage/index.jsp?courseId=22133'
req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
soup = BeautifulSoup(req.text, 'lxml')
for x in soup.find_all(name="a", attrs={"target": "_blank"}):
    # link = x.get('href')
    link = x.string
    if link:
        link_list.append(link)
print(link_list)
# print(list(soup.find_all(name="a", attrs={"class": "href"}).string.strip()))
# for i in :
#     print(list(soup.find_all(name="a", attrs={"class": "href"}))[i].string.strip())
