from django.http import HttpResponse
from django.views import View


class PublisherView(View):
    """出版社"""

    def get(self, request, *args, **kwargs):
        print("View: get")
        return HttpResponse("ok")

    def dispatch(self, request, *args, **kwargs):
        print("View: dispatch")
        ret = super(PublisherView, self).dispatch(request, *args, **kwargs)
        print(f"View-ret：{ret}")
        return HttpResponse(ret)
