def manual_iter():
    try:
        with open('text.txt') as f:
            try:
                while True:
                    line=next(f)
                    # line=f.readline()
                    print(line,end='')
            except StopIteration:
                print('迭代结束了！！')
                pass
    except FileNotFoundError:
        print('文件不存在！！')






if __name__=='__main__':
    # manual_iter()
    items = [1, 2, 3, 4]
    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    