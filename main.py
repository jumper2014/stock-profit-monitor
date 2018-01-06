# coding=utf-8
# author: ijumper2014
# 支持运行时修改json配置文件

import time
import json
import requests
import threading
from share import Share


def read_json():
    with open("owned.json", 'r') as f:
        contents = json.loads(f.read())
        return contents


def get_data(share):
    slice_num, value_num = 21, 3
    name, now = u'——无——', u'  ——无——'
    if share.code in ['s_sh000001', 's_sz399001']:
        slice_num = 23
        value_num = 1
    r = requests.get("http://hq.sinajs.cn/list=%s" % (share.code,))
    res = r.text.split(',')
    if len(res) > 1:
        name, now = r.text.split(',')[0][slice_num:], r.text.split(',')[value_num]
    # print(share.code, share.name, now)
    share.calc_profit(float(now), float(now))


if __name__ == '__main__':

    while True:
        configs = read_json()
        shares = list()
        for config in configs:
            share = Share(code=config["code"], name=config["name"],
                          number=config["number"], cost=config["cost"])
            shares.append(share)

        threads = list()
        for share in shares:
            t = threading.Thread(target=get_data, args=(share,))
            threads.append(t)
            t.start()
            time.sleep(0.1)

        for t in threads:
            t.join()

        time.sleep(10)

