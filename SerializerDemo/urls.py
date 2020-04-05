
from django.conf.urls import url
from django.urls import include

urlpatterns = [

    url(r'^library/view/', include("LibraryView.urls")),

    url(r'^library/apiview/', include("LibraryAPIView.urls")),

    url(r'^library/genericapiview/', include("LibraryGenericAPIView.urls")),

    url(r'^library/modelviewset/', include("LibraryModelViewSet.urls")),
]
