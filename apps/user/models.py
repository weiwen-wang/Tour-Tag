from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('guide', 'guide'),
        ('driver', 'driver')
    )
    user_type = models.CharField(verbose_name='User Type', choices=USER_TYPE_CHOICES, max_length=6)
