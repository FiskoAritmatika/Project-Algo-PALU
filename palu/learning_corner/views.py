from django.shortcuts import render

# Create your views here.
def indexMateri(request):
    return render(request, 'materi/index.html')
  
def indexEvent(request):
    return render(request, 'event/index.html')