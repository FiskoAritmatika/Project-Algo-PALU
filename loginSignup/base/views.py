from django.shortcuts import render, redirect
from django.contrib import messages # Biar bisa pake alert django
from django.contrib.auth.hashers import make_password # Bikin password ke hash
from django.contrib.auth.hashers import check_password # Bandingin password inputan sama yang di hash di database
from .models import User # Import model User

def register(request):
    if request.method == "POST": # Cek apakah form pake method POST
        nama = request.POST.get("nama") # Ambil data dari form html yang punya name serupa, dimasukin ke variable
        nim = request.POST.get("nim") # request.POST adalah dictionary berisi input user
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Validasi email
        if User.objects.filter(email=email).exists(): # Cek apakah email sudah ada di database, kalo udah ada tampil error
            messages.error(request, "Email sudah terdaftar")
            return redirect("register")

        # Validasi nim
        if User.objects.filter(nim=nim).exists():
            messages.error(request, "Nim sudah terdaftar")
            return redirect("register")

        # Simpan user
        User.objects.create(
            nama=nama,
            nim=nim,
            email=email,
            password=make_password(password) # Password di hash
        )

        return redirect("login") # Setelah selesai, diarahkan ke halaman login

    return render(request, "users/register/index.html") # Kalo bukan menjalankan method POST, berarti render ke page index register

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Cari user berdasarkan email
        user = User.objects.filter(email=email).first() # filter() = mengembalikan QuerySet, first() = ambil data paling pertama

        # Pengecekan, user harus ada dan membandingkan password input dengan hash di database
        if user and check_password(password, user.password): 
            request.session["user_id"] = user.id # Simpen session yang diperlukan di server
            request.session["user_nama"] = user.nama
            request.session["user_nim"] = user.nim
            return redirect("dashboard")

        # Kalo pengecekan tadi false, menampilkan message error
        messages.error(request, "Email atau password tidak ditemukan")

    return render(request, "users/login/index.html")

def logout(request):
    # Menghapus semua session user, otomatis user logout
    request.session.flush()
    return redirect("login")