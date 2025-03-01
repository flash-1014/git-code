d = {"a":1,"b":2}#键值对的方式
new_d ={}#字典的键值需要两个接受
# #实现小写字符串变成大写字符串a-A
# for k,v  in d.items() :
#     new_d[k.upper()] = v#键与值直接等于 =
#字典推导式:{键表达式:值的表达式 for k v in d.items()
print({k.upper():v for k,v in d.items()})
#将一个字典键值对互换
print({v:k  for k,v in d.items()})
#面试题：统计一串字符中出现字符的个数，比如abbbabbabbaca
s = "abababcababbac"
print({char:s.count(char) for char in s})
d = {}
for a in s :
    d[a]  = d.get(a,0)+1
print(d)
