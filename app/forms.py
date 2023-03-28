from django.forms import ModelForm
from django import forms

from .models import Contact, Booking, Packbook


# class Usermessage(ModelForm):
# name = forms.CharField(required=True)
# email_id = forms.EmailField(required=True)
# subject = forms.CharField(required=True)
# message = forms.CharField(required=True)

# class Meta:
#     model = Contact
#     fields = ['name', 'email_id', 'subject', 'subject']
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        labels = {
            'name': '',
            'gender': '',
            'email': '',
            'telephone': '',
            'people': '',
            # 'ishotel_name':''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Enter Your name required' }),
            'gender': forms.TextInput(attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Select Your gender required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email required'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number required'}),
            'people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For how many people required'}),
            # 'ishotel_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hotel name'}),
            # 'startdate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Starting date'}),
            # 'enddate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ending date date'}),
        }


class PackageForm(forms.ModelForm):
    class Meta:
        model = Packbook
        fields = '__all__'
        labels = {
            'name': '',
            'gender': '',
            'email': '',
            'telephone': '',
            'package_name': '',
            'people': '',

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Enter Your name' }),
            'gender': forms.TextInput(attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Select Your gender'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'package_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter package name'}),
            'people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For how many people'}),
            # 'startdate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Starting date'}),
            # 'enddate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ending date date'}),
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': '',
            'email_id': '',
            'subject': '',
            'message': '',
        },
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter The Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),}
