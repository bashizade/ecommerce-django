from django.db import models


# Create your models here.
class MainModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSetting(MainModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='')


class Slider(MainModel):
    image = models.ImageField(upload_to='')


class Banner(MainModel):
    image = models.ImageField(upload_to='')
    type = models.IntegerField()
