f = open("嫩模联系方式",encoding='utf-8')

for line in f:#每一行读一次
    line = line.split()
    #print(line)
    high = int(line[3])
    weight  = int(line[4])
    if high >= 170 and weight <= 50:
        print(line)


    #print(line,end='')