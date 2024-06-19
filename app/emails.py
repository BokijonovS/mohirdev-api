from django.core.mail import send_mail
from django.conf import settings
from .models import User


def send_update_email(user_email, subject, message):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
