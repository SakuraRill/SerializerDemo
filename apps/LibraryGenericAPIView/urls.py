
from django.conf.urls import url

from LibraryGenericAPIView.views import PublisherView, PublisherViewDetail

urlpatterns = [
    # Rest_framework GenericAPIView实现
    url(r'^publisher$', PublisherView.as_view()),
    url(r'^publisher/(?P<pk>\d+)$', PublisherViewDetail.as_view()),
]
