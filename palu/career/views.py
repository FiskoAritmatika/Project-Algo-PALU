from django.shortcuts import render
from users.decorators import user_login_required

@user_login_required
def indexCareer(request):
    return render(request, 'career/index.html')