from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.login_page, name='login'),
    path('', views.logout_page, name='logout'),
    path('index/', views.index, name="index"),
    path('index/about/', views.about, name="about"),
    path('register/', views.register_page, name='register_page'),
    path('hotels/', views.hotels, name='hotels'),
    path('insurance/', views.insurance, name='insurance'),
    path('index/package/', views.package, name='package'),
    path('messages/', views.message, name='messages'),
    path('contact/', views.contact, name='contact'),
    path('index/payment/', views.payment,name='payment'),
]

