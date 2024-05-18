
from django.contrib import admin
from django.urls import path, include

#
from django.conf import settings
from django.conf.urls.static import static

from mysite.views import home,about,detail_artikel,contact
from mysite.authentifikasi import akun_login,akun_registrasi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),

    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('detail_artikel/<slug:slug>', detail_artikel, name="detail_artikel"),
    path('dasboard/',include('berita.urls')),

    path('authentifikasi/login',akun_login, name="akun_login"),
    path('authentifikasi/regitrasi',akun_registrasi, name="akun_registrasi"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)