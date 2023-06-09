import django_filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import PerevalAdded
from .serializers import PerevalAddedSerializers, PerevalAddedUpdateSerializer
from pereval.filters import PerevalFilter


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


@api_view(['GET'])
def get_data(request, pk):
    try:
        pereval = PerevalAdded.objects.get(pk=pk)
    except PerevalAdded.DoesNotExist:
        return Response(status=404)

    serializer = PerevalAddedSerializers(pereval)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_pereval(request, pk):
    try:
        pereval = PerevalAdded.objects.get(pk=pk)
    except PerevalAdded.DoesNotExist:
        return Response({'state': 0, 'message': 'Pereval not found'}, status=status.HTTP_404_NOT_FOUND)

    if pereval.status != 'new':
        return Response({'state': 0, 'message': 'Pereval status is not NEW'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = PerevalAddedUpdateSerializer(pereval, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'state': 1}, status=status.HTTP_200_OK)
    return Response({'state': 0, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PerevalList(ListAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializers
    filterset_class = PerevalFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
