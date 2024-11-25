from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can add extra fields here if necessary
    pass

# core/models.py
from django.db import models

class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    node = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    ext_no = models.CharField(max_length=50)
    port_ip = models.CharField(max_length=50)
    password = models.CharField(max_length=200)  # Or use Django's password hashing
    power_broker_id = models.CharField(max_length=50)
    applied_rating_id = models.CharField(max_length=50)
    user_creation_date = models.DateField()
    suspended_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
