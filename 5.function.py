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

# 2.位置参数

# 3.关键字参数

# 4.默认参数

# 5.可变长参数 *args

# 可变长参数 **kwargs
























