from django.urls import path
from . import views
from app.views import ResetPasswordView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'app'
urlpatterns = [
    path('', views.login_page, name='login'),
    path('', views.logout_page, name='logout'),
    path('index/', views.index, name="index"),
    path('index/about/', views.about, name="about"),
    path('register/', views.register_page, name='register_page'),
    path('hotels/', views.hotels, name='hotels'),
    path('index/package/', views.package, name='package'),
    path('messages/', views.message, name='messages'),
    path('contact/', views.contact, name='contact'),
    path('index/payment.html/', views.payment, name='payment'),
    path('booking/<pkg_id>', views.booking, name='booking'),
    path("confirm/<pkg_id>", views.confirm, name='confirm'),
    path('passwordreset/', ResetPasswordView.as_view(), name='passwordreset'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
