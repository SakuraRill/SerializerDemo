"""多重继承基础"""


class A:
    def b(self):
        print("3")


class B:
    def a(self):
        print("1")
        self.b()

    def b(self):
        print("2")


class C(A, B):
    def __init__(self):
        self.a()


if __name__ == '__main__':
    c = C()



# C.a -> A.a -> B.a
# C.b -> A.b

# 类C多重继承AB,类C实例化的时候，执行了self.a()方法,其中self是C
# 首先会在C找不到a()方法，然后去类A中找不到a()方法，横向寻找去B类中，结果在类B中找到a方法并执行
# a方法中又调用了self.b()方法，
# 这时候应该回去C开始找b方法，而不是直接调用B中的b方法，原因是self代表的就是C
# 最后会在A中找到b方法，执行并打印
