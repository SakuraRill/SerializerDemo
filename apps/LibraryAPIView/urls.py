
from django.conf.urls import url

from LibraryAPIView.views import PublisherView

urlpatterns = [
    # Rest_framework APIView实现
    url(r'^publisher$', PublisherView.as_view()),
]
