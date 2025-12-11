from django.shortcuts import render
from users.decorators import user_login_required

# Create your views here.
@user_login_required
def indexDashboard(request):
    return render(request, 'dashboard/index.html', {
        "nama": request.session.get("user_nama"),
        "nim": request.session.get("user_nim"),
    })