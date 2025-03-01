#unicode  万国码
#支持所有国家语言，但是比ASC||编码多一倍
#用utf-8，，在windows系统里面 在中国，编码默认为gbk

# 编写字符串：路飞学城，windows gbk
# 发送到mac上，mac正常显示，怎么办
#gbk--->utf-8

# 2种办法
# 1.直接转成unicode
# py3内存里所有字符全是Unicode，unicode是万国码

# 2.直接转成utf-8
# gbk--->unicode--->utf-8
# gbk-----unicode 的过程叫做解码   也就是Unicode为基础编码，基础到进阶为编码，转到基础为解码
# unicode----utf-8的过程2叫做编码
