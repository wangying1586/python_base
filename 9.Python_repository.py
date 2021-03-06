# 10.1 time库
# Python处理时间的标准库

# 1.获取现在时间
#（1）time.localtime() 本地时间
#（2）time.gmtime() UTC世界统一时间
# 北京时间比时间统一时间UTC早8个小时
import time

t_local = time.localtime()
t_UTC = time.gmtime()
print("t_local", t_local)           # 本地时间
print("t_UTC", t_UTC)               # UTC统一时间
"""
t_local time.struct_time(tm_year=2021, tm_mon=7, tm_mday=26, tm_hour=10, tm_min=17, tm_sec=15, tm_wday=0, tm_yday=207, tm_isdst=0)
t_UTC time.struct_time(tm_year=2021, tm_mon=7, tm_mday=26, tm_hour=2, tm_min=17, tm_sec=15, tm_wday=0, tm_yday=207, tm_isdst=0)
"""
time.ctime()                        # 返回本地时间的字符串
# 'Mon Jul 26 10:18:25 2021'


# 2.时间戳与计时器
"""
（1）time.time()           返回自纪元以来的秒数，记录sleep
（2）time.perf_counter()   随意选取一个时间点，记录现在时间到该时间点的间隔秒数，记录sleep
（3）time.process_time()   随意选取一个时间点，记录现在时间到该时间点的间隔秒数，不记录sleep
perf_counter()             精度较time()更高一些
"""
t_1_start = time.time()
t_2_start = time.perf_counter()
t_3_start = time.process_time()

res = 0
for i in range(1000000):
    res += i
    
time.sleep(5)
t_1_end = time.time()
t_2_end = time.perf_counter()
t_3_end = time.process_time()

print("time方法：{:.3f}秒".format(t_1_end-t_1_start))
print("perf_counter方法：{:.3f}秒".format(t_2_end-t_2_start))
print("process_time方法：{:.3f}秒".format(t_3_end-t_3_start))
"""
1622041287.8768225
3536.5760356
1.53125
time方法：5.165秒
perf_counter方法：5.166秒
process_time方法：0.156秒
"""

# 3.格式化
#（1）time.strftime 自定义格式化输出
lctime = time.localtime()
time.strftime("%Y-%m-%d %A %H:%M:%S", lctime)
# '2021-07-26 Monday 10:18:54'


# 4.睡觉觉
#（1）time.sleep()

# 10.2 random库
# 随机种子------seed  （1）相同种子会产生相同的随机数 （2）如果不设置随机种子，以系统当前时间为默认值
from random import *
seed(10)
print(random())  # 0.5714025946899135
# 产生随机整数
numbers = [randint(1, 10) for i in range(10)]  # 产生[a,b]的随机整数
numbers = [randrange(10) for i in range(10)]  # 产生[0, a)的随机整数
numbers = [randrange(0, 10, 2) for i in range(10)]  # 产生[a,b]以step步长的随机整数

# 产生随机浮点数
numbers = [random() for i in range(10)]    # 产生[0.0, 1.0)之间随机浮点数
numbers = [uniform(2.1, 3.5) for i in range(10)]    # 产生[a,b]间随机浮点数

# 序列用函数
choice(["win", "lose", "draw"])  # 从序列中随机返回一个元素
choice("python"]  # h
choices(["win", "lose", "draw"], [3, 3, 4], k=5) # k次重复采样，可设置权重
shuffle()  # 打乱序列
sample([10, 20, 30, 40, 50], k=3)  # 从pop类型中随机选取k个元素，以列表类型返回

       
# 5.概率分布-以高斯分布为例
gauss(mean, std)  #产生一个符合高斯分布的随机数
import matplotlib.pyplot as plt
res = [gauss(0, 1) for i in range(10000)]
plt.hist(res, bins=1000)
plt.show()

# example 1: random实现微信红包分配
# 数学期望(mean)是试验中每次可能结果的概率乘以其结果的总和，是最基本的数学特征之一。
# 它反映随机变量平均取值的大小
import random
import numpy as np

def red_packet(total, num):
    ls = []
    for i in range(1, num):
        # 当前红包金额为0.01-平均值的2倍之间
        per = random.uniform(0.01, total / (num - i + 1) * 2)
        total = total - per
red_pecket(10, 5)
       
# example 2: 生成4位由数字和英文字母构成的验证码
import random
import string
       
s = string.digits + string.ascii_letters
v = random.sample(s, 4)

 
# 10.3 collections库----容器数据类型
import collections
# collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
Point = collections.namedtuple("Point", ["x", "y"])
p = Point(1, y=2)
# 可调用属性，且有元组的属性
p.x, p.y
x, y = p
print(isinstance(p, tuple))  # 是元组子类

# example：模拟扑克牌
Card = collections.namedtuple("Card", ["rank", "suit"])
ranks = [str(n) for n in range(2, 11)] + list("JQKA")
suits = "spades diamonds clubs hearts".split()
cards = [Card(rank, suit) for rank in ranks
                          for suit in suits]
# 洗牌
from random import *
random.shuffle(cards)
# 抽牌
choice(cards)
# 随机抽多张牌
sample(cards, k=5)

# 2. Counter ---- 计数器工具
from collections import Counter






