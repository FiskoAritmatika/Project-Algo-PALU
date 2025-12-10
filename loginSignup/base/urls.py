from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]


#from django.urls import path, include
#from. views import authView, home
#from django.conf import settings
#from django.conf.urls.static import static

#app_name = "base"

#urlpatterns = [ 
    #path("signup/", authView, name = "authView"),
    #path("accounts/", include("django.contrib.auth.urls")), 
    #path("", home, name="home"),
#] + static(settings.STATIC_URL)

#path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

