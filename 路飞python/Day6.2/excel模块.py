#pip install openpyxl
from openpyxl import load_workbook
#实例化
wb = load_workbook( )
#获取当前激活的sheet
ws = wb.active
# print(sheet.title)