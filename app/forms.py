from django.forms import ModelForm
from django import forms

from app.models import Contact


class Usermessage(ModelForm):
    name = forms.TextInput()
    email_id = forms.TextInput()
    subject = forms.TextInput()
    message = forms.TextInput()

    class Meta:
        model = Contact
        fields = ['name','email_id','subject','subject']