#300名员工进行抽奖，分别有三种奖，规则是抽3个阶段，先把3等奖数量抽完，再二等奖，最后一等奖，每个人只能中奖一次
#应该是需要把中奖的编号分别列出，就是最后的结果了
#[1~300]的一个列表，需要一个把元素从列表中剔除的函数，更新列表，随机的范围是1~300
import random

#三个奖项也要随着改变，设定初始值
n1 = 3
n2 = 6
n3 = 30
#1~300的列表 range函数
num_str = list(range(1,301))#list直接将range类型强行转换为列表类型
coun =0#初始化计数器
#循环主体
while coun< n1 + n2 + n3:
    if coun<n3:
        for _ in range(n3-coun):
            num = random.randint(1, 300)  # 随机1~300的一个数
            if num in num_str:
                print(f"恭喜获得三等奖！{num}号")
                num_str.remove(num)
                #print(num_str)
                coun +=1
                break
            else:
                continue

    if coun< n2 + n3:
        for _ in range(n2-(coun-n3)):
            num = random.randint(1, 300)  # 随机1~300的一个数
            if num in num_str:
                 print(f"恭喜获得二等奖！{num}号")
                 num_str.remove(num)
                 coun +=1
                 break
            else:
                continue
    if coun<n1+n2+n3:
        for _ in range(n1-(coun-n2-n3)):
            num = random.randint(1, 300)  # 随机1~300的一个数
            if num in num_str:
                 print(f"恭喜获得一等奖！{num}号")
                 num_str.remove(num)
                 coun +=1
                 break
            else:
                continue
    if coun >= n1+n2+n3:
       break
