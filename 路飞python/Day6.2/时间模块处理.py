import time
from time import gmtime

# 当前时间localtime(sec)secc参数未提供则以当前时间为准
# print(time.localtime())
# print(gmtime())
# # # 将当前时间转化为时间戳时间，时间戳是从1970年1月1日开始以秒计时的时间格式
# print(time.time())
# # # 将本地strut_time啥时间格式转化成时间戳格式
# time.mktime(time.localtime())

# 推迟进程时间
# time.sleep(5)
# print(time.localtime(time.time()))

# 将时间元组或者struct_time转换为格式化的时间字符串，有固定参数
# Y:年，m月，d天，H小时，M分钟，S秒。加不加localtime都一样
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(time.strftime("%Y-%m-%d %H:%M:%S"))#, time.localtime()))
# time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# print(time_str)
# #字符串转时间
# print(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))
#
# # 引入datatime包
# import datetime
# d = datetime.datetime.now()
# print(d.timetuple())
#
# #引入随机数模块
import random
# a = random.randint(1,10)
# print(a)
# b = random.randrange(1,100)
# print(b)
# c = random.random()
# print(c)
# d = random.choices("abcdefg")
# print(d)
# e =  random.sample("gywjakq",3)
# print(e)

#进阶生成特定的随机字符串,字符里面的26个小写英文加数字组成10位数密码
import string
randstring = ''.join(random.sample(string.ascii_lowercase + string.digits, 10))
print(randstring)
#洗牌shuffle
a = [1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a)