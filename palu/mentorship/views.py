from django.shortcuts import render
from users.decorators import user_login_required

@user_login_required
def indexMentorship(request):
    return render(request, 'mentorship/index.html')