import random

# 三个奖项的数量
n1 = 3  # 一等奖数量
n2 = 6  # 二等奖数量
n3 = 30  # 三等奖数量

# 1~300的列表
num_str = list(range(1, 301))

# 初始化计数器
coun = 0

# 循环主体
while coun < n1 + n2 + n3:
    if coun < n3:  # 抽三等奖
        num = random.randint(1, 300)  # 随机1~300的一个数
        if num in num_str:
            print(f"恭喜获得三等奖！{num}号")
            num_str.remove(num)
            coun += 1
        else:
            continue

    elif coun < n2 + n3:  # 抽二等奖
        num = random.randint(1, 300)  # 随机1~300的一个数
        if num in num_str:
            print(f"恭喜获得二等奖！{num}号")
            num_str.remove(num)
            coun += 1
        else:
            continue

    elif coun < n1 + n2 + n3:  # 抽一等奖
        num = random.randint(1, 300)  # 随机1~300的一个数
        if num in num_str:
            print(f"恭喜获得一等奖！{num}号")
            num_str.remove(num)
            coun += 1
        else:
            continue

    if coun >= n1 + n2 + n3:
        break
