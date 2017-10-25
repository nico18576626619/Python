# 删除不需要的字符
str=' hello world '
# 删除两边空格
print(str.strip())
# 删除左边空格
print(str.lstrip())
# 删除右边空格
print(str.rstrip())


# 删除其他字符
str2='=======hello====='
# 删除两边的等号
print(str2.strip('='))
# 删除左边等号
print(str2.lstrip('='))
# 删除右边等号
print(str2.rstrip('='))


# 删除中间空格
str3='hello     world'
print(str3.replace(' ',''))
import re
x=re.compile('\s+')
print(x.sub('', str3))

# 读取并打印多行数据
file=open('1.txt','r')
# for i in file:
#     print(i.strip())

# print(file.readlines())
with open('1.txt','r') as  f:
    for line in(i.strip() for i in f):
        print(line)