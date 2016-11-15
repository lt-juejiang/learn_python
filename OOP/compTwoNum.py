#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Com(object):
#
#     def __init__(self):
#         self.n1=float(input('输入一个数字：'))
#         self.n2=float(input('再输入一个数字：'))
#
#     def compa(self):
#         if self.n1>self.n2:
#             return str(self.n1)+'大于'+str(self.n2)
#         elif self.n1==self.n2:
#             return str(self.n1)+'等于'+str(self.n2)
#         else:
#             return str(self.n1)+'小于'+str(self.n2)
#
#
# x=Com()
# print('第一个数字:''%s' % (x.n1)+'\n''第二个数字：''%s' % (x.n2))
# print(x.compa())

class Com:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def compa(self):
        if self.num1 > self.num2:
            return str(self.num1)+'>'+str(self.num2)
        elif self.num1 == self.num2:
            return str(self.num1)+'='+str(self.num2)
        else:
            return str(self.num1)+'<'+str(self.num2)

M0=input('input a num:')
M1=input('input a num again:')

print('first num:%s' % M0+'\n'+'two num:%s' % M1)
print '*******************'
x=Com(M0,M1)
print(x.compa())