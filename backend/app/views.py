from urllib.parse import unquote
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import generics, permissions, status, mixins
from rest_framework.decorators import api_view

from backend import settings
from app.models import Video, Image
from app.serializers import VideoSerializer, ImageSerializer
from app.forms import SignUpForm

# upload video
# get user's article(video)


@api_view(['POST'])
def create_video(request):
    if request.user.is_authenticated:
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response({"id": serializer.data['id']},
                            status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


class VideoListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        backup_queryset = self.queryset
        self.queryset = Video.objects.filter(writer=request.user.id)
        returning_value = self.list(request, *args, **kwargs)
        self.queryset = backup_queryset
        return returning_value


class VideoDetail(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


@api_view(['POST'])
def create_image(request):
    if request.user.is_authenticated:
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response({"id": serializer.data['id']},
                            status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def image(request, pk):  # 이미지 반환
    test_file = open(
        settings.BASE_DIR +
        unquote(str(get_object_or_404(Image, pk=pk).image.url)), 'rb')
    return HttpResponse(content=test_file,
                        content_type="image/jpeg",
                        status=status.HTTP_200_OK)


@api_view(['GET'])
def video(request, pk):  # 비디오 반환
    test_file = open(
        settings.BASE_DIR +
        unquote(str(get_object_or_404(Video, pk=pk).video.url)), 'rb')
    return HttpResponse(content=test_file,
                        content_type="file",
                        status=status.HTTP_200_OK)


class ImageListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        backup_queryset = self.queryset
        self.queryset = Image.objects.filter(writer=request.user.id)
        returning_value = self.list(request, *args, **kwargs)
        self.queryset = backup_queryset
        return returning_value


@api_view(['POST'])
def sign_up(request):  # 회원가입
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)