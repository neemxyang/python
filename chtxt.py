# _8_ coding:utf-8 _8_

import pandas as pd
from pandas import DataFrame
from openpyxl import Load_workbook
a = []
with open("c:\\Users\\Administrator\\chocolist.txt", "r") as f:
    data = f.readlines()
    for l in data:
        b = l.split("[",2)
        c = b[0].split(" ",2)
        a.append([c[0],c[1]])
    # a.append(data)

d = DataFrame(a)
print(d)

d.to_excel('choco4.xlsx',index=False,header=1)


fd = 'd:\\gitdir\\choco4.xlsx'
workb = Load_workbook(fd)
ws = wb['Sheet1']
ws["A1"] = 'Softwar Name'
ws["B1"] = "Version"
wb.save('choco5.xlsx')