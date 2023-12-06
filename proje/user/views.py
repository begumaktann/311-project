from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def register(request):
    if request.method== 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('home')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page, change 'genel:home' to your desired URL name
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    u_form=UserUpdateForm()

    context = {
        'u_form': u_form,
    }
    return render(request,"profile.html",context)

@login_required
def user_logout(request):
    logout(request)
    return redirect("home")


def profile(request):
    return render(request,"profile.html")