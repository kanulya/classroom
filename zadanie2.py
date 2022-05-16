
# Банкомат
# Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 
# 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.

from collections import OrderedDict

n = int(input())
class bankomat(object):
    def __init__(self, x=10):
        self.r = OrderedDict(((5000, x), (2000, x), (1000, x), (500, x), (200, x), (100, x), (50, x), (20, x), (10, x), (5, x), (3, x), (1, x)))

    def get_money(self, s):
        res = {5000: 0, 2000: 0, 1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 3: 0, 1: 0}
        for k, _ in self.r.items():
            if s == 0:
                break
            while self.r[k] > 0 and s >= k:
                self.r[k] = self.r[k] - 1
                res[k] += 1
                s -= k
        if s == 0:
            print(res)
        else:
            raise ValueError

b = bankomat()
b.get_money(n)