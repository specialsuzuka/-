import random
import requests
import socket
import time
from bs4 import BeautifulSoup


class Weather:

    def get_city_url(self, city_code):
        city_url = "http://www.weather.com.cn/weather/" + city_code + ".shtml"
        return city_url

    def get_content(self, city_url):
        header = {
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4557.4 Safari/537.36"
        }
        timeout = random.choice(range(80, 180))
        while True:
            try:
                rep = requests.get(url=city_url, headers=header, timeout=timeout)
                rep.encoding = 'utf-8'
                break
            except socket.timeout as e:
                print('3:', e)
                time.sleep(random.choice(range(8, 15)))
            except socket.error as e:
                print('4:', e)
                time.sleep(random.choice(range(20, 60)))
        return rep.text

    def get_weather(self, city_code):
        url = self.get_city_url(city_code)
        html_text = self.get_content(url)
        bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
        body = bs.body  # 获取body部分)
        df = body.find('div', {'id': '7d'})  # 找到id=7d的div
        ul = df.find('ul', {'class': 't clearfix'})
        li = ul.find_all('li')
        day = li[1]
        temp = []
        date = day.find('h1').string  # 找到日期
        temp.append(date)
        inf = day.find_all('p')  # 找到li标签中所有的p标签
        temp.append(inf[0].string)  # 将第一个p标签中的内容（天气状况）加入到temp中
        if inf[1].find('span') is None:
            emperature_higgest = None  # 天气预报可能没有当天的最高气温（到了傍晚，就是这样），需要加一个判断，来输出最低气温
        else:
            temperature_higgest = inf[1].find('span').string  # 找到最高气温
            # temperature_higgest = temperature_higgest.replace('℃', '') # 到了晚上网站内容会有变动，去掉这个符号
        if inf[1].find('i') is None:
            temperature_lowest = None
        else:
            temperature_lowest = inf[1].find('i').string  # 找到最低温度
        if inf[2].find("i") is None:
            wind_level = None
        else:
            wind_level = inf[2].find("i").string
            # temperature_lowest = temperature_lowest.replace('℃', '')
            temp.append(temperature_higgest)
            temp.append(temperature_lowest)
            temp.append(wind_level)

        return temp


weather = Weather()
