from collections import deque

class linehistory:
    def __init__(self,lines):
        self.lines=lines
        self.history=deque()


    def __iter__(self):
        enum=enumerate(self.lines,1)
        for lineno,line in enum:
            self.history.append((lineno,line))
            yield line

    def clear(self):
        self.history.clear()


if __name__=='__main__':
    # with open('text.txt','r') as f:
    #     lines=linehistory(f)
    #     for i in lines:
    #         if 'python' in i:
    #             # for lineno,hline in lines.history:
    #                 # print('{}:{}'.format(lineno,hline),end='')
    #             # 打印文本中含有python字符串的行
    #             temp=lines.history.pop()
    #             print('第{}包含python:{}'.format(temp[0],temp[1]),end='')

    with open('text.txt','r') as f:
        enum=enumerate(f,1)
        for m,n in enum:
            if 'python' in n:
                print('{}:{}'.format(m,n),end='')