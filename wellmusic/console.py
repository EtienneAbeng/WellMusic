import os
import django
from well.models import CustomUser

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wellmusic.settings')
django.setup()

# Create a new user
new_user = CustomUser.objects.create(username='john_doe', password='password123')

# Read all users
users = CustomUser.objects.all()
print(users)

# Read a specific user by ID
user = CustomUser.objects.get(id=1)
print(user)

# Update an existing user
user.username = 'new_username'
user.save()

# Delete a user
user.delete()
