#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 股票类


class Stock(object):
    def __init__(self, code, name, share, cost):
        """
        初始化
        :param code: 股票代码
        :param name: 股票名，仅仅用于显示
        :param share: 持有股数
        :param cost: 持有成本
        """
        self.code = code
        self.name = name
        self.share = share
        self.cost = cost
        self.today = 0    # 今日盈亏
        self.total = 0    # 总盈亏
        self.percent = 0.0  # 盈亏百分比

    def show_profit(self, yesterday, current):
        """
        通过开盘价和当前价计算今日盈亏和总盈亏
        :param yesterday: 昨日收盘价
        :param current: 当前价格
        :return: None
        """
        self.today = (current - yesterday) * self.share
        self.total = (current - self.cost) * self.share
        self.percent = ((current - self.cost)/self.cost) * 100
        print "---------------------------------------------"
        print self.name, " | ", self.code, " | ", self.total, " | ", round(self.percent, 2), r"%"
