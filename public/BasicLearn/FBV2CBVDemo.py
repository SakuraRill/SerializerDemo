from django.http import HttpResponse
from django.views import View

"""FBV和CBV"""


class MyView(View):   # 基于CBV实现
    def get(self, request):
        return HttpResponse('OK')


def my_view(request):   # 基于FBV实现
    if request.method == 'GET':
        return HttpResponse('OK')