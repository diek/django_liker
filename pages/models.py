from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import CustomUser


class Reader(CustomUser):
    pass

    def __str__(self):
        return self.email


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=200)
    post = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class PostLike(models.Model):
    liked = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
