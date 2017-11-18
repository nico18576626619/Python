# 调用父类的方法
# class A:
#     def span(self):
#         print('a.span')
#
#
# class B(A):
#     def span(self):
#         print('b.span')
#         super().span()

# 确保父类被初始化
class A:
    def __init__(self):
        self.x=10

class B(A):
    def __init__(self):
        self.y=1
        super().__init__()






if __name__=='__main__':
    print(B().x)
    print(B().y)
