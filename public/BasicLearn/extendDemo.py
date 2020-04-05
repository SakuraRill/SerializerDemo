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
    """hhhh"""
    pass


c = C()
c.a()

# C.a -> A.a -> B.a
# C.b -> A.b
