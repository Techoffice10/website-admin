from django.contrib.auth.models import AbstractUser
from django.utils import timezone  # For timezone.now

# core/models.py
from django.db import models



class CustomUser(AbstractUser):
    # You can add extra fields here if necessary
    pass


class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    node = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    ext_no = models.CharField(max_length=15)
    port_ip = models.CharField(max_length=255)
    password = models.CharField(max_length=55)  # Or use Django's password hashing
    power_broker_id = models.CharField(max_length=50)
    applied_rating_id = models.CharField(max_length=50)
    user_creation_date = models.DateField()
    suspended_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)

class Meta:
        db_table = 'core_userinfo'  # specify the table name here

def __str__(self):
        return self.user_name
    


# Define choices for the 'emailed' field in Billing.html sheet
EMAILED_CHOICES = [
    ('YES', 'Yes'),
    ('NO', 'No'),
]

class BillingModel(models.Model):
    client_name = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)
    billing_to = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    bill_description = models.CharField(max_length=255)
    ticket_id = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    # Updated 'emailed' field to use choices for YES/NO
    emailed = models.CharField(
        max_length=3, 
        choices=EMAILED_CHOICES,  # Use choices for YES/NO
        default='NO'  # Default value is 'NO'
    )
    # Default value for 'comments' set to an empty string
    comments = models.CharField(max_length=255, default='No Comments')

    # Make 'invoice_no' and 'invoice_date' optional (allow null values)
    invoice_no = models.IntegerField(null=True, blank=True, default=None)
    invoice_date = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.client_name} - {self.service_type}'
