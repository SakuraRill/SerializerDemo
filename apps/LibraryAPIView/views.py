from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin

from LibraryModelViewSet.models import PublisherModel
from LibraryModelViewSet.serializers.PublisherSerializers import PublisherSerializers


class PublisherView(APIView):
    """出版社"""

    def get(self, request, *args, **kwargs):

        instances = PublisherModel.objects.all()

        ps = PublisherSerializers(instances, many=True)

        return Response(ps.data)

