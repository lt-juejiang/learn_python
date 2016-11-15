#!/user/bin/python
#coding=utf-8

# class Screen(object):
#
#     def __init__(self, width=2880, height=1800):
#         self.width = width
#         self.height = height
# screen1 = Screen()
# screen2 = Screen(1080)
# screen3 = Screen(1400, 900)
# screen4 = Screen(height=2100)

class Screen(object):

    def __init__(self, **kw):
        self.width = kw.get('width', 2880)#设置默认参数
        self.height = kw.get('height', 1800)
screen1 = Screen()
screen2 = Screen(width=1080)
screen3 = Screen(width=1400, height=900)
screen4 = Screen(height=2100)


print('screen1: %d * %d' % (screen1.width, screen1.height))
print('screen2: %d * %d' % (screen2.width, screen2.height))
print('screen3: %d * %d' % (screen3.width, screen3.height))
print('screen4: %d * %d' % (screen4.width, screen4.height))


