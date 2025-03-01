#计算1~100中所有的偶数和

# ret = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         ret += i
#     else :
#         pass
# print(ret)

#2.1~100所有能整除13的数字和
# pat = 0
# for i in range(1,101):
#     if i % 13 == 0:
#         print("i",i)
#         pat += i
#     else:
#         pass
# print(pat)

#3.无限循环嵌套分支语句
while 1:
    print("""
    1.前进
    2.攻击
    3.购买装备
    4.查看地图
    5.回城
    """)

    choice = input("请输入你的选择：")
    if choice == "1":
        print("前进...")
    elif choice == "2":
        print("攻击...")
    elif choice == "3":
        print("购买装备...")
    elif choice == "4":
        print("查看地图...")
    elif choice == "5":
        print("回城...")