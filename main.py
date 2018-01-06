# coding=utf-8
# author: ijumper
# 支持运行时修改json配置文件

import time
import json
import requests
import threading
from stock import Stock


retrieve_interval = 60  # 抓取间隔
config_json = "owned.json"  # 股票信息配置文件


def read_json():
    with open(config_json, 'r') as f:
        contents = json.loads(f.read())
        return contents


def show_stock_data(stock):
    slice_num, value_num = 21, 3
    name, now = u'——无——', u'  ——无——'
    if stock.code in ['s_sh000001', 's_sz399001']:
        slice_num = 23
        value_num = 1
    r = requests.get("http://hq.sinajs.cn/list=%s" % (stock.code,))
    res = r.text.split(',')
    if len(res) > 1:
        name, now = r.text.split(',')[0][slice_num:], r.text.split(',')[value_num]
    stock.show_profit(float(now), float(now))


if __name__ == '__main__':
    while True:
        # 实时获得配置信息
        configs = read_json()
        stocks = list()
        for config in configs:
            stock = Stock(code=config["code"], name=config["name"],
                          number=config["number"], cost=config["cost"])
            stocks.append(stock)

        # 启动多线程，抓取股票实时价格
        threads = list()
        for stock in stocks:
            t = threading.Thread(target=show_stock_data, args=(stock,))
            threads.append(t)
            t.setDaemon(True)
            t.start()
            time.sleep(0.1)

        for t in threads:
            t.join()

        # 设置抓取频度
        time.sleep(retrieve_interval)

