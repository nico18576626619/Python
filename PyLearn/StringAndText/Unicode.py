s1='Jalape\u00f1o'
s2='Jalapen\u0303o'
print(s1)
print(s2)
print(s1==s2)
# 使用unicodedata模块将文本标准化
import unicodedata
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
print(t1==t2)
print(t1)
print(t2)