#主要是函数的编写
#对于用户学员输入信息
#文件操作
db_file = "student.txt"

def register():
    #存储数据
    stu_data = {}
    print("欢迎来到湖南工程学院".center(50,"-"))
    print("请完成学籍注册")
    name = input("姓名：".strip())#strip()去掉前后空格
    age = input("年龄：".strip())
    #可以对手机号和身份证号进行限制，手机号必须是数字，手机号的位数，等等
    #这个简单程序有个问题，如果进行判断的话，判断为错的话直接跳出了，需要重新将所有信息进行输入，我觉得加循环可以解决这个问题但是会很繁琐，输入的东西多了之后就需要用到函数，但是语句较少也不大行
    phone = input("手机号：".strip())
    if phone in phone_list:
        exit("该手机已注册")
    if not phone.isdigit():
        print("您输入的不全是数字，请重新输入！")
        #return register() #神之一手
        #exit()
        #直接重新调用函数
        phone = input("手机号：".strip())
    if len(phone) != 11:
        print("您输入的手机号不满11位，请重新输入!")
        #exit()
        phone = input("手机号：".strip())
    number = input("身份证号：".strip())
    if number in number_list:
        exit("该身份证号已注册")
    #重点return直接返回
    #return name,age,phone,number
    #课程选择：
    print("请选择你的课程："
          "1.python全栈 "
          "2.linux云计算 "
          "3.网络安全 "
          "4.前端 "
          "5.数据分析 ")

    choice_str = input("请输入你的选择:").strip()  # 使用input()获取用户输入，并去除首尾空白
    while True:  # 使用True作为循环条件，确保循环持续进行
        try:
            choice = int(choice_str)  # 尝试将输入转换为整数
        except ValueError:  # 如果转换失败（即用户输入的不是数字）
            print("输入无效，请输入1至5之间的数字。")
            choice_str = input("请输入你的选择:").strip()  # 重新输入
            continue  # 跳过剩余循环体，重新开始循环

        # 使用if-elif-else结构简化逻辑
        if choice == 1:
            print("恭喜你选择了python全栈课程！")
            break  # 退出循环
        elif choice == 2:
            print("恭喜你选择了Linux云计算课程！")
            break
        elif choice == 3:
            print("恭喜你选择了网络安全课程！")
            break
        elif choice == 4:
            print("恭喜你选择了无就业前景的前端课程！")  # 注意这里的描述可能需要调整以更正面地引导用户
            break
        elif choice == 5:
            print("恭喜你选择了数据分析课程！")
            break
        else:
            print("输入超出范围，请输入1至5之间的数字。")
            choice_str = input("请输入你的选择:").strip()  # 输入不合法，重新输入
#存储数据到文件中
    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["phone"] = phone
    stu_data["number"] = number
    return stu_data
    #stu_data["course"] = course  课程的选择用列表方便一些
    # course_list  = ["Python全栈","Linux云计算","网络安全","前端","数据分析"]
    # for index,course in enumerate(course_list):
    #     print(f"{index+1}.{course}")
def commit(filename,stu_data):
    f = open(filename,"a",encoding="utf-8")
    #将数据以字典一行表示
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['number']}\n"
    f.write(row)
    f.close()

#对于检查文件中数据的唯一性的函数
def invalid_data(filename):
    f  = open(filename8)
    phone_list = []
    number_list = []
    for line in f:
        line = line.split(",")
        phone = line[2]
        number = line[3]
        phone_list.append(phone)
        number_list.append(number)

        return phone_list,number_list

phone_list,number_list = invalid_data(db_file)
#调用函数
student_data = register()
print(student_data)
commit(db_file,student_data)