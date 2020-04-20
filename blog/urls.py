from django.urls import path
from blog import views
urlpatterns = [
    path('', views.home, name='home'),
    path('hey/',views.hr, name='hr'),
    path('how/',views.hk, name='hk'),
    
    
]
