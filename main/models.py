from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='')


class Slider(models.Model):
    image = models.ImageField(upload_to='')


class Banner(models.Model):
    image = models.ImageField(upload_to='')
    type = models.IntegerField()
