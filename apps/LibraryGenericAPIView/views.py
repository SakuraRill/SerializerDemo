
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from LibraryModelViewSet.models import PublisherModel
from LibraryModelViewSet.serializers.PublisherSerializers import PublisherSerializers


class PublisherView(ListModelMixin,
                    CreateModelMixin,
                    GenericAPIView):

    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PublisherViewDetail(RetrieveModelMixin,
                          UpdateModelMixin,
                          DestroyModelMixin,
                          GenericAPIView):

    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# 进阶版
class PublisherSupperView(ListCreateAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializers


class PublisherSupperViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializers