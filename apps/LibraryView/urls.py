
from django.conf.urls import url

from LibraryView.views import PublisherView

urlpatterns = [
    # Django View实现
    url(r'^publisher$', PublisherView.as_view()),
]
