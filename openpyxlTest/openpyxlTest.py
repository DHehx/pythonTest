#操作xlsx
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet1')
sheetActive = wb.get_active_sheet()
print(sheetActive['A1'].value)
A1 = sheetActive['A1']
print(A1.column)
print(A1.coordinate)