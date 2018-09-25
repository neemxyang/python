# -*- coding:utf-8 -*-
import xlwt
# workbook = xlwt.Workbook(encoding = 'utf-8')
# #初始化数据
# cc=[15000,10000,5000,200]
# ym=[]
# #定义变量，给变量赋值
# str1=["银幕最大画面为","宽银幕","遮幅银幕","画面尺寸为","订购银幕尺寸","订购银幕面积"]
# tcd = cc[0]
# tkd = cc[1]
# tgd = cc[2]
# mdq = cc[3]
# #计算数据
# ymkd = tkd - 2 * mdq
# ymgd = ymkd / 1.85
# # 开始循环
# if ymgd + 1200 >= tgd: #如果高度不够
#     print (str1[0] +":" + str1[2])
#     ymgd = ymkd / 2.35
#     ymgd = int(ymgd)
#     print (str1[1] + str1[3] + " ："+ str(ymkd) +" 毫米 x" + str(ymgd) + " 毫米")
#     zymkd = int(ymgd * 1.85)
#     print(str1[2] + str1[3] + " ：" + str(zymkd) + " 毫米 x" + str(ymgd) + " 毫米")
#     dymkd = ymkd +300
#     dymgd = ymgd + 300
#     print(str1[4]  + " ：" + str(dymkd) + " 毫米 x" + str(dymgd) + " 毫米")
#     dymmj = dymkd * dymgd
#     dymmj = round(dymmj / 1000000,2)
#     print (str1[5] + " : " + str(dymmj) + "平方米")
#
#     ymkd = int(ymgd *2.35)
#     mdq = (tkd - ymkd) / 2
#     cc[3] =mdq
#     ym.append(ymkd)
#     ym.append(ymgd)
#     ym.append(zymkd)
#     ym.append(ymgd)
#     ym.append(dymkd)
#     ym.append(dymgd)
#     ym.append(dymmj)
#     print(ym)
# else:                   #如果高度足够
#     print (int(ymgd))
#
#
#
# worksheet = workbook.add_sheet('基础数据')
# bt=["项目","数值","单位"]
# for i in range(3):
#     worksheet.write(0,i,label = bt[i])
# tt=["厅长","厅宽","厅高","幕到墙"]
#
# for j in range(4):
#     worksheet.write(j+1,0,label = tt[j])
# for i in range(len(cc)):
#     worksheet.write(i+1,1, label = cc[i])
#
# worksheet = workbook.add_sheet('银幕数据')
# tt = ["宽银幕画面宽度","宽银幕画面高度","遮幅画面宽度","遮幅画面高度","订购银幕宽度","订购银幕高度","订购银幕面积"]
# for i in range(3):
#     worksheet.write(0,i,label = bt[i])
# for j in range(7):
#     worksheet.write(j+1,0,label = tt[j])
# for i in range(len(ym)):
#     worksheet.write(i+1,1, label = ym[i])
#
# workbook.save('d:\\Excel_test.xls')

def count_screen(width,high):
    global screen
    screen=[]
    sc_w = width - 2*200
    ss_r = 2.39
    sf_r = 1.85
    sc_d = 800
    sc_u = 100
    ha_h = high - sc_d - sc_u
    sc_fh = sc_w / sf_r
    sc_sh = sc_w / ss_r
    if sc_fh <= ha_h: #厅足够高 最大画面：遮幅画面
        sc_sw = sc_w
        sc_fw = sc_w
        sc_bw = sc_w
        screen.append("情况1 厅够高")
        screen.append(sc_bw)
        screen.append(sc_fh)
        screen.append(sc_bw)
        screen.append(sc_sh)
    elif sc_sh <= ha_h & ha_h < sc_fh: #厅高度适中，宽银幕最大 宽度满足
        sc_sw = sc_w
        sc_fh = sc_sh
        sc_fw = sc_fh * sf_r
        sc_bw = sc_sw
        screen.append("情况2 厅刚好")
        screen.append(sc_bw)
        screen.append(sc_sh)
        screen.append(sc_fw)
        screen.append(sc_fh)

    else: #厅太矮了 只能按高度来
        sc_sh = ha_h
        sc_sw = sc_sh * ss_r
        sc_fh = ha_h
        sc_fw = sc_fh * sf_r
        sc_bw = sc_sw
        screen.append("情况3 厅太矮")
        screen.append(sc_bw)
        screen.append(sc_sh)
        screen.append(sc_fw)
        screen.append(sc_fh)

    print(screen)

count_screen(8050,4500)

def count_stair(length,width,high):
    count_screen(width,high)
    sc_bw = 800+300
    fs_ratio = 0.6
    sc_fs = screen[1] * fs_ratio
    fs_mid = 1500
    fs_end = 1400
    fs_width = 1200
    n = (length - sc_bw - sc_fs - fs_mid - fs_end) // fs_width
    m = (length - sc_bw - sc_fs - fs_mid - fs_end) % fs_width
    fs_cz = fs_width - m
    bl = screen[1]*0.1
    if fs_cz < bl :
        n = n + 1
        sc_fs = sc_fs - fs_width + m
        print ("情况1")
        print (n + 2)
        print (m)
        print (sc_fs)
    else:
        n=n
        print ("情况2")
        print (n+2)
        print (m)
        print(sc_fs)

count_stair(14300,9050,6000)