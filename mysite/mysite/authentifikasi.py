from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def akun_login(request):
    # Cek jika pengguna sudah terautentikasi
    if request.user.is_authenticated:
        return redirect('/')
    
    template_name = "halaman/login.html"
    pesan = ''
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            pesan = "Login Gagal"
    
    # Pastikan konteks terbentuk dan di-render dalam kedua kasus (GET dan POST)
    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)


def akun_registrasi(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    template_name = "halaman/registrasi.html"
    context ={

    }
    return render(template_name,context)