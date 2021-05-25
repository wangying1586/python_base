# 程序结构控制
# 非顺序式的程序控制，需要根据特定条件决定程序运行路线。


# 一、条件测试
# 1、比较运算
a = 10
b = 8
print(a > b)     # 大于
print(a < b)     # 小于
print(a >= b)    # 大于等于
print(a <= b)    # 小于等于
print(a == b)    # 等于
print(a != b)    # 不等于
# 非空
ls = [1]
if ls:            # 数据结构不为空、变量不为0、None、False 则条件成立
    print("非空")
else:
    print("空的")
# 2、逻辑运算
# 与或非
a = 10
b = 8
c = 12
print((a > b) and (b > c))    # 与
print((a > b) or (b > c))     # 或
print(not(a > b))             # 非
# 复合逻辑运算优先级------- 非>与>或
# 3、存在运算
# 元素 (not)in 列表/字符串
cars = ["BYD", "BMW", "AUDI", "TOYOTA"]
print("BMW" (not)in cars)
print("BENZ" (not)in cars)

# 二、分支结构-if语句
# 1、单分支
age = 8
if age > 7:
    print("孩子，你该上学啦！")
# 2、二分支
age = 6
if age > 7:
    print("孩子，你该上学啦！")
else:
    print("再玩两年泥巴！")
# 3、多分支
age = 38
if age < 7:
    print("再玩两年泥巴")
elif age < 13:
    print("孩子，你该上小学啦")
elif age < 16:
    print("孩子，你该上初中了")
elif age < 19:
    print("孩子，你该上高中了")
elif age < 23:
    print("大学生活快乐")
elif age < 60:
    print("辛苦了，各行各业的工作者们")
else:     # 有时为了清楚，也可以写成elif age >= 60:
    print("享受退休生活吧") 
# 4、嵌套语句
# 年满18周岁，在非公共场合方可抽烟，判断某种情形下是否可以抽烟
age = eval(input("请输入年龄"))
if age > 18:
    is_public_place = bool(eval(input("公共场合请输入1，非公共场合请输入0")))
    print(is_public_place)
    if not is_public_place:
        print("可以抽烟")
    else:
        print("禁止抽烟")
else:
    print("禁止抽烟")

# 三、遍历循环-for循环
# 1、直接迭代-----列表[]/元组()/集合{}/字符串""
graduates = ("李雷", "韩梅梅", "Jim")
for graduate in graduates:
    print("Congratulations, "+graduate)
# 2、变换迭代-----字典
students = {201901: "xiaoming", 201902: "xiaohong", 201903: "xiaoqiang"}
for k, v in students.items():
    print(k, v)
for student in students.keys():
  print(student)
# 3、range()对象
res = []
for i in range(1000):
    res.append(i**2)
print(res[:5])  # [0, 1, 4, 9, 16]
print(res[-1])  # 99980001
res = []
for i in range(1, 10, 2):
    res.append(i**2)
print(res)  # [1, 9, 25, 49, 81]
# 4、循环控制：break----退出循环   continue----退出本次循环，进入下一次循环
# 5、for与else的配合
product_scores = [89, 90, 99, 70, 67, 78, 85, 92, 77, 82] # 1组10个产品的性能评分
 # 如果低于75分的超过1个，则该组产品不合格
i = 0
for score in product_scores:
    if score < 75:
        i+=1 
    if i == 2:
        print("产品抽检不合格")
        break
else:
    print("产品抽检合格")
    
# 四、无限循环-while循环
# 4.1 为什么要用while循环
# 猜数字
albert_age = 18
#第1次
guess = int(input(">>:"))
if guess > albert_age :
    print("猜的太大了，往小里试试...")
elif guess < albert_age :
    print("猜的太小了，往大里试试...")
else:
    print("恭喜你，猜对了...")
#第2次
guess = int(input(">>:"))
if guess > albert_age :
    print("猜的太大了，往小里试试...")
elif guess < albert_age :
    print("猜的太小了，往大里试试...")
else:
    print("恭喜你，猜对了...")

# 4.2 while循环的一般形式
albert_age = 18 
guess = int(input(">>:"))
while guess != albert_age: 
    if guess > albert_age :
        print("猜的太大了，往小里试试...")
    elif guess < albert_age :
        print("猜的太小了，往大里试试...")
    guess = int(input(">>:"))
print("恭喜你，猜对了...")
# 4.3 while与风向标
albert_age = 18 
flag = True     # 布尔类型
while flag:
    guess = int(input(">>:"))
    if guess > albert_age :
        print("猜的太大了，往小里试试...")
    elif guess < albert_age :
        print("猜的太小了，往大里试试...")
    else:
        print("恭喜你，猜对了...")
        flag = False    # 当诉求得到满足，就让风向变一下
# 4.4 while与循环控制break、continue
albert_age = 18 
while True:
    guess = int(input(">>:"))
    if guess > albert_age :
        print("猜的太大了，往小里试试...")
    elif guess < albert_age :
        print("猜的太小了，往大里试试...")
    else:
        print("恭喜你，猜对了...")
        break    # 当诉求得到满足，就跳出循环
# 输出10以内的奇数
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue       # 跳出本次循环，进入下一次循环
    print(i)
# 4.5 while与else
# 如果while 循环全部执行完毕，没有被break中止，则运行else块
count = 0
while count <= 5:
    count += 1
    print("Loop", count)
else:
    print("循环正常执行完啦！！！")
# 4.6 Two Examples
# No.1 删除列表中的特定值
pets = ["dog", "cat", "dog", "pig", "goldfish", "rabbit", "cat"]
while "cat" in pets:
    pets.remove("cat")  # ['dog', 'dog', 'pig', 'goldfish', 'rabbit']
# No.2 将未读书籍列表中书名分别输出后，存入已读书籍列表
not_read = ["1", "2", "3"]
have_read = []
while not_read:
    book = not_read.pop()
    have_read.append(book)
    print("读过{}".format(book))

# 五、控制语句注意问题
# 5.1 尽可能减少多层嵌套-----------可读性差，容易把人搞疯掉

# 5.2 避免死循环-------------------条件一直成立，循环永无止境

# 5.3 封装过于复杂的判断条件--------如果条件判断里表达式过于复杂，出现太多not/and/or 导致可读性大打折扣
# 考虑将条件封装为函数
a, b, c, d, e = 10, 8, 6, 2, 0
if (a > b) and (c > d) and (not e):
    print("我已经晕鸟")

numbers = (10, 8, 6, 2, 0)
def judge(num):
    a, b, c, d, e = num
    x = a > b
    y = c > d
    z = not e
    return x and y and z

if judge(numbers):
    print("就是这个feel，biu倍儿爽")


