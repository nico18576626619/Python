class Test:
    __name='python'

    def a(self):
        print(Test.__name)

a=Test()
a.a()
print(Test._Test__name)
print(a._Test__name)