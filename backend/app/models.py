from django.db import models


# Create your models here.
class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.user',
                               related_name='article',
                               on_delete=models.CASCADE)
    video = models.FileField(upload_to='uploads/')