
"""
数据类型：数字、字符串、布尔类型、列表、元祖、字典、集合
变量：命令、保留字、赋值
控制流程：顺序语句、循环语句for、while、分支语句if
输入和输出：input、eval、print、formate
程序格式：缩进、注释
"""

"""
# 数据类型
Python保留字：and、as、assert、break、class、continue、def、del、elif、else、except、False、finally、for、from、global、if、import
in、is、lambda、None、nonlocal、not、or、pass、raise、return、True、try、while、with、yield

数据元素+外部输入到控制语句－>输出

变量命名规则：
【1】字母、数字、汉字、下划线以及组合
【2】严格区分大小写
【3】尽量具备实际意义
【4】首字母不能为数字
【5】中间不能有空格
【6】不能是Python保留字

格式化输出："字符{0:修饰}字符{1:修饰}".format(v1,v2)
"""

"""
基础数据类型－－－－－－－－－－－－－－
【1】数字类型：分类int、float、complex，操作符+－*/%//**，操作函数abs()、max()...
【2】字符串类型：基本性质索引、切片，操作符+*in，操作函数len()、count()...
【3】布尔类型：逻辑运算and、or、not
【4】类型转换：类型判断type()、isinstance()，类型转换str(),int()...

继承－－－类和实例

[1]数字类型
int整数－进制的转换-----2
float浮点数－运算可存在不确定小数-------2.0 
complex复数------ 3+4j
运算操作符－加减乘除，整数商、模运算，除法－结果浮点数
数字操作函数－四舍五入round、最大最小maxmain、绝对值abs、求和sum、幂次方pow、divmod、借助math包

[2]字符串类型
表达－或、转义符\
索引－正向从0开始、反向从－1开始
切片－s[a:b]不包含b
a in b－a是否是b的子集
拼接和复制－:"py"+"thon","mn"*2
处理函数－长度len、统计count、字母大小写upper/lower/letter、替换replace、删除strip、分割split、组合join

[3]布尔类型
True False、逻辑运算、作为循环的指示、numpy pandas掩码
[4]类型判别和转换
类型判别：type isinstance
字符串检查函数：isdigit、isalpha、isalnum
类别转换：str、int、float
"""

"""
组合数据类型－－－－－－－－－－－－－－
list列表-----数据有位置顺序  a = [1,2,3,4]    a[0]
tuple元组----元素不支持修改（不可变列表）  b = (1,2,3,4)  b[0]
dict字典-----通过键值实现数据存储和查找    stu = {201901:"小明",201902:"小强"}  stu[201901]
set集合------一系列互不相等元素的集合，无序  s = {"小明","小红","小强"} s
"""

"""
# 变量
x = eval(input("请输入一个数字：")) --- eval去掉引号   

# 输出控制
print(123, end=" ") end控制不换行

print("PI = {0},E = {1}".format(PI, E))

# ____3.1415926_____  进行填充
print("{0:_^20}".format(PI))
# 3.1415926*********************
print("{0:*<30}".format(PI))
# 10,000,000
print("{0:,}".format(10000000))
# 保留2位小数
print("{0:.2f}".format(PI))
# '二进制111000010,Unicode码ǂ,十进制450,八进制702,十六进制1c2'
"二进制{0:b},Unicode码{0:c},十进制{0:d},八进制{0:o},十六进制{0:x}".format(450)

"""


