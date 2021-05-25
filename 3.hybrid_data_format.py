# 4.1 列表

# 4.1.1 列表的表达
# 序列类型：内部元素有位置关系，能通过位置序号访问其中元素
# 列表是一个可以使用多种类型元素，支持元素的增删改查操作的序列类型
ls = ["Python", 1989, True, {"version": 3.7}]
# 另一种产生方式：list(可迭代对象)-----字符串、元组、集合、range()等
# 字符串转列表
list("人工智能是未来的趋势")
# 元组转列表
list(("我"， "们"， "很"， "像"))
# 集合转列表
list({"李雷", "韩梅梅", "Jim", "Green"})
# 特殊的range(起始数字,中止数字,数字间隔)
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
for i in range(6):
    print(i)
# 起始数字缺省为0，必须包含中止数字，数字间隔缺省为1
for i in range(1, 11, 2):
    print(i)   # 1 3 5 7 9
# range()转列表
list(range(1, 11, 2))  # [1, 3, 5, 7, 9]

# 4.1.2 列表的性质
# 列表的长度-len(list)
# 列表的索引 -  变量名[位置编号]   正向索引0开始  反向索引-1开始  
# 列表切片   -  变量名[开始位置：结束位置：切片间隔]

# 4.1.3 列表的操作符
# 用list1+list2形式实现列表拼接
a = [1, 2]
b = [3, 4]
a+b            # 该用法用的不多
# 用 n*list 或 list*n 实现列表的成倍复制
[0]*10   # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 4.1.4 列表的操作方法
# 【1】增加元素
# 在末尾增加元素-列表.append(待增元素)
languages = ["Python", "C++", "R"]
languages.append("Java")   # ['Python', 'C++', 'R', 'Java']
# 在任意位置插入元素-列表.insert(位置编号，待增元素)
# 其位置编号相应元素前插入待增元素
languages.insert(1, "C")   # ['Python', 'C', 'C++', 'R', 'Java']
# 在末尾整体并入另一列表-列表1.extend(列表2)
# append 将列表2整体作为一个元素添加到列表1中
languages.append(["Ruby", "PHP"])  # ['Python', 'C', 'C++', 'R', 'Java', ['Ruby', 'PHP']]
# extend 将列表2内的元素逐个添加到列表1中
languages.extend(["Ruby","PHP"])   # ['Python', 'C', 'C++', 'R', 'Java', 'Ruby', 'PHP']
# 【2】删除元素
# 删除列表i位置的元素   列表.pop(位置)
languages = ['Python', 'C', 'C++', 'R', 'Java']
languages.pop(1)   # ['Python', 'C++', 'R', 'Java']
# 不写位置信息，默认删除最后一个元素
languages.pop()
# 删除列表之间中的第一次出现的待删元素-列表.remove(待删元素)
languages = ['Python', 'C', 'R', 'C', 'Java']
languages.remove("C")   # ['Python', 'R', 'C', 'Java']
while "C" in languages:
    languages.remove("C")    # ['Python', 'R', 'Java']
# 【3】查找元素
# 列表中第一次出现待查元素的位置-列表.index(待查元素)
languages = ['Python', 'C', 'R','Java']
idx = languages.index("R")   # 2
# 【4】修改元素
# 通过“先索引后赋值”的方式，对元素进行修改-列表名[位置]=新值
languages = ['Python', 'C', 'R','Java']
languages[1] = "C++"
# 【5】列表的复制
# 1.浅拷贝   列表.copy()
languages = ['Python', 'C', 'R','Java']
languages_2 = languages.copy()  
languages.pop()     
print(languages)    # ['Python', 'C', 'R']
print(languages_2)  # ['Python', 'C', 'R', 'Java']
# 2.列表[:]
languages = ['Python', 'C', 'R','Java']
languages_3 = languages[:]
languages.pop()
print(languages)    # ['Python', 'C', 'R']
print(languages_3)  # ['Python', 'C', 'R', 'Java']
# 【6】列表的排序
# 使用列表.sort()对列表进行永久排序
# 直接在列表上进行操作，无返回值
ls = [2, 5, 2, 8, 19, 3, 7]
ls.sort()  # [2, 2, 3, 5, 7, 8, 19]
# 递减
ls.sort(reverse = True)   # [19, 8, 7, 5, 3, 2, 2]
# 使用sorted(列表)对列表进行临时排序
# 原列表保持不变，返回排序后的列表
ls = [2, 5, 2, 8, 19, 3, 7]
ls_2 = sorted(ls)
print(ls)    # [2, 5, 2, 8, 19, 3, 7]
print(ls_2)  # [19, 8, 7, 5, 3, 2, 2]
sorted(ls, reverse = True)  # [19, 8, 7, 5, 3, 2, 2]
# 【7】列表的翻转
# 使用列表.reverse()对列表进行永久翻转
# 直接在列表上进行操作，无返回值
ls = [1, 2, 3, 4, 5]
print(ls[::-1])  # [5, 4, 3, 2, 1]
# 【8】使用for循环对列表进行遍历
ls = [1, 2, 3, 4, 5]
for i in ls:
    print(i)

# 4.2 元组

# 4.2.1 元组的表达
# 元组是一个可以使用多种类型元素，一但定义，内部元素不支持增删改操作的序列类型---不可变的列表
names = ("Peter", "Pual", "Mary")

# 4.2.2 元组的操作
# 不支持增删改。其他操作和列表一致

# 4.2.3 元组的常见用处
# 打包与解包
# example 1
def f1(x):   # 返回x的平方和立方 
    return x**2, x**3   # 实现打包返回
f1(3)  # (9, 27)
type(f1(3))  # <class 'tuple'>
a, b = f1(3)  # 实现解包赋值   a 9  b 27
# example 2
numbers = [201901, 201902, 201903]
name = ["小明", "小红", "小强"]
list(zip(numbers, name))   # [(201901, '小明'), (201902, '小红'), (201903, '小强')]
for number, name in zip(numbers, name):  # 每次取到一个元组 立刻解包赋值
    print(number, name)

# 4.3 字典

# 4.3.1 字典的表达
# 映射类型：通过"键":"值"的映射实现数据存储和查找    常规字典无序
students = {201901: '小明', 201902: '小红', 201903: '小强'}
# 字典键是唯一的、字典键必须是不可变类型，如果键可变找不到对应存储的值了
# 不可变类型：数字、字符串、元组
# 可变类型：列表、字典、集合
d1 = {1: 3}
d2 = {"s": 3}
d3 = {(1,2,3): 3}

# 4.3.2 字典的性质
# 字典的长度-键值对的个数 len(dict)
# 字典的索引- 字典[键] 来获取对应值
students = {201901: '小明', 201902: '小红', 201903: '小强'}
students[201902]  # '小红'

# 4.3.3 字典的操作方法
# 【1】增加键值对
# 变量名[新键] = 新值
students = {201901: '小明', 201902: '小红', 201903: '小强'}
students[201904] = "小雪"  # {201901: '小明', 201902: '小红', 201903: '小强', 201904: '小雪'}
# 【2】删除键值对
# 1.del 变量名[待删除键]
del students[201903]  # {201901: '小明', 201902: '小红'}
# 2.变量名.pop(待删除键),同时删除键值对的值
value = students.pop(201903)  # {201901: '小明', 201902: '小红'}
# 3.变量名.popitem()随机删除一个键值对，并以元组返回删除键值对
students = {201901: '小明', 201902: '小红', 201903: '小强'}
key, value = students.popitem()
# 【3】修改值
# 通过先索引后赋值的方式对相应的值进行修改
students = {201901: '小明', 201902: '小红', 201903: '小强'}
students[201902] = "小雪 # {201901: '小明', 201902: '小雪', 201903: '小强'}
# 【4】d.get()方法
# d.get(key,default) 从字典d中获取键key对应的值，如果没有这个键，则返回default
s = "牛奶奶找刘奶奶买牛奶"
d = {}
for i in s:
    d[i] = d.get(i, 0)+1
print(d)  # {'牛': 2, '奶': 5, '找': 1, '刘': 1, '买': 1}
# 【5】d.keys()  s.values()方法
students = {201901: '小明', 201902: '小红', 201903: '小强'}
print(list(students.keys()))     # [201901, 201902, 201903]
print(list(students.values()))   # ['小明', '小红', '小强']
# 【6】d.items()方法及字典的遍历
print(list(students.items()))  # [(201901, '小明'), (201902, '小红'), (201903, '小强')]
for k, v in students.items():
    print(k, v)
        
# 4.4 集合
# 4.4.1 集合的表达
# 一系列互不相等元素的无序集合  必须是不可变类型：数字，字符串/元组，可视作字典的键
# 可看做是没有值，或者值为None的字典
students = {"小明", "小红", "小强", "小明"}   #可用于去重
# 4.4.2 集合的运算
# 通过集合进行交集并集的运算
Chinese_A = {"刘德华", "张学友", "张曼玉", "钟楚红", "古天乐", "林青霞"}
Math_A = {"林青霞", "郭富城", "王祖贤", "刘德华", "张曼玉", "黎明"}
# 语文和数学两门均为A的学员
# S & T 返回一个新集合，包括同时在集合S和T中的元素
Chinese_A & Math_A  # {'刘德华', '张曼玉', '林青霞'}
# 语文或数学至少一门为A的学员，S | T 返回一个新集合，包括集合S和T中的所有元素
Chinese_A | Math_A  
# {'刘德华', '古天乐', '张学友', '张曼玉', '林青霞', '王祖贤', '郭富城', '钟楚红', '黎明'}
# 语文数学只有一门为A的学员，S ^ T 返回一个新集合，包括集合S和T中的非共同元素
Chinese_A ^ Math_A  # {'古天乐', '张学友', '王祖贤', '郭富城', '钟楚红', '黎明'}
# 语文为A，数学不为A的学员，S - T 返回一个新集合，包括在集合S但不在集合T中的元素
Chinese_A - Math_A  # {'古天乐', '张学友', '钟楚红'}
# 数学为A，语文不为A的学员
Math_A - Chinese_A  # {'王祖贤', '郭富城', '黎明'}
# 4.4.3 集合的操作方法  
# 【1】增加元素-S.add(x)
stars = {"刘德华", "张学友", "张曼玉"}
stars.add("王祖贤")  # {'刘德华', '张学友', '张曼玉', '王祖贤'}
# 【2】移除元素-S.remove(x)
stars.remove("王祖贤")  # {'刘德华', '张学友', '张曼玉'}
# 【3】集合的长度-len(S)
len(stars)
# 【4】集合的遍历-借助for循环
for star in stars:
    print(star)
