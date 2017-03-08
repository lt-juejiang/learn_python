#!/user/bin/python
#coding=utf-8

import os
def dirlist():
    if input('请输入你的命令： \n') == 'dir -l':
        for x in os.listdir('.'):
            if os.path.isfile(x):
                print(os.path.join(os.path.abspath('.'),x+'\n'))
    else:
        print('输入命令错误！')



def find(str_name , path_x):
    for x in os.listdir(path_x):
        path_y = os.path.join(path_x, x)
        if os.path.isfile(path_y) and str_name in os.path.split(path_y)[1]:
            print(path_y)
        elif os.path.isdir(path_y):
            find(str_name,path_y)
if __name__ == '__main__':
    find("Fun", ".")