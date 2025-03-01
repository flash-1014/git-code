#(5) isdigit 判断字符串是否是纯数字
# numstr = input("请输入一个数字")
#
# #先判断numstr是否是一个纯数字
# print(numstr.isdigit())
#
# if numstr.isdigit():
#     numstr = int(numstr)
#     print(numstr*2)
# else:
#     print("numstr不是一个纯数字，请重新输入")


#(6)strip 去除字符串两端的空格或换行符
user = input("请输入用户名：")
user = user.strip()
print(user,len(user))
