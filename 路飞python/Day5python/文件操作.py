#增删改查：
#打开文件：f = open(filename)

#首先创建一个文件
f = open('name_list.txt', mode ='w')
f.write("永劫无间英雄")
f.write("天海")
f.write("顾清寒")
f.write("妖刀姬")

f.close()

