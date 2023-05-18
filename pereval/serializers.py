from rest_framework.serializers import ModelSerializer

from .models import Users, Coords, PerevalAdded, PerevalAreas, PerevalImages


class UsersSerializers(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializers(ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalAddedSerializers(ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'


class PerevalAreasSerializers(ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = '__all__'


class PerevalImagesSerializers(ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'

class PerevalAddedUpdateSerializer(ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'
        read_only_fields = ['user']
