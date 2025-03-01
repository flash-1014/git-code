
# with open('顺丰地址数据.txt','r') as file:
#     data = [line.strip() for line in file]
#     print(data)w


#抛出测试检验是否出现了找不到和没有权限问题


# try:
#     # 假设路径正确且权限问题已解决，这里直接使用原路径
#     with open(r'D:\MypythonCode\路飞python\Day4顺丰快递分拣小程序\顺丰地址数据.txt', 'r', encoding='utf-8') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("文件未找到，请检查路径是否正确。")
# except PermissionError:
#     print("权限被拒绝，请确保有足够权限访问该文件。")
# except Exception as e:
#     print(f"读取文件时发生未知错误：{e}")


#正常读取文件,,,,,'r','t'表示对文件的读取方式
with open(r'D:\MypythonCode\路飞python\Day4顺丰快递分拣小程序\顺丰地址数据.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)


