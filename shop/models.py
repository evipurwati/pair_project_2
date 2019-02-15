from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField

from django.db import models as models

class Category(models.Model) :
    nama_kategori = models.CharField(max_length = 100)

    def __str__(self) :
        return self.nama_kategori

class Stuff(models.Model) :
    foto = models.ImageField(upload_to="static/images")
    nama = models.CharField(max_length = 100)
    harga = models.CharField(max_length = 25)
    deskripsi = models.TextField(max_length = 600)
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) :
        return self.nama

