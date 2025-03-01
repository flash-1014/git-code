#导入一个包，随机数的模块
import random
#获取1~100的随机数
print(round(random.random()*100))
#导入一个时间的包
import datetime
#打印当前时间，格式为年/月/日 时:分:秒
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
