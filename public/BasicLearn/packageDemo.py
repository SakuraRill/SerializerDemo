

# 封装的Demo
class MyDemo1:
    """把同一个类的方法封装到类中"""

    def get(self):
        print('this is method get')

    def post(self, request):
        print(f'this is method post, {request}')

    @classmethod
    def as_view(cls):
        """函数封装"""
        def view(request):
            print(f"request: {request}\nview.self: {view.self}\nview.attr: {view.attr}")
            self = view.self

            if hasattr(self, 'post'):  # 反射判断是否有post方法
                handler = getattr(self, 'post', lambda x, y: print(f"Find not post method, {y}"))
            else:
                handler = lambda x, y: print(f"Find not post attr, {y}")
            return handler(self, request)  # 执行

        # 对函数进行数据封装
        view.self = cls
        view.attr = 'this is a view function'
        return view  # 返回一个函数


class MyDemo2:
    """将数据封装到自己的对象中"""
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    print("把同一个类的方法封装到类中".center(100, '='))
    demo1 = MyDemo1()
    print(demo1.__dir__())
    demo1.get()

    print("将数据封装到自己的对象中".center(100, '='))
    demo2 = MyDemo2('zhaowei')
    demo2.address = '深圳市'
    print(demo2.__dict__)

    print("对函数进行封装".center(100, '='))
    view = demo1.as_view()
    print(view)
    print(view.__dir__())
    view('this is request data')

