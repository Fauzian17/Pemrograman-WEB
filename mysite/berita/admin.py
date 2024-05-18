from django.contrib import admin
from berita.models import Katagori, Informasi, Artikel

# Register your models here.

admin.site.register(Katagori)

class InformasiAdmin(admin.ModelAdmin):
    list_display=['foto','nama_pasien','usia','riwayat','sakit']
    search_fields = ['nama_pasien']
admin.site.register(Informasi,InformasiAdmin)

class ArtikelAdmin(admin.ModelAdmin):
    list_display=['judul','kategori','author']
    search_fields = ['judul']
admin.site.register(Artikel,ArtikelAdmin)


