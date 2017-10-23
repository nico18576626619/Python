# 简单的字面替换使用replace,将yeah换成hi
text='yeah,but no,but yeah,but no,but yeah'
print(text.replace('yeah', 'hi'))

import re
# 复杂模式,如将11/27/2010换成 2010-11-27,用过sub函数来完成
text='Today is 11/27/2010,Pyconstarts 3/12/2013'
print(re.sub(r'(\d*)/(\d*)/(\d*)', r'\3-\1-\2',text))

# 预编译方式，subn可以返回替换的次数
x=re.compile(r'(\d+)/(\d+)/(\d+)')
print(x.subn(r'\3-\1-\2', text))


# 通过回调函数来实现,此回调函数的参数是match对象

from calendar import month_abbr
def change_date(m):
    mon_name=month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))


print(x.sub(change_date, text))



