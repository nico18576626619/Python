# 忽略大小写替换
# 完全忽略
import re
text='Yeah,but no,but YEAH,but no,but yeah'
print(re.sub('yeah','boot', text, flags=re.IGNORECASE))



# 根据替换的字符大小写规则来替换,比如替换的字符串为大写，替换的字符也为大写，替换的字符为小写替换后也为小写，首字母大写同理
# 则要使用回调函数
def matchcase(word):#辅助函数
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        if text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print(re.sub('yeah',matchcase('boot'),text,flags=re.IGNORECASE))
