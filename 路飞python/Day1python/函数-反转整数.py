#-123翻转为-321，函数完成
def reverse(value):
    if value>-10 and value<10:
        print(value)
    str_value = str(value)
    if str_value[0]!= "-":
        re = int(str_value[::-1])
    else:
        re = -int(str_value[1::][::-1])
    return re
print(reverse(-1257))