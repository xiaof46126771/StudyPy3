# -*- coding: UTF-8 -*-

fpath = r'D:\tmp.txt'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

with open(fpath, 'w') as fw:
    fw.write('bbbb')
