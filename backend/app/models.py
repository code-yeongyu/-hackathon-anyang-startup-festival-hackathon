from django.db import models


# Create your models here.
class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('auth.user',
                               related_name='video',
                               on_delete=models.CASCADE)
    video = models.FileField(upload_to='uploads/video/')


class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('auth.user',
                               related_name='image',
                               on_delete=models.CASCADE)
    image = models.FileField(upload_to='uploads/image/')