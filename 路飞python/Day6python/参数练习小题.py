#元组传参
def print_info(*args):
    print("--------info---------")
    print("name:",args[0])
    print("age:",args[1])
    print("Sex:",args[2])
    print("hobbie:",args[3])


print_info("alex",18,"M","大保健")

#字典传参
def print_info(**kwargs):
    print("--------info---------")
    print("name:",kwargs.get("name"))
    print("age:",kwargs.get("age"))
    print("sex:",kwargs.get("sex"))
    print("hobbie:",kwargs.get("hobbie"))

print_info(name ="Jack",age=26,sex="M",hobbie="学习")