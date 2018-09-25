# coding:utf-8

import xlwt
file = xlwt.Workbook()
table = file.add_sheet("报价表")

tt = ["编码","品名","品牌","型号","数量","单价","总价","备注"]
for i in range(len(tt)):
    table.write(1,i,tt[i])

sb = ["音频解码器","主声道音箱","次低频音箱","环绕声音箱","环绕箱支架","功率放大器","机柜","接插件","安装费","汇总","  "]
for i in range(3):
    for j in range(len(sb)-1):
        a =  2+j + len(sb)*i
        table.write(a,0,str(i+1) +"."+str(j+1))
        table.write(a,1,sb[j])
        table.write(a,2,"NEEMX")
file.save('d:\\test1.xlsx')

