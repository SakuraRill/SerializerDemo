from rest_framework.serializers import ModelSerializer

from LibraryModelViewSet.models import PublisherModel, AuthorModel, BookModel


class PublisherSerializers(ModelSerializer):
    """出版社序列化器"""

    class Meta:
        model = PublisherModel
        fields = "__all__"


class AuthorSerializers(ModelSerializer):
    """作者序列化器"""

    class Meta:
        model = AuthorModel
        fields = "__all__"


class BookSerializers(ModelSerializer):
    """书籍序列化器"""

    class Meta:
        model = BookModel
        fields = "__all__"
