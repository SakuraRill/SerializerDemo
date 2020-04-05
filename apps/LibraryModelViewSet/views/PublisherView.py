
from rest_framework.viewsets import ModelViewSet

from LibraryModelViewSet.models import PublisherModel, AuthorModel, BookModel
from LibraryModelViewSet.serializers.PublisherSerializers import PublisherSerializers, AuthorSerializers, \
    BookSerializers


class PublisherView(ModelViewSet):
    """出版社"""
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializers


class AuthorView(ModelViewSet):
    """作者"""
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers


class BookView(ModelViewSet):
    """书籍"""
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
