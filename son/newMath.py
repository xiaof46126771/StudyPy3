# -*- coding: UTF-8 -*-

# Filename  :   MathCalcGenerate.py
# Author    :   XiaoFeng
# Version   :   0.5

# file operation step by step
# 1 determine if the file exists.
# 2 open the file with a. example


# judge the file exists
import os
import time

# join strings , filename
fn = 'question' + time.strftime("%d%m%y")

# determine if the fn exists
s = r'D:\{0}.txt'.format(fn)
print(s)
#print(os.path.isfile(s))
if os.path.isfile(s):
    print('file is exists ')
    with open(s, 'r') as f:
        print(f.read())
else:
    with open(s, 'x') as tt:
        tt.write(time.strftime("%y-%m-%d %H:%M:%S\n"))
    with open(s, 'r') as tt:
        print(tt.read())
    print('file is not exists , create it OK !')

#with open(s, 'r') as f:
#    print(f.read())


# import random module
import random

# define variables
total = input("请输入算式的个数 :")
print("请输入计算的类型，")
opertype = input("加法为 1， 减法为 2，加减混合 为3 ：")
sum = input("请输入计算范围，默认最小值为0，请输入最大值：")
#print(total)
#print(type(total))

# define

# 思路，使用循环来实现。需要定义  个变量
# total         用来定义一共有多少个算式
# opertype      用来定义计算的类型，加法为 1， 减法为 2，加减混合 为3， 乘法为 4，除法为 5，全混合为 6
# oper          用来定义有几种操作符，该变量为数组，包含 + 、 - 、 * 、 /
# opnum         用来定义随机操作，其实为 oper 该数组的索引，当混合算式时采用随机数，默认为1，代表加法
# sum           用来定义计算范围，即计算结果的最小值和最大值。

# 如：while cnt == total
total = int(total)    # total 的数据类型默认为str，while循环判断会报错，更改为int。
#print(type(total))
sum = int(sum)
cnt = 1

while cnt <= total:
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    opertype = int(opertype)
    if opertype == 1:
        result = a + b
        if result <= sum:
            with open(s, 'a') as ad:
                ad.writelines('{0} + {1} =  \n'.format(a, b))
            print('{0} + {1} = {2}'.format(a, b, result))
            cnt += 1
    elif opertype == 2:
        result = a - b
        if (result >= 0) and (result <= sum):
            with open(s, 'a') as sub:
                sub.writelines('{0} - {1} = \n'.format(a, b))
            print('{0} - {1} = {2}'.format(a, b, result))
            cnt += 1
