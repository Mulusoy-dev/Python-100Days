import xlrd




file="measurement.xlsx"

inputWorkbook=xlrd.open_workbook(file)
print("The number of worksheets is {0}".format(inputWorkbook.nsheets))
print("Worksheet name(s): {0}".format(inputWorkbook.sheet_names()))


sh = inputWorkbook.sheet_by_index(0)
inputWorksheet=inputWorkbook.sh


print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))




# file=open('new.txt','r',encoding='utf-8')

# content=file.read()

# print(content)

# for i in file:
#     print(i)






