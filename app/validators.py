from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_unique_email(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError(f"Email address %s already exists." % value)


def validate_unique_username(value):
    exist = User.objects.filter(username=value)
    if exist:
        raise ValidationError(f"Username %s already exists." % value)
