from django.shortcuts import render, get_object_or_404
from .models import Event, Materi
from django.utils import timezone

def indexEvent(request):
    events = Event.objects.all()   # ambil semua event
    now = timezone.now()
    return render(request, 'learning_corner/event/index.html', {
        'events': events,
        'now': now,
        })

def detailEvent(request, pk):
    event = get_object_or_404(Event, pk=pk)
    now = timezone.now()
    return render(request, 'learning_corner/event/detail.html', {
        'event': event,
        'now': now,
        })

def indexMateri(request):
    materis = Materi.objects.all()
    return render(request, 'learning_corner/materi/index.html', {'materis': materis})

def detailMateri(request, pk):
    materi = get_object_or_404(Materi, pk=pk)
    return render(request, 'learning_corner/materi/detail.html', {'materi': materi})