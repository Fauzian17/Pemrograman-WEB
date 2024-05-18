from django.shortcuts import render
from berita.models import Artikel,Katagori

def home(request):
    template_name = "halaman/index.html"
    kategori = request.GET.get('kategori')
    
    # data_kategori = Katagori.objects.all()
    
    # if kategori is None or kategori == "ALL":
    #     print("ALL")
    #     data_artikel = Artikel.objects.all()
    #     menu_aktif = "ALL"
    # else:
        # try:
        #     kategori_obj = Katagori.objects.get(riwayat_sakit=kategori)
        #     data_artikel = Artikel.objects.filter(kategori=kategori_obj)
        #     menu_aktif = kategori_obj.riwayat_sakit
        # except Katagori.DoesNotExist:
        #     data_artikel = Artikel.objects.none()
        #     menu_aktif = "NONE"
        #     print(f"Kategori dengan riwayat_sakit {kategori} tidak ditemukan.")
    if kategori is None or kategori == "ALL":
        print("ALL")
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        kategori_obj = Katagori.objects.filter(riwayat_sakit=kategori)
        print(kategori_obj)
        if kategori_obj.count() != 0:
            data_artikel = Artikel.objects.filter(kategori=kategori_obj[0])
            menu_aktif = kategori
        else:
            menu_aktif="ALL"
            data_artikel=[]


    data_kategori = Katagori.objects.all()
    context = {
        'title': 'Selamat datang',
        'data_artikel': data_artikel,
        'data_kategori': data_kategori,
        'menu_aktif': menu_aktif,
    }
    
    return render(request, template_name, context)

def about(request):
    template_name="halaman/about.html"
    context={
        'title':'Hallo selamat datang di halam about',
        'umur':20,
    }
    return render(request,template_name,context)

def contact(request):
    template_name="halaman/contact.html"
    context={
        'title' : 'Hubungi Saya'
    }
    return render(request,template_name,context)

def detail_artikel(request, slug):
    template_name = "halaman/detail_artikel.html"
    artikel = Artikel.objects.get(slug=slug)
    print(artikel)
    context = {
        'title' : artikel.judul,
        'artikel': artikel
        
    }
    return render(request,template_name,context)