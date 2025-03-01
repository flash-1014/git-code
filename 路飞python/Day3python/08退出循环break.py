#break退出整个循环
#continue 退出当次循环

# for i in range(1,11):
#     print(i)
#     if i == 6:
#         break
# print("process end")

#1.打印半径1m~100m的圆的面积 π*r**2
#2.半径为1~100m范围内找到第一个面积大于1000的半径值
for r in range(1,101):
    print("半径r:",r)
    #计算圆的面积
    S = 3.1415926*r**2#连续两个*为平方
    if S > 1000:
        print(f"半径为{r}的面积为{S}")
        break