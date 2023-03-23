from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path(r'', views.login_page, name='login'),
    path(r'', views.logout_page, name='logout'),
    path(r'index/', views.index, name="index"),
    path(r'index/about/', views.about, name="about"),
    path(r'register/', views.register_page, name='register_page'),
    path(r'hotels.html/', views.hotels, name='hotels'),
    path(r'insurance.html/', views.insurance, name='insurance'),
    path(r'index/package.html/', views.package, name='package'),
    path(r'messages.html/', views.message, name='messages'),
    path(r'contact.html/', views.contact, name='contact'),
]
