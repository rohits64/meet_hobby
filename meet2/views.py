from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from . forms import *
from . models import *

def home(request):
    return render(request, 'home.html')

def signup(request):
    form = SignUpForm(request.POST)
    profile_form = ProfileForm(request.POST)

    if form.is_valid() and profile_form.is_valid():
        user = form.save()
        user.refresh_from_db()

        user.profile.AddressRoomNo = profile_form.cleaned_data.get('AddressRoomNo')
        user.profile.AddressHall = profile_form.cleaned_data.get('AddressHall')
        user.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')    
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'form':form, 'profile_form':profile_form})        

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect('index')
            else:
                messages.error(request, "Invaild username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "login.html", context={"form":form}) 


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('home')

def index(request):
    user = request.user
    if user.username and user.is_superuser is False:
        return render(request, 'index.html')
    else:
        messages.warning(request, 'You are not logged in. Please login') 
        return redirect('home')  

def show_joined_group(request):
    user = request.user                                     
    GM = GroupMembers.objects.filter(UserId=user)

    user_groups = []
    for x in GM:
        user_groups.append(x.GroupId)
    return render(request, 'show_group.html', {'user_groups':user_groups})

def show_new_group(request):
    user = request.user

    GM = GroupMembers.objects.filter(UserId=user)

    user_groups = []
    for x in GM:
        user_groups.append(x.GroupId)

    all_groups = Group.objects.all()

    new_groups = []

    for group in all_groups:
        if group not in user_groups:
            new_groups.append(group)
    print(new_groups)        

    return render(request, 'new_group.html', {'new_groups':new_groups})

def join_group(request, id):
    user = request.user   
    if user.username:
        cur_group = Group.objects.get(GroupId = id)

        new_member = GroupMembers()
        new_member.GroupId = cur_group
        new_member.UserId = user
        new_member.save()


        return redirect(show_joined_group)
    else:
        messages.warning(request, 'You are not logged in. Please login')
        return redirect('home')    

    
