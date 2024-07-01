from django.urls import path
from . import views

urlpatterns = [
    # URL patterns mapped to respective view functions
    path('', views.home, name='home'),        # Home page
    path('login/', views.login_view, name='login'),     # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('signup/', views.signup_view, name='signup'),  # Signup page
]