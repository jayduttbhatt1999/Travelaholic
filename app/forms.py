from django.forms import ModelForm
from django import forms

from .models import Contact, Booking, Packbook, Hotel


class BookingForm(forms.ModelForm):
    gender = forms.ChoiceField(label="Gender", choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                               widget=forms.RadioSelect)
    class Meta:
        model = Booking
        fields = '__all__'
        labels = {
            'name': '',
            'gender': '',
            'email': '',
            'telephone': '',
            'people': '',
            'hotel_name': 'Hotel name'
        }
        abstract = True
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Please enter Your name', 'required': True}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your email', 'required': True}),
            'telephone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number', 'required': True}),
            'people': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'For how many people?', 'required': True}),
            'hotel_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter hotel name?', 'required': True}),
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
            'pack_price':''

        }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'common-input mb-20 form-control', 'placeholder': 'Please enter Your name', 'required': True}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your email', 'required': True}),
            'telephone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number', 'required': True}),
            'package_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter package name', 'required': True}),
            'people': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'For how many people?', 'required': True}),
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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your message'}), }
