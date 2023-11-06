from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerailizer(ModelSerializer):
    class Meta:
        model=Room
        fields = '__all__'