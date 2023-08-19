from rest_framework import serializers
from .models import Room

# Defining a serializer class named 'RoomSerializer' that extends 'serializers.ModelSerializer'.
# This serializer will be used to convert complex data types (like a Room model instance) into JSON data and vice versa.
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        #Meta class provides additional information about the serializer.

        model= Room
        fields=('id','code','host','guest_can_pause','votes_to_skip','created_at')
        # Specifies the fields from the 'Room' model that should be included in the serialized output.
        # These fields will be converted into JSON format when serializing data.
