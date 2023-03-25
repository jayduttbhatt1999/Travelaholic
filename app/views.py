from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Amenities, Hotel, Extras, Package


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app/passwordreset.html'
    email_template_name = 'app/passwordresetemail.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('app:login')

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            messages.warning(request, 'Register here')
            return redirect('app:register_page')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        return redirect('app:index')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'app/login.html')

def logout_page(request):
    logout(request)
    return render(request, 'app/index.html')

def payment(request):
    return render(request, "app/payment.html")


def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            message.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request, 'app/register.html')


def about(request):
    return render(request, "app/about.html")


def hotels(request):
    amenities_objs = Amenities.objects.all()
    hotel_objs = Hotel.objects.all()
    context = {'amenities_objs': amenities_objs, 'hotel_objs': hotel_objs}
    return render(request, "app/hotels.html", context)


def package(request):
    extras = Extras.objects.all()
    package_objs = Package.objects.all()
    context = {'amenities_objs': extras, 'package_objs': package_objs}
    return render(request, "app/packages.html",context)


def message(request):
    return render(request, "app/messages.html")


def contact(request):
    return render(request, "app/contact.html")
