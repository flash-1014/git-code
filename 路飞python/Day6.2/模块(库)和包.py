# os操作系统的模块
# import os
# os.mkdir("six document")

# 或者
# from os import system
#
# system("df -h")

import My_first_mod
import sys
from My_first_mod import sayhi
#打印当前脚本路径
print(__file__)
#打印当前文件路径
print(sys.path)

print(My_first_mod.sayhi())
sayhi()