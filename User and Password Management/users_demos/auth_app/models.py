# auth models/ models.py

from django.contrib.auth import models as auth_models
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from users_demos.auth_app.managers import AppUserManager


# variant s PROXY
# tuk trqbva da ima SAMO informaciq za authentication-a
# class AppUser(User):
#     def has_email(self):
#         return self.email or False
#
#     class Meta:
#         proxy = True


# variant s NASLEDQVANE i extending
# class AppUser(AbstractUser):
#     age = models.PositiveIntegerField()


# nai dobre e da napravim variant s custom user ! Nasledqvame AbstractBaseUser
# ot AbstractUser vzimame kakvoto ni e neobhodimo i ako trqbvaa go prenapisvame
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    # user credentials consists of email and password
    USERNAME_FIELD = 'email'
    objects = AppUserManager()
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )
    last_name = models.CharField(
        max_length=25,
    )
    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
