
from django.urls import path
from berita.views import (
    dasboard,
    katagori_ls,
    kategori_add,
    kategori_update,
    kategori_delete,
    artikel_list,
    artikel_add,
    artikel_detail,
    artikel_update,
    artikel_delete)

urlpatterns = [
    path('', dasboard, name="dasboard"),

    path('katagori/list', katagori_ls, name="katagori_ls"),
    path('kategori/add', kategori_add, name="kategori_add"),
    path('kategori/update/<int:id_katagori>', kategori_update, name="kategori_update"),
    path('kategori/delete/<int:id_katagori>', kategori_delete, name="kategori_delete"),

    path('artikel/list', artikel_list, name="artikel_list"),
    path('artikel/add', artikel_add, name="artikel_add"),
    path('artikel/detail/<int:id_artikel>', artikel_detail, name="artikel_detail"),
    path('artikel/update/<int:id_artikel>', artikel_update, name="artikel_update"),
    path('artikel/delete/<int:id_artikel>', artikel_delete, name="artikel_delete"),
]