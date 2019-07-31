# -*- coding: utf-8 -*-
# @Time    : 2019-06-17 21:34
# @Author  : zyh
# @File    : main.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from source_html import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

browser = webdriver.Chrome()  # 创建一个浏览器对象,这里还可以使用chrome等浏览器
base_url = 'http://www.ioc-sealevelmonitoring.org/'
# url = 'http://www.ioc-sealevelmonitoring.org/station.php?code=abed'
# url = 'http://www.ioc-sealevelmonitoring.org/list.php'
# req = requests.get(html, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
soup = BeautifulSoup(html, 'lxml')
f = open('TideInfo.txt', 'a')
for continent_url in soup.find_all(name='a', attrs={"class": None}):
    if continent_url.string:
        if continent_url.string.strip() == '[open]':
            browser.get(base_url + continent_url['href'])  # 获取并打开url
            html = browser.page_source
            data = str(pq(html))
            nextpagebutton = browser.find_element_by_xpath('//span[contains(@onclick,"newgraph")]')  # 定位到“more detail”按钮
            nextpagebutton.click()  # 模拟点击下一页
            soup = BeautifulSoup(browser.page_source, 'lxml')
            print('http://www.ioc-sealevelmonitoring.org')
            print()
            data_info = {"station": None, "station_id": None, "create_time": None, "latitude": None, "longitude": None, "sea_level": None, "units": None,
                         "country": None, "time_zone": None, "time_span": None, "date_source": None, "interval_time": None, "date_url": base_url + continent_url['href']}
            for i in range(0, len(list(soup.find_all(name="td", attrs={"class": "field", "colspan": None})))):
                # print(list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i])
                # print(list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i])
                # print("A")
                if list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string:
                    # print(list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip())
                    # print("C")
                    # print("i: "+str(i))
                    if list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Location':
                        # print(list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i])
                        # print(list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i])
                        # print("B")
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            # print("i: "+str(i))
                            data_info["station"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'GLOSS ID':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["station_id"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Added to the system':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["create_time"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Latitude':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["latitude"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Longitude':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["longitude"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Sea Level':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["sea_level"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Units of measure':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["units"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Country':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["country"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Time Zone':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["time_zone"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Time Span':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["time_span"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Data Source':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["date_source"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Transmit interval (min)':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["interval_time"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
                    elif list(soup.find_all(name="td", attrs={"class": "field", "colspan": None}))[i].string.strip() == 'Transmit interval (min)':
                        if list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string:
                            data_info["date_url"] = list(soup.find_all(name="td", attrs={"class": "nice", "align": None}))[i].string.strip()
            for key, value in data_info.items():
                print(key+':'+value)
                f.write(value+';')
            f.write('\n')
            # wait = WebDriverWait(browser, 30)  # 浏览器等待10s
f.close()
