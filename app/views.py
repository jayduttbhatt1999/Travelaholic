#import form as form
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
#from django import forms
#from django.core.mail import send_mail


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


# def hotelbooking(request):
#     return render(request, "app/hotelbooking.html")


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
    if request.method == 'POST':

        form3 = BookingForm(request.POST)
        if form3.is_valid():
            form3.save()
            msg1 = "Thank you for booking with us, %s" % (form3.cleaned_data['name'])
            msg2 = "We are looking forward te meet you at %s" % (form3.cleaned_data['ishotel_name'])
            msg3 = "Your Confirmation and payment link will be sent to, %s" % (form3.cleaned_data['email'])
            # form4 = BookingForm()
            # messages.success(request, "Booking Confirmed")
            return render(request, 'app/confirm.html', {'form3': form3, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3})
    else:
        form6 = BookingForm()
        return render(request, 'app/book.html', {'form1': form6})
    return render(request, 'app/book.html', {'form1': form3})
    # return render(request, "app/book.html")


def packbook(request):
    # extras = Extras.objects.all()
    package_objs = Package.objects.all()
    # request.session['hotelID'] = pkg_id
    # pkg = Hotel.objects.get(uuid=pkg_id)
    if request.method == 'POST':
        form3 = PackageForm(request.POST)
        if form3.is_valid():
            form3.save()
            msg1 = "Thank you for booking with us, %s" % (form3.cleaned_data['name'])
            msg2 = "Your package is  %s" % (form3.cleaned_data['ispackage_name'])
            msg3 = "Your Confirmation and payment link will be sent to, %s" % (form3.cleaned_data['email'])
            # msg4 = "Your total amount is %s " % (form3.cleaned_data['package_objs.package_price'])
            # form4 = BookingForm()
            context = {'form3': form3, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3, 'package_objs': package_objs}
            return render(request, 'app/confirm1.html', context)
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


def quebec(request):
    return render(request, "app/quebec.html")


def banff(request):
    return render(request, "app/banff.html")


def niagara(request):
    return render(request, "app/niagara.html")


def search_hotels(request):
    search = request.POST['search']
    amenities_objs = Amenities.objects.all()
    hotel_objs = Hotel.objects.filter(hotel_city=search)
    context = {'amenities_objs': amenities_objs, 'hotel_objs': hotel_objs}
    return render(request, "app/hotels.html", context)
