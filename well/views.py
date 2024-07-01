from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    """View function for rendering the home page."""
    return render(request, 'home.html')

def login_view(request):
    """View function for handling user login."""
    if request.method == 'POST':
        # Extract username and password
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user is authenticated, log them in and redirect to home
            login(request, user)
            return redirect('home')
        else:
            # Handle authentication failure
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    # Render the login form (GET request)
    return render(request, 'login.html')

def logout_view(request):
    """View function for handling user logout."""
    logout(request)
    return redirect('home')  # Redirect to home page after logout

def signup_view(request):
    """View function for handling user signup."""
    if request.method == 'POST':
        # Process the signup form if it's a POST request
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user and redirect to login page
            form.save()
            return redirect('login')
    else:
        # Display a blank signup form for GET requests
        form = UserCreationForm()
    # Render the signup form template with the form context
    return render(request, 'signup.html', {'form': form})