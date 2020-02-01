from django.db import models

# Create your models here.

# TODO add date completed


class ListItem(models.Model):
    name = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField()
