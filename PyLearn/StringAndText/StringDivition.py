# 字符使用多个界定符分割字段


#1、单一界定符,以空格切分
import re

line='hello world'
l=line.split(' ')
print(l)


#2、多个界定符分割,通过re.split()来进行分割
line='asdf fjdk; afed,jsjj,foo'
l=re.split('[;,\s]\s*',line)
print(l)