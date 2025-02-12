from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from .models import UserProfile
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email

            if User.objects.filter(username=user.email).exists():
                messages.error(request, "This email is already used as a username.")
                return redirect('signup')

            user.save()

            if UserProfile.objects.filter(user=user).exists():
                messages.error(request, "A profile for this user already exists.")
                return redirect('signup')

            UserProfile.objects.create(user=user, 
                                       email=user.email, 
                                       full_name=form.cleaned_data['full_name'])

            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error(None, 'Invalid login credentials.')
            except User.DoesNotExist:
                form.add_error(None, 'No user with this email exists.')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def home_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'app/home.html', {'user_profile': user_profile})

def logout_view(request):
    logout(request)
    return redirect('login')
