from idlelib.iomenu import encoding
#图片转二进制模式打开，不涉及编码
#将图片转二进制编码  rb

f = open('夏日重现.png',"rb")

for line in f:
    print(line)

#encoding = None#告诉解释器默认编码为None


#写二进制，编码为wb
f = open("wb_file","wb")

s = "路飞"
f.write(s.encode("utf-8"))