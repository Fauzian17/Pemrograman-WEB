import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

x = datetime.datetime.now()

class Katagori(models.Model):
    riwayat_sakit = models.CharField(max_length=100)

    def __str__(self):
        return self.riwayat_sakit

    class Meta:
        verbose_name_plural = '1. Katagori'

class Artikel(models.Model):
    judul = models.CharField(max_length= 100)
    isi = models.TextField(blank=True, null=True)
    kategori = models.ForeignKey(Katagori, on_delete=models.SET_NULL,blank=True , null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True ,null= True)
    thumbnail = models.ImageField(upload_to='artikel',blank=True, null=True)

    create_at =models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True,null=True)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{x.year}-{x.month}-{x.day}-{self.judul}')
        super(Artikel, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = '2. Artikel'


class Informasi(models.Model):
    nama_pasien = models.OneToOneField(User , on_delete=models.CASCADE)
    usia = models.CharField(max_length=100)
    riwayat =models.ForeignKey(Katagori, on_delete=models.SET_NULL, blank=True,null=True)
    foto =models.ImageField(upload_to='pengguna',blank=True, null=True)
    sakit=models.CharField(max_length=255)

    def __str__(self):
        return self.sakit


    class Meta:
        verbose_name_plural = '3. Informasi'

