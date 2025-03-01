#模块import
import string
import random
#随机生成一个字符
s = ""
for char in range(5):
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
# print(all_chars)

    char = random.choice(all_chars)
    print(char)
    s += char
print(s)




