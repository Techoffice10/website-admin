# core/forms.py
from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user_name', 'full_name', 'phone_no', 'email', 'node', 'branch', 'ext_no', 'port_ip', 
                  'password', 'power_broker_id', 'applied_rating_id', 'user_creation_date', 'suspended_date', 'status']



    # Optionally customize the widgets
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter user name'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter full name'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    node = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter node'}))
    branch = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter branch'}))
    ext_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter extension number'}))
    port_ip = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter port IP'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    power_broker_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter power broker ID'}))
    applied_rating_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter applied rating ID'}))
    user_creation_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'Enter creation date'}))
    suspended_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'Enter suspended date'}))
    status = forms.ChoiceField(choices=[('active', 'Active'), ('inactive', 'Inactive')])


class YourForm(forms.Form):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'In-active'),
        ('hold', 'Hold'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select)