import os

# 检查字符串开头和结尾startwith(),endwith()
url='https://www.baidu.com'
print(url.startswith('https:'))
print(url.endswith('.com'))

# 注意如果判断的条件是多种的话一定要传元组否则报错,通过tuple()进行转换
list=['.iml','.xml']
sets=set()
sets.add('.iml')
sets.add('.xml')

filenames=os.listdir('../.idea')
# 提取.iml或.xml结尾的文件
file=[item for item in filenames if item.endswith(tuple(sets))]
print(file)



