#!/usr/bin/env python

# Copyright (C) 2005 Kiseliov Roman

from xlwt import *

wb = Workbook()
ws0 = wb.add_sheet('sheet1')

#定义了每列的列宽
ws0.col(0).width = 0xBFF
ws0.col(1).width = 0x3FFF
ws0.col(2).width = 0xCFF
ws0.col(3).width = 0xCFF
ws0.col(4).width = 0xCFF
ws0.col(5).width = 0xCFF

#定义了第一行合并单元格的字体
fnt = Font()
fnt.name = 'Times New Roman'
fnt.height=400
fnt.bold = True

#定义了第二行标题的字体
fnt1 = Font()
fnt1.name = 'Times New Roman'
fnt1.height=220
fnt1.bold = True

#定义了正文的字体
fnt2 = Font()
fnt2.name = 'Times New Roman'
fnt2.height=220
fnt2.bold = False

#定义了字体的外边界的边框
borders = Borders()
borders.left = 1
borders.right = 1
borders.top = 0
borders.bottom = 1

#设置字体居中
al = Alignment()
al.horz = Alignment.HORZ_CENTER
al.vert = Alignment.VERT_CENTER

#第一行合并单元格字体的所有格式，包括字体大小、边框、居中
style = XFStyle()
style.font = fnt
style.borders = borders
style.alignment = al

#第二行标题的所有格式，包括字体大小、边框、居中
style1 = XFStyle()
style1.font = fnt1
style1.borders = borders
style1.alignment = al

#正文的所有格式，包括字体大小、边框、居中
style2 = XFStyle()
style2.font = fnt2
style2.borders = borders
style2.alignment = al

#合并单元格的操作，并输入具体内容
ws0.write_merge(0, 0, 0, 5, '201709月份文章列表', style)

#标题栏的操作
ws0.write(1,0,'序号',style1)
ws0.write(1,1,'文章title',style1)
ws0.write(1,2,'文章类型',style1)
ws0.write(1,3,'文章归档',style1)
ws0.write(1,4,'作者',style1)
ws0.write(1,5,'发布日期',style1)

#正文操作
for i in range(2,0x53):
    ws0.write(i,0,i-1,style2)

wb.save('merged.xls')