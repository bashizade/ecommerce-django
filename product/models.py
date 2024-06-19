from django.db import models

from main.models import MainModel


# Create your models here.
class Category(MainModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Comment(MainModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class ProductGallery(MainModel):
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')


class Product(MainModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
