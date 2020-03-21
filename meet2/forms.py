from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=60, help_text='Username')
    email = forms.EmailField(max_length=150, help_text='Email')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class ProfileForm(forms.Form):
    AddressRoomNo = forms.CharField(max_length=60)
    AddressHall = forms.CharField(max_length=60)

    
        

        