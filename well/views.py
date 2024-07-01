# well/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

def home(request):
    """View function for rendering the home page."""
    return render(request, 'home.html')

def login_view(request):
    """View function for handling user login."""
    if request.method == 'POST':
        # Extract username and password from POST data
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user is authenticated, log them in and redirect to home page
            login(request, user)
            return redirect('home')
        else:
            # If authentication fails, display error message
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    """View function for handling user logout."""
    logout(request)
    return redirect('home')

def signup_view(request):
    """View function for handling user signup."""
    if request.method == 'POST':
        # Process the signup form if it's a POST request
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            form.save()
            # Authenticate and log in the new user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        # Display a blank signup form for GET requests
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
