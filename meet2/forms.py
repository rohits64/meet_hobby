from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    UserName = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=200)
    AddressRoomNo = forms.CharField(max_length=60)
    AddressHall = forms.CharField(max_length=60)
    

    class Meta:
        model = User
        fields = ('username', 'AddressRoomNo', 'AddressHall', 'email', 'password1', 'password2', )