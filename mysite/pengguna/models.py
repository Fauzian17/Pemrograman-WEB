from django.db import models
from django.contrib.auth.models import User

class DataPasien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    namaPasien = models.TextField()
    telefon = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.TextField()
    ruangan = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = '2. Biodata'

    def __str__(self):
        return self.user.username

class RumahSakit(models.Model):
    data_pasien = models.ForeignKey(DataPasien, on_delete=models.CASCADE)
    nama_RS = models.CharField(max_length=255)
    alamat_RS = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = '1. Rumah Sakit'

    def __str__(self):
        return self.nama_RS

class Golongan(models.Model):
    rumah_sakit = models.ManyToManyField(RumahSakit)
    no_BPJS = models.CharField(max_length=255)
    keterangan = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = '3. Golongan'

    def __str__(self):
        return self.no_BPJS
    
#  Relasi One-to-One:
# Antara model DataPasien dan model User. Setiap DataPasien terhubung dengan satu User.
    
# Relasi One-to-Many:
# Antara model DataPasien dan model RumahSakit.mSetiap RumahSakit dapat memiliki banyak DataPasien.
    
# Relasi Many-to-Many:
# Antara model Golongan dan model RumahSakit. Banyak Golongan dapat terhubung dengan banyak RumahSakit.
