from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, SongForm
from .models import CustomUser, Song

def home(request):
    """View function for rendering the home page."""
    return render(request, 'home.html')

def login_view(request):
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

@login_required
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user
            song.save()
            messages.success(request, 'Song uploaded successfully.')
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'upload.html', {'form': form})

def player(request):
    """View function for rendering the player page."""
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'player.html')

def search(request):
    query = request.GET.get('q')
    if query:
        songs = Song.objects.filter(title__icontains=query)
    else:
        songs = []
    return render(request, 'player.html', {'songs': songs})
