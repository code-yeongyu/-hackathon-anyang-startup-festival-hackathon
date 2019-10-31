from rest_framework import serializers
from app.models import Video

# edit for the video model


class VideoSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Video
        fields = ('id', 'created_at', 'author', 'video')