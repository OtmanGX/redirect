from django.db import models


# Create your models here.
class ShortLink(models.Model):
    key = models.TextField()
    url = models.CharField(max_length=30)
