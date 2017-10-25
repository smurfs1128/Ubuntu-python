# !/usr/bin/python

# Python:   3.5.1
# Platform: Windows
# Author:   Heyn (heyunhuan@gmail.com)
# Program:  China Merchants Bank.
# History:  2016/11/10 V1.0.0[Heyn]
#           2017/10/10 V1.0.1[Heyn] Add itchat

# (1) Limit all lines to a maximum of 79 characters
# (2) Private attrs use [__private_attrs]
# (3) [PyLint Message: See web: http://pylint-messages.wikidot.com/]


import re
import sys
import requests

from xlwt import *

class BlogInfo:
    """TFS  i-soft  Test Department Blog."""

    num = 0
    def __init__(self,userid,inputdate):
        super(BlogInfo, self).__init__()
        self.userid = userid
        self.inputdate = inputdate
        self.count = 0
        self.html = self.title = self.blogtype = self.original = self.author = self.releasedate = []
     
    def loadurl(self):
        """Loading"""
        url = 'http://tfs.i-soft.com.cn/blog'
        try:
            payload = {'author':self.userid,'m':self.inputdate}
            self.html = requests.get(url,params=payload).text
        except BaseException:
            return False
        return True
                 
    def info(self):
        """blog info"""
        if self.loadurl() is False:
            return ''
        self.title = re.findall(r'"bookmark">(.*)</a></h2>',self.html)   #title是list
        self.blogtype = re.findall(r'"category">(.+?)</a>',self.html)    #blogtype是list，too
        self.releasedate = re.findall(r'"entry-date">(.+?)</span>',self.html) #release也是list
        self.author = re.findall(r'发布的文章">(.*)</a></span>',self.html)
        for i in range(len(self.title)):
            self.count += 1
            if '转载' in self.title[i] :
                self.original.append('转载')
            else:
                self.original.append('原创')
        BlogInfo.num += self.count 
        return self.count,self.title,self.blogtype,self.original,self.author,self.releasedate

def settingmerged():
    """ Set meraged. """
    #定义了第一行合并单元格的字体
    fnt = Font()
    fnt.name = 'Times New Roman'
    fnt.height=400
    fnt.bold = True

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
    return style

def settingtitle():
    """ Set meraged. """
    #定义了第二行标题的字体
    fnt1 = Font()
    fnt1.name = 'Times New Roman'
    fnt1.height=220
    fnt1.bold = True

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

    #第二行标题的所有格式，包括字体大小、边框、居中
    style1 = XFStyle()
    style1.font = fnt1
    style1.borders = borders
    style1.alignment = al
    return style1

def settingcontent():
    """ Set meraged. """
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

    #正文的所有格式，包括字体大小、边框、居中
    style2 = XFStyle()
    style2.font = fnt2
    style2.borders = borders
    style2.alignment = al
    return style2
           
def main():
    try:
        inputdate = sys.argv[1]      #运行脚本时传递的参数
    except Exception as e:
        print ('请输入参数，例如：')
        print ('查询9月份的文章请输入：python blog.py 201709')
        exit() 
    
    wb = Workbook()
    ws0 = wb.add_sheet('%s月份文章'%inputdate)

    #定义了每列的列宽
    ws0.col(0).width = 0xBFF
    ws0.col(1).width = 0x3FFF
    ws0.col(2).width = 0xCFF
    ws0.col(3).width = 0xCFF
    ws0.col(4).width = 0xCFF
    ws0.col(5).width = 0x17FF

    #合并单元格的操作，并输入具体内容
    ws0.write_merge(0, 0, 0, 5, '%s月份文章列表'%inputdate, settingmerged())

    #标题栏的操作
    ws0.write(1,0,'序号',settingtitle())
    ws0.write(1,1,'文章title',settingtitle())
    ws0.write(1,2,'文章类型',settingtitle())
    ws0.write(1,3,'文章归档',settingtitle())
    ws0.write(1,4,'作者',settingtitle())
    ws0.write(1,5,'发布日期',settingtitle())

    #正文操作
    #for i in range(2,0x53):
     #   ws0.write(i,0,i-1,style2)

     #ws0.write(2,i,userPaper.info(),settingcontent())



    '''user = {5:'黄  俊',7:'李小双',8:'赵盼盼',10:'刘  珂',11:'刘  辉',12:'刘春媛', 13:'路  斐',14:'梁  凯',\
        15:'李兴峰',16:'刘  璐',17:'姚翔川',18:'刘  畅',19:'刘  杨',20:'赵丽丽',21:'迟建平'}'''
    for i in range(2,22):
        userPaper =BlogInfo(i,inputdate)
        userPaper.info()
        print (userPaper.title,userPaper.blogtype,userPaper.original,userPaper.author,userPaper.releasedate)
       
        ws0.write(i,1,userPaper.title,settingcontent())
        ws0.write(i,2,userPaper.blogtype,settingcontent())
        ws0.write(i,3,userPaper.original,settingcontent())
        ws0.write(i,4,userPaper.author,settingcontent())
        ws0.write(i,5,userPaper.releasedate,settingcontent())
        


    wb.save('普华测试技术分享平台%s月份文章列表统计.xls'%inputdate)
    
            
if __name__ == '__main__':
    main()