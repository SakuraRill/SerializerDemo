
from django.conf.urls import url

from LibraryModelViewSet.views.PublisherView import PublisherView

urlpatterns = [
    # Rest_FlameWork ModelViewSet实现
    url(r'^publisher$', PublisherView.as_view({'get': 'list', 'post': 'create'})),
    url(r'^publisher/(?P<pk>\d+)$', PublisherView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
