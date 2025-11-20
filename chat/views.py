from django.shortcuts import render

# Create your views here.
def indexChat(request):
    return render(request, 'index.html')