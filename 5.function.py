# 函数
# 4.1 函数的定义及调用
# 4.1.1 为什么要用函数
# 提高代码复用性-抽象出来封装为函数
# 将复杂的大问题分解成一系列小问题，分而治之-模块化设计的思想
# 利于代码的维护和管理
# 1.顺序式
# 5的阶乘，20的阶乘
n = 5
res = 1
for i in range(1, n+1):
    res *= i
n = 20
res = 1
for i in range(1, n+1):
    res *= i   
# 2.抽象成函数
def factoria(x):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
factoria(5)
factoria(20)

# 4.1.2 函数的定义及调用
# 白箱子:输入-处理-输出
# 三要素：参数、函数体、返回值
# 求正方形的面积
def area_of_square(length_of_side):
    square_area = pow(length_of_side, 2)
    return square_area    
area = area_of_square(5)

# 4.1.3 参数传递
# 1.形参与实参
# 形参：函数定义时的参数，实际上是变量名
# 实参：函数调用时的参数，实际上是变量的值
# 2.位置参数
# 严格按照位置顺序，用实参对形参进行赋值，一般用在参数较少的时候
def function(x, y, z):
    print(x, y, z)
fucntion(1, 2, 3)   # 实参和形参需一一对应
# 3.关键字参数
# 打破位置限制，直呼其名的进行值的传递（形参=实参），必须实参与形参一一对应，用在参数较多场合
function(x=1, y=2, z=3)
# 位置参数和关键字参数混合使用，但未知参数必须放在关键字参数前面//不能为同一个形参重复传值
function(1, y=2, z=3)
# 4.默认参数
# 在定义阶段就给形参赋值----该形参的常用值
# 默认参数必须放在非默认参数后面，调用函数时-可以不对该形参传值
def register(name, age, sex="male"):
    print(name, age, sex)
register("大芥菜", 18)
register("林志玲", 38, "female")  # 也可
# 默认参数应该设置为不可变类型（数字、字符串、元组）
def function(ls=[]):
    print(id(ls))
    ls.append(1)
    print(id(ls))
    print(ls)
function()   # 1759752744328   1759752744328  [1]
function()   # 1759752744328   1759752744328  [1, 1]
function()   # 1759752744328   1759752744328  [1, 1, 1]
def function(ls="Python"):
    print(id(ls))
    ls += "3.7"
    print(id(ls))
    print(ls)
function()   # 1759701700656  1759754352240  Python3.7
function()   # 1759701700656  1759754353328  Python3.7
function()   # 1759701700656  1759754354352  Python3.7
# 让参数变成可选的
def name(first_name, last_name, middle_name=None):
    if middle_name:
        return first_name+middle_name+last_name
    else:
        return fist_name+last_name
print(name("大","仔"))           # 大仔
print(name("大", "仔", "杰"))    # 大杰仔
# 5.可变长参数 *args
# 不知道会传过来多少参数 *args，该形参必须放在参数列表的最后
def foo(x, y, z, *args):
    print(x, y, z)
    print(args)
foo(1, 2, 3, 4, 5, 6)   # 多余参数打包传递给args  1 2 3 (4, 5, 6)
# 实参打散
foo(1, 2, 3, [4, 5, 6])    # 1 2 3  ([4, 5, 6])
foo(1, 2, 3, *[4, 5, 6])   # 打散的是列表、字符串、元组或集合  1 2 3 (4, 5, 6)
# 可变长参数 **kwargs
def foo(x, y, z, **kwargs):
    print(x, y ,z)
    print(kwargs)
foo(1, 2, 3, a=4, b=5, c=6)    #  多余的参数，以字典的形式打包传递给kwargs
# 1 2 3 {'a': 4, 'b': 5, 'c': 6}
foo(1, 2, 3, **{"a": 4, "b": 5, "c":6}) 
# 1 2 3 {'a': 4, 'b': 5, 'c': 6}
# 可变长参数组合使用
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(1, 2, 3, a=4, b=5, c=6) 
# (1, 2, 3)  {'a': 4, 'b': 5, 'c': 6}

# 4.1.4 函数体与变量作用域
# 函数体就是一段只在函数被调用时，才会执行的代码
# 局部变量-仅在函数体内定义和发挥作用
def multipy(x, y):
    z = x*y
    return z   
multipy(2, 9)  # 函数执行完毕，局部变量z已经被释放掉了
# 全局变量-外部定义的都是全局变量，全局变量可在函数体内被直接使用
n = 3
ls = [0]
def multipy(x, y):
    z = n*x*y
    ls.append(z)
    return z   
print(multipy(2, 9))  # [0, 54]
# 通过global 在函数体内定义全局变量
def multipy(x, y):
    global z
    z = x*y
    return z 
print(multipy(2, 9))  # 18
print(z)  # 18

# 4.1.5 返回值
# 1.单个返回值
def foo(x):
    return x**2
res = foo(10)  # 100
# 2.多个返回值-以元组形式
def foo(x):
    return 1, x, x**2, x**3  
res = foo(3)  # 1, 3, 9, 27
a, b, c, d = foo(3)  # 解包赋值
# 3.可以有多个return语句，一旦其中一个执行，就代表函数运行结束
def is_holiday(day):
    if day in ["Sunday", "Saturday"]:
        return "Is holiday"
    else:
        return "Not holiday"
    print("啦啦啦德玛西亚，啦啦啦啦")  # 没机会运行
# 4.没有return语句，返回值为None
def foo():
    print("我是孙悟空")
res = foo()
print(res)  # None

# 4.1.6 几点建议
# 1.函数及其参数的命名参照变量的命名---字母小写及下划线组合并具有实际意义
# 2.应包含简要阐述函数功能的注释，注释紧跟在定义后
# 3.函数定义前后各空两行
# 4.默认参数赋值等号两侧不需空格

# 4.2 函数式编程实例
# 模块化编程思想-----自顶向下，分而治之
"""
小丹和小伟羽毛球打的都不错，水平也在伯仲之间，小丹略胜一筹，基本上，打100个球，小丹能赢55次，小伟能赢45次。
但是每次大型比赛（1局定胜负，谁先赢到21分，谁就获胜），小丹赢的概率远远大于小伟，小伟很是不服气。
亲爱的小伙伴，你能通过模拟实验，来揭示其中的奥妙吗？
----------
问题抽象：
1、在小丹Vs小伟的二元比赛系统中，小丹每球获胜概率55%，小伟每球获胜概率45%；
2、每局比赛，先赢21球（21分）者获胜；
3、假设进行n = 10000局独立的比赛，小丹会获胜多少局？（n 较大的时候，实验结果≈真实期望）
"""
# 问题分解
def main():
    prob_A, prob_B, number_of_games = get_inputs()
    win_A, win_B = sim_n_games(prob_A, prob_B, number_of_games)
    print_summary(win_A, win_B, number_of_games)
    
def get_inputs():
    prob_A = eval(input("请输入运动员A的每球获胜概率(0~1):"))
    prob_B = round(1 - prob_A, 2)
    number_of_games = eval(input("请输入模拟的场次（正整数）:"))
    print("模拟比赛总次数：", number_of_games)
    print("A 选手每球获胜概率：", prob_A)
    print("B 选手每球获胜概率：", prob_B)
    return prob_A, prob_B, number_of_games

def sim_n_games()
    win_A, win_B = 0, 0
    for i in range(number_of_games):
        score_A, score_B = sim_one_game(prob_A, prob_B)
        if score_A > score_B:
            win_A += 1
        else:
            win_B += 1
    return win_A, win_B

import random
def sim_one_games(prob_A, prob_B):
    score_A, score_B = 0, 0
    while not game_over(score_A, score_B):
        if random.random() < prob_A:  # random.random() 生产[0,1)之间的随机小数,均匀分布
            score_A += 1
        else:
            score_B += 1
    return score_A, score_B

def game_over(score_A, score_B):
    return score_A == 21 or score_B == 21
            
# 单元测试用 assert-断言
# assert expression
# 表达式结果为false的时候触发异常
assert game_over(21, 8) == True   
assert game_over(9, 21) == True
assert game_over(11, 8) == False
assert game_over(21, 8) == False  # 触发异常
print(sim_one_game(0.55, 0.45))  # (21, 7)
print(sim_one_game(0.7, 0.3))    # (21, 14)
print(sim_one_game(0.2, 0.8))    # (10, 21)
print(sim_n_games(0.55, 0.45, 1000))   # (731, 269)

# 结果汇总输出
def print_summary(win_A, win_B, number_of_games):
    # 结果汇总输出
    print("共模拟了{}场比赛".format(number_of_games))
    print("选手A获胜{0}场，占比{1:.1%}".format(win_A, win_A/number_of_games))
    print("选手B获胜{0}场，占比{1:.1%}".format(win_B, win_B/number_of_games))
   
# 完整代码流程
import random


def get_inputs():  
    # 输入原始数据
    prob_A = eval(input("请输入运动员A的每球获胜概率(0~1)："))
    prob_B = round(1-prob_A, 2)
    number_of_games = eval(input("请输入模拟的场次（正整数）："))
    print("模拟比赛总次数：", number_of_games)
    print("A 选手每球获胜概率：", prob_A)
    print("B 选手每球获胜概率：", prob_B)
    return prob_A, prob_B, number_of_games


def game_over(score_A, score_B):
    # 单场模拟结束条件，一方先达到21分，比赛结束    
    return score_A == 21 or score_B == 21


def sim_one_game(prob_A, prob_B):
    # 模拟一场比赛的结果
    score_A, score_B = 0, 0
    while not game_over(score_A, score_B):
        if random.random() < prob_A:                # random.random() 生产[0,1)之间的随机小数,均匀分布
            score_A += 1                 
        else:
            score_B += 1
    return score_A, score_B


def sim_n_games(prob_A, prob_B, number_of_games):
    # 模拟多场比赛的结果
    win_A, win_B = 0, 0                # 初始化A、B获胜的场次
    for i in range(number_of_games):   # 迭代number_of_games次
        score_A, score_B = sim_one_game(prob_A, prob_B)  # 获得模拟依次比赛的比分
        if score_A > score_B:
            win_A += 1
        else:
            win_B += 1
    return win_A, win_B


def print_summary(win_A, win_B, number_of_games):
    # 结果汇总输出
    print("共模拟了{}场比赛".format(number_of_games))
    print("\033[31m选手A获胜{0}场，占比{1:.1%}".format(win_A, win_A/number_of_games))
    print("选手B获胜{0}场，占比{1:.1%}".format(win_B, win_B/number_of_games))
    

def main():
    # 主要逻辑
    prob_A, prob_B, number_of_games = get_inputs()                        # 获取原始数据
    win_A, win_B = sim_n_games(prob_A, prob_B, number_of_games)           # 获取模拟结果
    print_summary(win_A, win_B, number_of_games)                          # 结果汇总输出


if __name__ == "__main__":
    main()
"""
请输入运动员A的每球获胜概率(0~1)：0.52
请输入模拟的场次（正整数）：10000
模拟比赛总次数： 10000
A 选手每球获胜概率： 0.52
B 选手每球获胜概率： 0.48
共模拟了10000场比赛
选手A获胜6033场，占比60.3%
选手B获胜3967场，占比39.7%
"""

# 4.3 匿名函数
# 1.基本形式
# lambda 变量：函数体
# 2.常用用法
# 在参数列表中最适合使用匿名函数，尤其是与key=搭配
# 排序sort()sorted()
ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
ls.sort()  # [(76, 94), (79, 100), (85, 85), (86, 71), (93, 88)]
ls.sort(key = lambda x: x[1])  # [(86, 71), (85, 85), (93, 88), (76, 94), (79, 100)]
ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
temp = sorted(ls, key = lambda x: x[0]+x[1], reverse=True)
# [(93, 88), (79, 100), (85, 85), (76, 94), (86, 71)]
# max()min()
ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
n = max(ls, key = lambda x: x[1])  # (79, 100)
n = min(ls, key = lambda x: x[1])  # (86, 71) 

# 4.4 面向过程和面向对象
# 面向过程-----以过程为中心的编程思想，以“什么正在发生”为主要目标进行编程。冰冰冷的程序化的
# 面向对象-----将现实世界的事物抽象成对象，更关注“谁在受影响”，更贴近现实。有血有肉的拟人化的
# 以公共汽车为例
# “面向过程”
# 汽车启动为一个事件，汽车到站为另一个事件
# 在编程序的时候我们关心的是某一个事件，而不是汽车本身。 我们分别对启动和到站编写程序。
# “面向对象”
# 构造“汽车”这个对象
# 对象包含动力、服役时间、生产厂家等等一系列的“属性”；
# 也包含加油、启动、加速、刹车、拐弯、鸣喇叭、到站、维修等一系列的“方法”。
# 通过对象的行为表达相应的事件
