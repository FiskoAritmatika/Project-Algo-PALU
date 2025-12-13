from django.contrib import admin
from django.urls import path
from users.views import register, login, logout
from chat.views import private_chat, inbox
from dashboard.views import indexDashboard
from learning_corner.views import indexEvent, indexMateri, detailEvent, detailMateri
from mentorship.views import indexMentorship, approve_mentorship, reject_mentorship, finish_mentorship
from career.views import career_list

from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


def root_redirect(request):
    return redirect('/dashboard/')


urlpatterns = [
    path('', root_redirect, name='root_redirect'),
    path('admin/', admin.site.urls),

    # Auth
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    # Pages
    path('dashboard/', indexDashboard, name='dashboard'),
    path('chat/<int:user_id>/', private_chat, name='private_chat'),
    path('chat/', inbox, name='chat_inbox'),

    path('learning_corner/materi/', indexMateri, name='materi'),
    path('learning_corner/event/', indexEvent, name='event'),
    path('learning_corner/event/<int:pk>/', detailEvent, name='detailEvent'),
    path('learning_corner/materi/<int:pk>/', detailMateri, name='detailMateri'),

    path('mentorship/', indexMentorship, name='mentorship'),
    path('mentorship/approve/<int:request_id>/', approve_mentorship, name='approve_mentorship'),
    path('mentorship/reject/<int:request_id>/', reject_mentorship, name='reject_mentorship'),
    path('mentorship/finish/<int:request_id>/', finish_mentorship, name='finish_mentorship'),

    path('career/', career_list, name='career'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)