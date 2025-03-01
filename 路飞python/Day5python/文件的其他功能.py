# seek  tell flush
#seek直接回到光标位置，立即覆盖内容
#tell 返回光标当前位置，直接可以到光标位置，内容也是位置信息
#flush 将内存数据强制直接保存到硬盘，针对与断电时的保护操作，但是没什么卵用，现在大致都有自我数据保护

f = open('seek_write.txt','w')
f.write("hellllllllo1\n")
print(f.tell())
f.write("hellllllllo2\n")
print(f.tell())
f.write("hellllllllo3\n")
f.seek(11)

print(f.tell())

#f.write("+______")