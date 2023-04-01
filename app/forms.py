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
    gender = forms.ChoiceField(label="Gender",choices=[('male','Male'),('female','Female'),('other','Other')], widget=forms.RadioSelect)
    class Meta:
        model = Booking
        fields = '__all__'
        labels = {
            'name': '',
            'gender': '',
            'email': '',
            'telephone': '',
            'people': '',
            'hotel_name': ''
        }
        abstract = True
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Enter Your name', 'required': True}),
            # 'gender': forms.TextInput(
            #     attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Select Your gender',
            #            'required': True}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': True}),
            'telephone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your phone number', 'required': True}),
            'people': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'For how many people', 'required': True}),
            'hotel_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter hotel name', 'required': True}),
            # 'startdate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Starting date'}),
            # 'enddate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ending date date'}),
        }


class PackageForm(forms.ModelForm):
    gender = forms.ChoiceField(label="Gender", choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                               widget=forms.RadioSelect)
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
            'name': forms.TextInput(
                attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Enter Your name', 'required': True}),
            # 'gender': forms.TextInput(
            #     attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Select Your gender',
            #            'required': True}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': True}),
            'telephone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your phone number', 'required': True}),
            'package_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter package name', 'required': True}),
            'people': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'For how many people', 'required': True}),
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
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}), }
