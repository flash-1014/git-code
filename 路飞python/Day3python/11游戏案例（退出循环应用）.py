from random import choice

while 1:
    print("""
    1.攻击
    2.购买装备
    """)
    choice = input("请输入您的选择：")
    #分支判断
    if choice == "1":
        print("攻击...")
    elif choice == "2":
        print("购买装备...")

    #引导用户做出选择
    choice2 = input("""
    1.回到第一关
    2.退出游戏
    3.继续下一关
    """)
    if choice2 == "1":
        continue
    elif choice2 == "2":
        break

   #第二关的选择
    print("进入第二关")
    choice3 = input("""
   1.前进
   2.查看地图
   3.回城
   """)
    if choice3 == "1":
        print("前进...")
    elif choice3 == "2":
        print("查看地图...")
    elif choice3 == "3":
        print("回城...")
    break

print("游戏结束！")