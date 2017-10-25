import re
text1='Computer says "no"'
str_pat=re.compile(r'\"(.*)\"')
print(str_pat.findall(text1))
text1='Computer says "no",Phone says "yes"'

str_pat=re.compile(r'\"(.*?)\"')
print(str_pat.findall(text1))

print(str_pat.search(text1).group(1))
