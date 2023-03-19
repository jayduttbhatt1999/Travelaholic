from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            message.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            message.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        return redirect('app:index')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'app/login.html')


def register_page(request):
    if request.method == 'POST':
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
    return render(request, "app/hotels.html")


def insurance(request):
    return render(request, "app/insurance.html")


def bloghome(request):
    return render(request, "app/blog-home.html")


def blogsingle(request):
    return render(request, "app/blog-single.html")


def package(request):
    return render(request, "app/packages.html")


def elements(request):
    return render(request, "app/elements.html")


def message(request):
    return render(request, "app/messages.html")

def logout(request):
    return redirect('app:login')
