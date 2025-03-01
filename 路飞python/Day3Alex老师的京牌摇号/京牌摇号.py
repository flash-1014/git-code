import random
import string


#构建随机字符

# #先确定京字后的一位大写的英文数字
# s1 = string.ascii_uppercase
# m = random.choice(s1)#sample(s1,1)
# print(m)
#
# s2 = string.ascii_uppercase + string.digits
# #随机选出后五位字符
# n = random.sample(s2,5)
# #将五个字符进行拼接为一串字符串，用到字符串函数n_str ="".join("a","b","c")
# n_str = "".join(n)
# print(n_str)
#
# #将京和s1和s2连接
# n_zone = "".join(["京",m+" ",n_str])
# print(n_zone)

#具体要求：1.允许用户最多选3次  2.每次放出20个车牌供用户选择 3.车牌号可以是字母与数字的组合

count = 0
while count < 3:
    car_nums = []  # 存储用户选择的号码，列表对元素进行存储
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits,5))
        car_num = f"京{n1}-{n2}"
        car_nums.append(car_num)#把生成的号码放入列表
        print(i+1,car_num)

    choice = input("输入你喜欢的号码：")
    if choice in car_num:
        print(f"恭喜你选择了新车牌号：{choice}")
        exit("Good luck")
    else:
        print("不合法的选择")

    count +=1
print("您的3次机会已结束")



