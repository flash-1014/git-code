#三元运算
#合并两部字典.键值对的形式
a = {"A": 1, "B": 2, }
b = {"C": 3, "D": 4, }
# 字典的附加就是update方法更新,
a.update(b)
print(a)
#如果有重复的键值对，会直接更新新的键值
a = {"A": 1, "B": 2, }
b = {"B": 3, "D": 4, }
a.update(b)
print(a)

#python的三元运算表达式，没有标准的三目运算符：A？B：C(x x>y else y)
x = 100
y = 120
print(x if x>y else y)

#判断偶数奇数
b =23
print("偶数" if b%2 == 0 else "奇数")