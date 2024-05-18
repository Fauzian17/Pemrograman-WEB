from django.shortcuts import render,redirect
from berita.models import Katagori,Informasi,Artikel
from berita.forms import ArtikelForm

# Create your views here.
def dasboard(request):
    template_name = "dasboard/index.html"
    context = {
        'title' : 'Halaman Dasboard'
    }

    return render(request,template_name,context)

def katagori_ls(request):
    template_name = "dasboard/snippets/katagori_ls.html"
    katagori= Katagori.objects.all()
    print(katagori)
    context = {
        'title' : 'Halaman Kategori',
        'katagori' : katagori
    }

    return render(request,template_name,context)

def kategori_add(request):
    template_name = "dasboard/snippets/kategori_add.html"
    if request.method == "POST":
        new_kategori = request.POST.get('nama_kategori')
        Katagori.objects.create(
            riwayat_sakit = new_kategori
            )
        return redirect(katagori_ls)
    context = {
        'title' : 'Tambah Kategori',
    }
    return render(request,template_name,context)

def kategori_update(request, id_katagori):
    template_name = "dasboard/snippets/kategori_update.html"
    try:
        up_kategori = Katagori.objects.get(id=id_katagori)
    except:
        return(katagori_ls)
    if request.method == "POST":
        new_kategori = request.POST.get('nama_kategori')
        up_kategori.riwayat_sakit = new_kategori
        up_kategori.save()
        return redirect(katagori_ls)
    context = {
        'title' : 'Tambah Kategori',
        'up_kategori' : up_kategori
    }
    return render(request,template_name,context)

def kategori_delete(request, id_katagori):
    try:
        Katagori.objects.get(id=id_katagori).delete()
    except:
        pass
    return redirect(katagori_ls)

def artikel_list(request):
    template_name = "dasboard/snippets/artikel_list.html"
    artikel = Artikel.objects.all()
    print(artikel)
    context = {
        'title' : 'daftar artikel',
        'artikel' : artikel
    }
    return render(request,template_name,context)

def artikel_add(request):
    print(request.user)
    template_name ="dasboard/snippets/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid:
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
        else:
            print(forms.error_class)
    forms = ArtikelForm()
    context ={
        'title' : 'Tambah Artikel Baru',
        'forms' : forms
    }
    return render(request,template_name,context)

def artikel_detail(request, id_artikel):
    template_name = "dasboard/snippets/artikel_detail.html"
    artikel = Artikel.objects.get(id=id_artikel)
    context = {
        'title' : artikel.judul,
        'artikel': artikel
    }
    return render(request,template_name,context)

def artikel_update(request, id_artikel):
    template_name = "dasboard/snippets/artikel_forms.html"
    artikel = Artikel.objects.get(id=id_artikel)
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid:
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
    forms = ArtikelForm(instance=artikel)
    context ={
        'title' : 'Edit Artikel Baru',
        'forms' : forms
    }
    return render(request,template_name,context)

def artikel_delete(request, id_artikel):
    try:
        Artikel.objects.get(id=id_artikel).delete()
    except:
        pass
    return redirect(artikel_list)