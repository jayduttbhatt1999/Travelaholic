import form as form
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ContactUsForm, BookingForm, PackageForm
from .models import Amenities, Hotel, Extras, Package, Contact
from django import forms
from django.core.mail import send_mail


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


def hotelbooking(request):
    return render(request, "app/hotelbooking.html")


@login_required
def profile(request):
    return render(request, 'app/profile.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            messages.warning(request, 'Please register here')
            # return redirect('app:register_page')
            return HttpResponseRedirect(reverse('app:register_page'))

        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)

        return HttpResponseRedirect(reverse('app:index'))
    return render(request, 'app/login.html')


def logout_page(request):
    logout(request)
    return render(request, 'app/index.html')


def payment(request):
    return render(request, "app/payment.html")


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('app:login')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'app/register.html')


def about(request):
    return render(request, "app/about.html")


def hotels(request):
    amenities_objs = Amenities.objects.all()
    package_objs = Package.objects.all()
    hotel_objs = Hotel.objects.all()
    context = {'amenities_objs': amenities_objs, 'hotel_objs': hotel_objs, 'package_objs': package_objs}
    return render(request, "app/hotels.html", context)


def package(request):
    extras = Extras.objects.all()
    package_objs = Package.objects.all()
    context = {'extra_amenities_objs': extras, 'package_objs': package_objs}
    return render(request, "app/packages.html", context)


def message(request):
    return render(request, "app/messages.html")


def book(request):
    # request.session['hotelID'] = pkg_id
    # pkg = Hotel.objects.get(uuid=pkg_id)
    if (request.method == 'POST'):

        form3 = BookingForm(request.POST)
        if form3.is_valid():
            form3.save()
            # form4 = BookingForm()
            messages.success(request, "Booking Confirmed")
            return HttpResponseRedirect(reverse('app:book'))
    else:
        form6 = BookingForm()
        return render(request, 'app/book.html', {'form1': form6})
    return render(request, 'app/book.html', {'form1': form3})
    # return render(request, "app/book.html")


def packbook(request):
    # request.session['hotelID'] = pkg_id
    # pkg = Hotel.objects.get(uuid=pkg_id)
    if request.method == 'POST':
        form3 = PackageForm(request.POST)
        if form3.is_valid():
            form3.save()
            # form4 = BookingForm()
            messages.success(request, "Package Booking Confirmed")
            return HttpResponseRedirect(reverse('app:book'))
    else:
        form6 = PackageForm()
        return render(request, 'app/bookpack.html', {'form2': form6})
    return render(request, 'app/bookpack.html', {'form2': form3})
    # return render(request, "app/book.html")


def contact(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form1 = ContactUsForm(request.POST)
        if form1.is_valid():
            form1.save()

            form2 = ContactUsForm()
            return render(request, 'app/contact.html', {'form': form2})
    else:
        # this must be a GET request, so create an empty form
        form5 = ContactUsForm()
        return render(request, 'app/contact.html', {'form': form5})
    # return render(request, "app/contact.html")


def booking(request, pkg_id):
    request.session['pkgID'] = pkg_id
    pkg = Package.objects.get(uuid=pkg_id)

    return render(request, "app/booking.html", {'package': pkg})


def confirm(request, pkg_id):
    request.session['pkgID'] = pkg_id
    name = request.POST['name']
    persons = int(request.POST['people'])
    email = request.POST['email']

    cost = (persons * Package.objects.get(uuid=pkg_id).package_price)

    send_mail('Confirm your booking', 'Make payment', 'hanikumari9831@gmail.com', [email.format(cost)],
              fail_silently=True)
    return render(request, "app/confirm.html", {'cost': cost, 'name': name, 'persons': persons, 'email': email})


def quebec(request):
    return render(request, "app/quebec.html")


def banff(request):
    return render(request, "app/banff.html")


def niagara(request):
    return render(request, "app/niagara.html")


def hotelconfirm(request, pkg_id):
    request.session['pkgID'] = pkg_id
    name = request.POST['name']
    numberOfPerson = int(request.POST['people'])
    email = request.POST['email']
    cost = (numberOfPerson * Hotel.objects.get(uuid=pkg_id).hotel_price)
    send_mail('Confirm your booking', 'Make payment', 'hanikumari9831@gmail.com', [email.format(cost)],
              fail_silently=True)
    return render(request, "app/confirm.html", {'cost': cost, 'name': name, 'persons': numberOfPerson, 'email': email})


def hotelbooking(request, pkg_id):
    request.session['hotelID'] = pkg_id
    pkg = Hotel.objects.get(uuid=pkg_id)

    return render(request, "app/hotelbooking.html", {'hotel': pkg})


def search_hotels(request):
    search = request.POST['search']
    amenities_objs = Amenities.objects.all()
    hotel_objs = Hotel.objects.filter(hotel_city=search)
    context = {'amenities_objs': amenities_objs, 'hotel_objs': hotel_objs}
    return render(request, "app/hotels.html", context)
