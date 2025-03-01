#三个奖项，先抽三等奖，再二等奖，最后一等奖。将抽到的编号及时去除，因为每个人只能中一次奖
import random

#对三个奖1的数量进行初始化
n1 = 3
n2 = 6
n3 = 30
#构建1~300的列表
num_str = list(range(1, 301))
#循环主体
count = 0
while count < n1 + n2 + n3:
    if count < n3:  #开始抽奖
        num = random.randint(1, 300)
        #需要判断抽出的数是不是已经抽过
        if num in num_str:
            #输出恭喜中奖的提示和中奖内容
            print(f"恭喜{num}号获得三等奖湖南工程学院究极豪华垃圾桶一个！",end = "/n")
            num_str.remove(num)  # 及时剔除抽过的数
            count += 1
        else:
            continue  # 退出循环
    #二等奖的判断的抽取
    elif count < n2 + n3:
        num = random.randint(1, 300)
        if num in num_str:
            #输出恭喜中奖的提示和中奖内容
            print(f"恭喜{num}号获得二等奖究极豪华iPhone16ProMax版本手机一个！")
            num_str.remove(num)  # 及时剔除抽过的数
            count += 1
        else:
            continue  # 退出循环
    elif count < n2 + n3 + n1:
        num = random.randint(1, 300)
        if num in num_str:
            #输出恭喜中奖的提示和中奖内容
            print(f"恭喜{num}号获得一等奖究极豪华泰国5日游一次！")
            num_str.remove(num)  # 及时剔除抽过的数
            count += 1
        else:
            continue  # 退出循环
    elif count >= n1 + n2 + n3:
        break
