import requests
import json

# 用户city_name
# toy1.weather.com.cn

# 用户city_name
# toy1.weather.com.cn
# save


class City:
    def get_city_code(self, city_name):
        url = "http://toy1.weather.com.cn/search?cityname=" + city_name
        res = requests.get(url=url)
        s = res.text
        df = json.loads(s.strip("(").strip(")"))
        # print(df)
        city_code = df[0]["ref"][0:9]
        return city_code


city = City()
# print(city.get_city_code("赣榆"))
