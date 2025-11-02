from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to home or another page
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
