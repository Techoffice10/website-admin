# core/forms.py
from django import forms
from .models import UserInfo
from .models import BillingModel

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


class BillingModelForm(forms.ModelForm):
    class Meta:
        model = BillingModel
        fields = ['client_name', 'client_address', 'billing_to', 'service_type', 'bill_description', 'ticket_id',  
                  'comments', 'emailed', 'invoice_no', 'invoice_date' ]
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'input-field'}),
            'client_address': forms.TextInput(attrs={'class': 'input-field'}),
            'billing_to': forms.TextInput(attrs={'class': 'input-field'}),
            'service_type': forms.TextInput(attrs={'class': 'input-field'}),
            'bill_description': forms.TextInput(attrs={'class': 'input-field'}),
            'ticket_id': forms.NumberInput(attrs={'class': 'input-field'}),
            'comments': forms.TextInput(attrs={'class': 'input-field'}),
            'emailed': forms.TextInput(attrs={'class': 'input-field'}),
            'invoice_no': forms.NumberInput(attrs={'class': 'input-field'}),
            'invoice_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'input-field'}),

        }


# Custom field for 'emailed' as a choice field
    emailed = forms.ChoiceField(
        choices=[('YES', 'Yes'), ('NO', 'No')],
        widget=forms.Select(attrs={'class': 'input-field'}),
        initial='NO'
    )



# If you have another form, like YourForm, this should be left as is, assuming it's a different use case.
class YourForm(forms.Form):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'In-active'),
        ('hold', 'Hold'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select)



#=============For new usercreation.html=============================


    



