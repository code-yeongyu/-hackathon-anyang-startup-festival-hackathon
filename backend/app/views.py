from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, permissions, status, mixins
from rest_framework.decorators import api_view

from app.models import Video
from app.serializers import VideoSerializer
from app.forms import SignUpForm

# upload video
# get user's article(video)


class VideoListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        backup_queryset = self.queryset
        self.queryset = Video.objects.filter(author=request.user)
        returning_value = self.list(request, *args, **kwargs)
        self.queryset = backup_queryset
        return returning_value

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VideoDetail(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


@api_view(['POST'])
def sign_up(request):  # 회원가입
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)