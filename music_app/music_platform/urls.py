# Configure App urls here
from django.urls import path,include
from . import views
urlpatterns = [
    path("home/",views.home),
    path("",views.root),
    path("registration/",views.registration),
    path('login/',views.logins),
    path("logout/",views.logouts)
]
