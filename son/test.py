# -*- coding: UTF-8 -*-

# Filename  :   MathCalcGenerate.py
# Author    :   XiaoFeng

# import random module
import random

cnt = 1

while cnt <= 10:
    #print(cnt)
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    if 1 == 1:
        result = a + b
        if result <= 100:
            print('{0} + {1} = '.format(a, b))
            cnt += 1
