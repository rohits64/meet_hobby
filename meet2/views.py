from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            UserName = username
            # user.profile.email = form.cleaned_data.get('email')
            # user.profile.AddressRoomNo = form.cleaned_data.get('AddressRoomNo')
            # user.profile.AddressHall = form.cleaned_data.get('AddressHall')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})