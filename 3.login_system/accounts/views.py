from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login
            messages.success(request, f'Account created successfully!')
            return redirect('dashboard')   # ✅ login না, dashboard
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required(login_url='login')   # ✅ BEST PRACTICE
def profile_view(request):
    return render(request, 'accounts/profile.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')   # already logged → dashboard

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')  # ✅ dashboard এ পাঠাবে
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('dashboard')   # logout হলে dashboard


@login_required
def session_view(request):
    session_key= request.session.session_key
    user_id=request.session.get('_auth_user_id')
    response = f"""
        <p> Session Key: {session_key}</p>
        <p> User ID: {user_id} </p>
    """
    return HttpResponse(response)

def reset_password_view(request):
    # This view will be handled by Django's built-in PasswordResetView
    pass