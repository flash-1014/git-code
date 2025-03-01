#身份证各数判断
pid = input("请输入你的身份证号：")


#判断身份证号是否是18位
if len(pid)==18:
    print("打印个人基本信息")
    #打印性别，身份证号倒数第二位为奇数为男生，为偶数即女生
    num = int (pid[16])
    if num % 2==0:
        print("性别：女性")
    else:
        print("性别：男性")
    #打印籍贯
    jiguancode = pid[0:6]
    print("jiguancode",jiguancode)
    if jiguancode == "100000":
        print("籍贯：北京市")
    elif jiguancode == "110000":
        print("籍贯：重庆市")
    elif jiguancode == "120000":
        print("籍贯：芜湖市")
    elif jiguancode == "130000":
        print("籍贯：兰州市")
    else:
        print("不是直辖市")




else:
    print("输入身份证号位数错误！")
print("程序结束")