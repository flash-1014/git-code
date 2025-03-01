#1.确定  在文件中存储的账号信息结构


#2。将账号数据读到内存，为了方便调用，可以改为list
#但是查找列表需要循环，容易出现查找循环次数过多情况，可以用字典来处理


# account = {
#     "alex":["alex","111111","1"]
# }
# f = open("account.txt","r")
# for line in f:
#     strip(",")这里没有用好，本来是为了对于文本信息中一行中的数据以逗号进行分割每一行，但是这个account的字典的添加部分需要是每一行信息中的一部分，没有设好
#     因为尝试将整个字符串（而不是预期的用户名、密码等元素）作为值赋给字典。
#     line = line.strip(",")
#     account[line[0]] = line

account = {
    "alex": ["alex", "111111", "1"]
}

with open("account.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")  # 去除行尾换行符并按逗号分割
        if len(parts) >= 3:  # 确保至少有三项（用户名、密码、状态）
            username, password, status = parts[:3]  # 解包前三项
            account[username] = [username, password, status]  # 正确地将信息存入字典

print(account)
#循环：loop 搞个loop，要求用户输入账号信息，去判断即可
count = 0
while count <=3:
    user = input("username:").strip()
    password = None
    if user in account:
        print("该用户存在，请输入密码：")
        password = input("密码为：").strip()
    else:
        print("该用户未注册")
        continue

    #然后判断在账号dict文本里面判断密码是否正确
    if password == account[user][1]:
        print(f"Welcome {user}...登录成功...")
        break
    else:
        print("Wrong password....")

    count += 1