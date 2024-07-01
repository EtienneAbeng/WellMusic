import django
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Wellcome in the WELLmusic !'
        message = 'Congratulation ! You are subcript in Wellmusic if you are this mail.'
        send_mail(
            subject,
            message,
            'your-email@example.com',
            [instance.email],
            fail_silently=False,
        )
