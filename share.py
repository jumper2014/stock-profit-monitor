# coding=utf-8
# 股票类


class Share(object):
    def __init__(self, code, name, number, cost):
        """
        初始化
        :param code: 股票代码
        :param name: 股票名，仅仅用于显示
        :param number: 持有股数
        :param cost: 持有成本
        """
        self.code = code
        self.name = name
        self.number = number
        self.cost = cost
        self.today = 0    # 今日盈亏
        self.total = 0    # 总盈亏

    def calc_profit(self, yesterday, current):
        """
        通过开盘价和当前价计算今日盈亏和总盈亏
        :param yesterday: 昨日收盘价
        :param current: 当前价格
        :return:
        """
        self.today = (current - yesterday) * self.number
        self.total = (current - self.cost) * self.number
        print(self.code, self.name, self.total)


