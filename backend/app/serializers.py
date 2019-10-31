from rest_framework import serializers
from app.models import Video, Image

# edit for the video model


class VideoSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Video
        fields = ('id', 'created_at', 'writer', 'video')


class ImageSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Image
        fields = ('id', 'created_at', 'writer', 'image')