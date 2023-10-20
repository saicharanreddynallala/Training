class cse:
    def __init__(self):
        print("default")
class two:
    def fun1(self):
        print("fun2-mother")
class three(two,cse):
    def fun5(self):
        print("5")
d=cse()
a=two()
b=three()
b.fun5()
a.fun1()