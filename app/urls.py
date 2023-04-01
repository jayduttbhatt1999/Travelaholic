from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'app'
urlpatterns = [
    path('', views.login_page, name='login'),
    path('', views.logout_page, name='logout'),
    path('accounts/login/', views.login_page, name='login'),

    path('index/', views.index, name="index"),
    path('index/about/', views.about, name="about"),

    path('register/', views.register_page, name='register_page'),

    path('hotels/', views.hotels, name='hotels'),
    path('hotels/search_hotels', views.search_hotels, name='hotel'),
    path('index/package/', views.package, name='package'),
    path('hotelbooking/', views.hotelbooking, name='hotelbooking'),
    path('packages/', views.package, name='packages'),
    path('quebec/', views.quebec, name='quebec'),
    path('packbook/', views.packbook, name='packbook'),
    path('book/', views.book, name='book'),
    # path('book/<int:pkg_id>', views.book, name='book'),
    path('niagara/', views.niagara, name='niagara'),
    path('banff/', views.banff, name='banff'),

    path('messages/', views.message, name='messages'),

    path('contact/', views.contact, name='contact'),
    path('payment/', views.payment, name='payment'),

    # path('booking/<pkg_id>', views.booking, name='booking'),
    # path('hotelbooking/<pkg_id>', views.hotelbooking, name='hotelbooking'),
    # path("confirm/<pkg_id>", views.confirm, name='confirm'),
    # path("hotelconfirm/<pkg_id>", views.hotelconfirm, name='hotelconfirm'),

    path('profile/', views.profile, name='users-profile'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='app/registration/password_reset_form.html',
             subject_template_name='app/registration/password_reset_subject.txt',
             email_template_name='app/registration/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('passwordreset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='app/registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='app/registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='app/registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
