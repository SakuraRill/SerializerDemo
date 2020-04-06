

class A(object):

    def call(self, msg, *args, **kwargs):
        super(A, self).call("zhaowei", *args, **kwargs)
        print("A", msg)


class B(object):

    def call(self, msg, *args, **kwargs):
        print("B", msg)


class C(A, B):

    def __init__(self):
        self.try_call()

    def try_call(self):
        self.call("hi")


if __name__ == '__main__':
    C()
