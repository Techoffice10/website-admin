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
                  'emailed', 'comments', 'invoice_no', 'invoice_date' ]
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'input-field'}),
            'client_address': forms.TextInput(attrs={'class': 'input-field'}),
            'billing_to': forms.TextInput(attrs={'class': 'input-field'}),
            'service_type': forms.TextInput(attrs={'class': 'input-field'}),
            'bill_description': forms.TextInput(attrs={'class': 'input-field'}),
            'ticket_id': forms.NumberInput(attrs={'class': 'input-field'}),
            'emailed': forms.TextInput(attrs={'class': 'input-field'}),
            'comments': forms.TextInput(attrs={'class': 'input-field'}),
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



#=======================================Form VALIDATIONS===============================================
#======================================================================================================

    # ***** START of Validation CODE's for Billing Form *****



    # Custom validation for client_name
    def clean_client_name(self):
        client_name = self.cleaned_data.get('client_name')
        if not client_name:
            raise forms.ValidationError("Client Name is required.")
        if len(client_name) < 3:
            raise forms.ValidationError("Client Name must be at least 3 characters long.")
        return client_name

    # Custom validation for client_address
    def clean_client_address(self):
        client_address = self.cleaned_data.get('client_address')
        if not client_address:
            raise forms.ValidationError("Client Address is required.")
        if len(client_address) < 10:
            raise forms.ValidationError("Client Address must be at least 10 characters long.")
        return client_address

    # Custom validation for billing_to
    def clean_billing_to(self):
        billing_to = self.cleaned_data.get('billing_to')
        if not billing_to:
            raise forms.ValidationError("Billing To is required.")
        return billing_to

    # Custom validation for service_type
    def clean_service_type(self):
        service_type = self.cleaned_data.get('service_type')
        if not service_type:
            raise forms.ValidationError("Service Type is required.")
        return service_type

    # Custom validation for bill_description
    def clean_bill_description(self):
        bill_description = self.cleaned_data.get('bill_description')
        if not bill_description:
            raise forms.ValidationError("Bill Description is required.")
        if len(bill_description) < 5:
            raise forms.ValidationError("Bill Description must be at least 5 characters long.")
        return bill_description
    
    # Custom validation for ticket_id
    def clean_ticket_id(self):
        ticket_id = self.cleaned_data.get('ticket_id')
        if not ticket_id:
            raise forms.ValidationError("Ticket ID is required.")
        return ticket_id


    # Custom validation for emailed
    def clean_emailed(self):
        emailed = self.cleaned_data.get('emailed')
        if emailed is None:
            raise forms.ValidationError("Please indicate whether the bill has been emailed.")
        return emailed

    # Custom validation for comments (optional field)
    def clean_comments(self):
        comments = self.cleaned_data.get('comments')
        if comments and len(comments) < 5:
            raise forms.ValidationError("Comments must be at least 5 characters long.")
        return comments

    
    # ***** END of Validation CODE for Billing Form *****
    



