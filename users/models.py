from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField('Phone Number', max_length=15)
    department = models.CharField('Department', max_length=50)
    designation = models.CharField('Designation', max_length=50)
