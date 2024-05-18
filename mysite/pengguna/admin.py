from django.contrib import admin
from pengguna.models import RumahSakit,Golongan,DataPasien

# Register your models here.
class DataPasienAdmin(admin.ModelAdmin):
    list_display = ['user','namaPasien','telefon','alamat','ruangan']
    search_fields =['namaPasien']
admin.site.register(DataPasien, DataPasienAdmin)

class RumahSakitAdmin(admin.ModelAdmin):
    list_display = ['nama_RS','alamat_RS']
    search_fields = ['nama_RS']
admin.site.register(RumahSakit,RumahSakitAdmin)

class GolonganAdmin(admin.ModelAdmin):
    list_display = ['no_BPJS','keterangan']
    search_fields=['no_BPJS']
admin.site.register(Golongan,GolonganAdmin)