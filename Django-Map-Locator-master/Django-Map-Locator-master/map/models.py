from django.db import models

# Create your models here.


class Obj(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    address= models.TextField(blank=True)
    status = models.CharField(max_length=100, null=True)
    financed=models.CharField(max_length=100, null=True)
    curator = models.TextField(blank=True)
    email = models.TextField(blank=True)
    objtype = models.CharField(max_length=100, null=True)
    sporttype = models.CharField(max_length=100, null=True)
    coordinatex = models.FloatField(verbose_name="coordinatex")
    coordinatey = models.FloatField(verbose_name="coordinatey ")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name
