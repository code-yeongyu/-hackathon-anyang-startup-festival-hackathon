from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^signup/$', views.sign_up),  # 프로필 정보를 얻거나 , 변경하는 라우트
    url(r'^video/(?P<pk>[0-9]+)/$',
        views.VideoDetail.as_view()),  # 해당되는 게시글을 얻는 라우트
    url(r'video/^$', views.VideoListAPIView.as_view())
]