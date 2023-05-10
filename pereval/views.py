from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import PerevalAdded
from .serializers import PerevalAddedSerializers


class PerevalViewSet(ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializers

@api_view(['POST'])
def submit_data(request):
    serializer = PerevalAddedSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
