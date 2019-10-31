from django.conf.urls import url
from app import views
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    url(r'^signin/$', drf_views.obtain_auth_token, name='auth'),
    url(r'^signup/$', views.sign_up),
    # video
    url(r'^upload/video/$', views.create_video),
    url(r'^video/(?P<pk>[0-9]+)/$', views.video),
    url(r'^video/$', views.VideoListAPIView.as_view()),
    # image
    url(r'^upload/image/$', views.create_image),
    url(r'^image/(?P<pk>[0-9]+)/$', views.image),
    url(r'^image/$', views.ImageListAPIView.as_view()),
]
