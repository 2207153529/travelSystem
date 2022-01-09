# -*- coding: utf-8 -*-
# @Author: 100yang
# @Date:   2020-04-24
# @Last Modified by:   100yang
# @Last Modified time: 2020-05-12
import requests
from bs4 import BeautifulSoup
# <title>非常抱歉，您访问的页面不存在-去哪儿网Qunar.com</title>


class QuNar:
    def __init__(self, article_id):
        self.baseURL = 'https://travel.qunar.com/travelbook/note/' + article_id

    def getPage(self):
        try:
            url = self.baseURL
            html = requests.get(url).content
            # print(html)
            soup = BeautifulSoup(html, 'lxml')
            return soup
        except Exception as e:
            raise e

    def getTitle(self):
        soup = self.getPage()
        if soup and soup.title.string.find('非常抱歉，您访问的页面不存在') == -1:
            return soup.find(id="booktitle").string
        else:
            return None

    def getContent(self):
        soup = self.getPage()
        if soup:
            string = ""
            for x in soup.find_all('link'):
                a = x.attrs['href']
                x['href'] = "https:" + a
                string = string + '\n' + str(x)
            # 将img　中src值　指向真实的图片地址
            for x in soup.find_all('img'):
                if x.get('data-original'):
                    x['src'] = x.get('data-original')
            Info = soup.find("div", class_='b_foreword')
            content = soup.find(id="b_panel_schedule")
            body = str(Info) + string + '\n' + str(content)
            # print(string + '\n' + str(content))
            return body
        else:
            return None

    def getAuthor(self):
        soup = self.getPage()
        s = soup.find_all('script')
        a = s[-5].string.find('nickName')
        b = s[-5].string.find('spaceBadge')
        return s[-5].string[a + 11:b - 3]
        # print(a, b)
        # print(s[-5].string[a + 11:b - 3])


class Hotel:
    def __init__(self, addr):
        self.baseURL = 'https://hotel.qunar.com/cn/' + addr

    def GetPage(self):
        try:
            url = self.baseURL
            html = requests.get(url).content
            # print(html)
            soup = BeautifulSoup(html, 'lxml')
            return soup
        except Exception as e:
            raise e

    def getDetail(self):
        soup = self.GetPage()
        tmp = soup.find('ul', id='hotel_lst_body')
        hotel_item = tmp.find_all('li', class_='item')
        img_list = []
        name_list = []
        score_list = []
        price_list = []
        msg_list = []
        href_list = []
        for item in hotel_item:
            img = item.find('img').attrs['src']
            # print(img)
            name = item.find('a', class_='hotel-name').get_text()
            # print(name)
            score = item.find('p', class_='comm').find('span', class_='num').get_text()
            # print(score)
            price = item.find('p', class_='price_new').get_text()
            # print(price)
            msg = item.find('p', class_="adress").get_text()
            # print(msg)
            href = item.find('a', class_='hotel-name').attrs['href']
            href = 'https://hotel.qunar.com' + href
            img_list.append(img)
            name_list.append(name)
            score_list.append(score)
            price_list.append(price[1:len(price) - 1])
            msg_list.append(msg)
            href_list.append(href)
        return [img_list, name_list, score_list, price_list, msg_list, href_list]


def getModule(id):
    return QuNar(id)


def getCity(addr):
    return Hotel(addr)
