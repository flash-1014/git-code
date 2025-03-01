#1,2，3,4,5能组成多少个互不相同且不重复的三位数字
l = [1,2,3,4,5]
new_l = []
# for i in l:
#     for j in l:
#         for k in l:
#             if i !=j and i!=k and j!=k:
#                 new_l.append(int(str(i)+str(j)+str(k)))
#
# print(new_l)
#直接推导式
new_l = [int(str(i)+str(j)+str(k)) for i in l for j in l for k in l if i !=j and i!=k and j!=k]
print(new_l)