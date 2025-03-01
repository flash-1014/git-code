#导入字符串和随机数的模块
import random
import string

#3次机会，每次生成20个车牌
count = 0
while count<3:
    #对于20个数据在后面对用户选择号码进行核对时，需要建立一个容器存储，这里采用列表
    num_str = []
    for i in range(20):
        #首先生成省会缩写后一位数字，再生成后4位数字 单个字符用choice函数，多个字符用sample函数
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits,4))
        #print("京"+n1+"-"+n2)

        num = f"京{n1}-{n2}"
        print(i+1,num)
        #在列表扩充添加函数：[].append(元素)
        num_str.append(num)

        #用户开始输入，根据输入与列表中数据进行判断
    num_choice = input("请输入您选择的车牌号：")
    #把字符串与列表中字符串进行对比的函数 “in” num_str
    if num_choice in num_str:
        print(f"恭喜您选择了车牌号：{num_choice}")
        exit("Good luck!")
    else:
        print("不合法的选择,请您再次选择")

    count +=1
print("您的3次机会已使用完毕，请下次再选择车牌号")
