# 字符使用多个界定符分割字段


# 1、单一界定符,以空格切分
import re

line = 'hello world'
l = line.split(' ')
print(l)

# 2、多个界定符分割,通过re.split()来进行分割
line = 'asdf fjdk; afed,jsjj,foo,ziooi'
print(line)
l = re.split('[;,\s]\s*', line)
print(l)

# 3、通过re.split()来进行分割,但保留分隔符，通过()来提取匹配的字符串
line = 'asdf fjdk; afed,jsjj,foo,zoo'
l = re.split('(;|,|\s)\s*', line)
print(l)

# 4、(),[]区别
lin = 'abc'
print(re.split('[b]', lin))
print(re.split('(b)', lin))

# 提取有用信息和分割符号
values=l[::2]
print(values)
delimiter=l[1::2]+['']
print(delimiter)
print('拼装:',''.join(v + d for v, d in zip(values, delimiter)))

# 5、使用()来分组，但分组非捕获分组用(?:...)
line = 'asdf fjdk; afed,jsjj,foo,zoo'
l = re.split('(?:;|,|\s)\s*', line)
print(l)
