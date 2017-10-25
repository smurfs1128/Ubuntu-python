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

class BlogInfo:
    """TFS  i-soft  Test Department Blog."""
    
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
        return self.count,self.title,self.blogtype,self.original,self.author,self.releasedate
           
def main():
    try:
        inputdate = sys.argv[1]      #运行脚本时传递的参数
    except Exception as e:
        print ('请输入参数，例如：')
        print ('查询9月份的文章请输入：python blog.py 201709')
        exit() 
    user = {5:'黄  俊',7:'李小双',8:'赵盼盼',10:'刘  珂',11:'刘  辉',12:'刘春媛', 13:'路  斐',14:'梁  凯',\
    15:'李兴峰',16:'刘  璐',17:'姚翔川',18:'刘  畅',19:'刘  杨',20:'赵丽丽',21:'迟建平'}
    for i in user.keys():
        userPaper =BlogInfo(i,inputdate) 
        print(userPaper.info()) 
 
        
if __name__ == '__main__':
    main()