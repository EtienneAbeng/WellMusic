import os
import django
from well.manage_users import create_user, get_user_by_id, update_user, delete_user, list_users

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wellmusic.settings')
django.setup()

# Create a new user
new_user = create_user('john_doe', 'password123')

# Read all users
users = list_users()
print(users)

# Read a specific user by ID
user = get_user_by_id(1)
print(user)

# Update an existing user
update_user(1, username='new_username')

# Delete a user
delete_user(1)
