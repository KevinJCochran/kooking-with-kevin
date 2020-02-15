from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=511)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    views = models.IntegerField
    content = models.TextField()
