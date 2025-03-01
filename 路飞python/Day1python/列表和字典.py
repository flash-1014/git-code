#列表：数组的按序查找
#字典：哈希：键值对查找，一般来说字典更快
#但数锯多少有影响：数据较少：列表更快，多则字典更快

#列表字典推导式
#一般推导新列表,例如新列表元素的平方
# 案例一：平方
# l =[1,2,3,4,5]
# new_l = []
# for i in l:
#     new_l.append(i*i)
# print(new_l)
#案例二：筛选偶数
# new_2l = []
# for i in l :
#     if i%2 == 0:
#         new_2l.append(i)
# print(new_2l)
#列表推导式 [表达式 for i in l]
# print([i for i in l])
# print([i*i  for i in l])
# print([i  for i in l if i%2==0])
#面试题：如何实现['1','2','3']变成[1,2,3]
l = ['1','2','3']
l2 = [1,2,3]
#字符串转成整型 int（i）
print([int(i) for i in l] )
#获取所有1-100中所有偶数平方的列表
print([i*i for i in range(1,100) if i%2==0])#for循环range函数
#进阶玩法：列表嵌套 变成只有一个外壳的列表 l = [1,2,3,4,5,6]
l = [[1,2],[3,4],[5,6]]
print([ j for i in l for j in i])
#字典
