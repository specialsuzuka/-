import requests
import json

url = "http://toy1.weather.com.cn/search?cityname=徐州"

res = requests.get(url=url)
str=res.text
data=json.loads(str)
print(data)

