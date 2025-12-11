"""
URL configuration for palu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import register, login, logout
from chat.views import private_chat, inbox
from dashboard.views import indexDashboard
from learning_corner.views import indexEvent, indexMateri, detailEvent, detailMateri

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
    path('chat/<int:user_id>', private_chat, name='private_chat'),
    path("chat/", inbox, name="chat_inbox"),
    path('learning_corner/materi/', indexMateri, name='materi'),
    path('learning_corner/event/', indexEvent, name='event'),
    path('learning_corner/event/<int:pk>/', detailEvent, name="detailEvent"),
    path('learning_corner/materi/<int:pk>/', detailMateri, name="detailMateri"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
