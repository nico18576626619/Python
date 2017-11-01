def frange(start,end,increment):
    while start<end:
        yield start
        start+=increment


def countdown(n):
    print('Starting to count from',n)
    while n>0:
        yield n
        n-=1
    print('done')

if __name__=="__main__":
    # x=frange(1,3,0.5)
    # for t in x:
    #     print(t)

    # print(list(x))

    x=countdown(5)
    for i in x:
        print(i)