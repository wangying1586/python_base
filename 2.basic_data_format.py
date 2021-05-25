# 一、数字类型
# 1.1 数字类型的组成
# 1.1.1 整数-不同进制的转换
# 默认输入十进制
# 二进制Ob、八进制Oo、十六进制Ox
16 == Ob10000 == Oo20 == Ox10
a = bin(16)  # 转二进制
b = oct(16)  # 转八进制
c = hex(16)  # 转十六进制
# 0b10000 0o20 0x10
# 转换后结果为字符串类型
# 其他进制转十进制
d = int(a, 2)   # 二进制转十进制
e = int(b, 8)   # 八进制转十进制
f = int(c, 16)  # 十六进制转十进制
# 16 16 16
# 1.1.2 浮点数----不确定性
# **计算机采用二进制小数来表示浮点数的小数部分**
# * 部分小数不能用二进制小数完全表示
0.1+0.2    # 0.30000000000000004
0.1 + 0.7  # 0.7999999999999999
# 1.1.3 复数----a+bj
# j或J均可、虚部系数为1，要显式写出
2+1j

# 1.2 数字运算操作符 （a操作符b） 
13 % 5       # 3 
# 整数与浮点数运算结果是浮点数
# 除法运算的结果是浮点数

# 1.3 数字运算操作函数 
abs(-4)   # 4
abs(3+4j)  # 对复数a+bj 执行的是求模运算(a^2+b^2)^0.5   --- 5.0
pow(2, 5)  # pow(x,n) x的n次方  等价于x**n   --- 32
pow(2, 5, 3) # 2^5 % 3  更快速   --- 2
a = 1.618
print(round(a))      # 默认四舍五入为整数  --- 2
print(round(a, 2))   # 参数2表示四舍五入后保留2位小数  --- 1.62
print(round(a, 5))   # 位数不足，无需补齐  --- 1.618
# 整数商和模运算
divmod(13, 5)   # 较（x//y,x % y）更快，只执行了一次x/y  --- (2,3)
a = [3, 2, 3, 6, 9, 4, 5]
print("max:", max(a)) # max: 9
print("min:", min(a)) # min: 2
sum((1, 2, 3, 4, 5))
# 借助科学计算库 math\scipy\numpy
import math
math.exp(1)   # 指数   ---2.718...
math.log2(2)  # 对数   ---1.0
math.sqrt(4)  # 开平方运算   ---2.0
import numpy as np
a = [1, 2, 3, 4, 5]
np.mean(a)   ---均值   3.0
np.median(a) ---中位数 3.0
np.std(a)    ---标准差 1.414....


# 二、字符串类型
print("I'm 18 years old")  # I'm 18 years old
print('"Python" is good')  # "Python" is good
print("\"Python\" is good")  # \ 我是个字符呀  "Python" is good
# 等等，我还没完事！
s = "py\   # python
thon"                    

# 2.2 字符串的性质
# 2.2.1 字符串的索引
s = "My name is Peppa Pig"
print(s[0])   # M 
print(s[2])   #  
print(s[5])   # m
print(s[-1])  # g
print(s[-3])  # P
print(s[-5])  # a
# 2.2.2 字符串的切片
# 变量名[开始位置：结束位置：切片间隔]   不包含结束位置。 不设置间隔默认为1
s = "Python"
s[0:3:1]   # Pyt
s[0:3]     # Pyt
s[0:3:2]   # Pt
# 起始位置为0可省略     结束位置省略表示取到最后一个字符    可使用反向索引
s[0:6]     # Python
s[:6]      # Python
s[:]       # Python
s[-6:]     # Python
# 反向切片  起始位置-1也可省略   结束位置省略取到第一个字符
s = "123456789"
s[-1:-10:-1]    # 987654321
s[:-10:-1]      # 987654321
s[::-1]         # 987654321

# 2.3 字符串操作符
# 2.3.1 字符串的拼接
a = "I love"
b = "my wife"
a+b   # 'I love my wife '
# 2.3.2 字符串的成倍复制
c = a+b
c * 3   # I love my wife I love my wife I love my wife 
3 * c   #  I love my wife I love my wife I love my wife 
# 2.2.3 成员运算
# 子集in全集   任何一个连续的切片都是原字符串的子集
folk_singers = "Peter, Paul and Mary"    
"Peter" in folk_singers
# 遍历字符串字符  for 字符 in 字符串
for s in "Python":
    print(s)

# 2.4 字符串处理函数
# 2.4.1 字符串的长度
len(S)
# 2.4.2 字符编码
# 将中文字库，英文字母、数字、特殊字符等转化成计算机可识别的二进制数
# 每个单一字符对应一个唯一不重复的二进制编码
# Python中使用Unicode编码
# 将字符串转化为Unicode码-----ord(字符)
ord("1")  # 49
ord("a")  # 97 
ord("*")  # 42
# 将Unicode转换为字符---------chr(Unicode码)
chr(1010)  # c
chr(23456)  # 宠

# 2.5 字符串的处理方法
# 2.5.1 字符串的分割-字符串.split(分割字符)   返回一个列表，原字符串不变
languages = "Python C C++ Java PHP R"
languages_list = languages.split(" ")  # Python C C++ Java PHP R
# 2.5.2 字符串的聚合-"聚合字符".join(可迭代数据类型)   可迭代-字符串、列表
s = "12345"
s_join = ",".join(s)  # '1,2,3,4,5'
s = ["1", "2", "3", "4", "5"]
s_join = "*".join(s)  # '1*2*3*4*5'
# 2.5.3 删除两端特定字符-字符串.strip(删除字符)
# strip从两侧开始搜索，遇到指定字符执行删除，遇到非指定符，搜索停止
# 类似的还有左删除lstrip和右删除rstrip
s = "      I have many blanks     "
s.strip(" ")
s.lstrip(" ")
s.rstrip(" ")
# 2.5.4 字符串的替换-字符串.replace("被替换","替换成")
s = "Python is coming"
s1 = s.replace("Python","Py")   # Py is coming
# 2.5.5 字符串统计-字符串.count("待统计字符串")
s = "Python is an excellent language"
"an:", s.count("an")   #  an:2
"e:", s.count("e")     #  e:4
# 2.5.6 字符串字母大小写
s = "Python"
s.upper()  # 全大写
s.lower()  # 全小写
s.title()  # 首字母大写


三、布尔类型  TRUE OR FALSE
# 3.1 逻辑运算的结果
a = 10
print(a > 8)   # True
print(a == 12)  # False
print(a < 5)  # False
# any() all()
any([False, 1, 0, None])  # True
all([False, 1, 0, None])  # False

# 3.2 指示条件
n = 2800 
while True:
    m = eval(input("请输入一个正整数："))
    if m == n:
        print("你猜对啦")
        break
    elif m > n:
        print("太大了")
    else:
        print("太小了")

# 3.3 作为掩码
import numpy as np
x = np.array([[1, 3, 2, 5, 7]])
print(x > 3)   # [[False, False, False, True, True]]
x[x > 3]       # array([5, 7])


# 四、类型判别及类型转换
# 4.1 类型判别
age = 20
name = "Ada"
type(age)   #  <class 'int'>
# isinstance(变量, 预判类型)  承认继承
# 变量类型是预判类型的子类型，则为真，否则为假
isinstance(age, int)     # True
isinstance(age, object)  # object 是老祖宗  True
isinstance(name, object)  # True
# 字符串检查方法     
# 字符串.isdigit()字符是否只有数字组成
age.isdigit()   # True
name.isdigit()  # False
# 字符串.isalpha()字符是否只有字母组成
name.isalpha()  # True
age.isalpha()   # False
# 字符串.isalnum()字符是否只有数字和字母组成
"Ada20".isalnum()   # 判断用户名是否合法   True

# 4.2 类型转换
# 数字类型转字符串-str(数字类型)
str(age)
# 仅有数字组成的字符串转数字 int() float() eval()
s1 = "20"
s2 = "10.1"
int(s1)
float(s2)
float(s1)
eval(s1)
eval(s2)















