# coding=utf-8
# 股票类

# import sys
# reload(sys)
# # sys.setdefaultencoding('gb2312')


class Stock(object):
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
        self.percent = 0.0  # 盈亏百分比

    def show_profit(self, yesterday, current):
        """
        通过开盘价和当前价计算今日盈亏和总盈亏
        :param yesterday: 昨日收盘价
        :param current: 当前价格
        :return:
        """
        self.today = (current - yesterday) * self.number
        self.total = (current - self.cost) * self.number
        self.percent = ((current - self.cost)/self.cost) * 100
        # print("code:{code}, name:{name}, profit:{profit}".format(
        #     code=self.code, name=self.name, profit=self.total
        # ))
        # print(self.code, self.name, self.total)
        print "---------------------------------------------"
        print self.name, " | ", self.code, " | ", self.total, " | ", self.percent
        # print(self.code)
