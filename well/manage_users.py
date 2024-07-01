from django.contrib.auth.hashers import make_password
from .models import CustomUser

def create_user(username, password):
    hashed_password = make_password(password)
    return CustomUser.objects.create(username=username, password=hashed_password)

def get_user_by_id(user_id):
    try:
        return CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return None

def update_user(user_id, **kwargs):
    try:
        user = CustomUser.objects.get(id=user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user
    except CustomUser.DoesNotExist:
        return None

def delete_user(user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()
    except CustomUser.DoesNotExist:
        pass

def list_users():
    return CustomUser.objects.all()
