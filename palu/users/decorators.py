from django.shortcuts import redirect

def user_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        
        # Cek apakah user id ada di session
        if "user_id" not in request.session:
            return redirect("login")
        # Kalo udah login jalanin view aslinya
        return view_func(request, *args, **kwargs)
    return wrapper