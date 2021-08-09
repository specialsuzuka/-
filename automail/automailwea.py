
# 1. 封装成class
    # Weather:
        # GetWeather(city)
    # Mail:
        # MailWeatherTo(address)
    # City:
        # GetCityCode(city_name) -> city_code
    # main:
        # 定时执行（APScheduler）
# https://www.cnblogs.com/leffss/p/11912364.html



import yaml
import logging
from City import city
from Mail import mail
from Weather import weather

import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


def get_yaml_df(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    file_df = file.read()
    file.close()

    print(file_df)
    print("类型：", type(file_df))

    # 将字符串转化为字典或列表
    df = yaml.load(file_df)
    print(df)
    print("类型：", type(df))
    return df


def mail_weather():
    config = get_yaml_df("config.yaml")
    for info in config:
        nickname = info['nickname']
        city_name = info['city']
        mail_address = info['mail_address']
        city_code = city.get_city_code(city_name)
        content = weather.get_weather(city_code)
        mail.MailWeatherTo(mail_address, city_name, content,nickname)
        logging.info("mail to {}, city {}".format(mail_address, city_code))


if __name__ == "__main__":
    print("1")
    scheduler = BlockingScheduler()
    # scheduler.add_job(mail_weather, trigger='cron', second='*/30')
    scheduler.add_job(mail_weather, 'interval', hous=24)
    logging.info("end")
    scheduler.start()
    print("2")




