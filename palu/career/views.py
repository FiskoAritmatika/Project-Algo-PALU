from django.shortcuts import render
from .models import Career

def career_list(request):
    careers = Career.objects.all()
    return render(request, 'career/index.html', {
        'careers': careers
    })