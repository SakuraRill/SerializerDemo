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
        self.c()

    def c(self):
        self.a()


if __name__ == '__main__':
    C()



# C.a -> A.a -> B.a
# C.b -> A.b
