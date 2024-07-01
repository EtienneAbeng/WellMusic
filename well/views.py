from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser, Music
from .forms import CustomUserCreationForm, MusicForm

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
        form = CustomUserCreationForm(request.POST)
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
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def upload_music(request):
    """View function for handling music upload."""
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new music instance but don't save it yet
            music = form.save(commit=False)
            # Assign the current logged-in user as the uploader
            music.uploaded_by = request.user
            music.save()
            return redirect('home')
    else:
        form = MusicForm()
    return render(request, 'upload_music.html', {'form': form})

def list_music(request):
    """View function for listing user's uploaded music."""
    musics = Music.objects.filter(uploaded_by=request.user)
    return render(request, 'list_music.html', {'musics': musics})
