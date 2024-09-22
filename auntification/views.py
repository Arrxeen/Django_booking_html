from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from auntification.forms import CustomeUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('room-list')
        else:
            messages.error(request,"some error ")
    else:
        form = CustomeUserCreationForm()
    
    return render(
        request,
        template_name="auntification/register.html",
        context={"form": form}
    )
    
def login_system(request):
    if request.method == "POST":
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('room-list')
            else:
                messages.error(request,"Wrong password or login")
    else:
        form_login = AuthenticationForm()
    return render(
        request,
        template_name= "auntification/login_system.html",
        context= {"form": form_login}
    )

def logout_system(request):
    logout(request)
    return redirect('room-list')