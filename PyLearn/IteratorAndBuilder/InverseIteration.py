# 使用内置函数进行反向迭代
a=[1,2,3,4,5]
for i in reversed(a):
    print(i)



with open('text.txt') as f:
    for i in reversed(list(f)):
        print(i,end='')


class CountDown:
    def __init__(self,start):
        self.start=start


    def __iter__(self):
        n=1
        while n<=self.start:
            yield n
            n+=2

    def __reversed__(self):

        n = self.start
        while n >= 0:
            yield n
            n -= 1


if __name__=='__main__':
    for i in CountDown(30):
        print(i)

    for i in reversed(CountDown(30)):
        print(i)