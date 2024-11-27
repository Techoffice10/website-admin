from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse
from .forms import UserInfoForm, BillingModelForm
from .models import BillingModel
from .models import UserInfo
from django.contrib import messages
from django.db.models import Q

User = get_user_model()

# Dashboard view with user creation
@login_required
def dashboard(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            messages.success(request, 'Records saved successfully!')
            return redirect('dashboard')  # Redirect to dashboard after saving
        else:
            messages.error(request, 'There was an error in the form submission.')
    else:
        form = UserInfoForm()

    return render(request, 'core/dashboard.html', {'form': form})

# User creation view
def user_creation(request):
    return render(request, 'core/usercreation.html')

# Billing section view (handles search and form submission)
def billing_view(request):
    if request.method == 'POST':
        # Handling form submission (save)
        form = BillingModelForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Billing entry created successfully!')
            return redirect('billing')  # Redirect to the billing page or another view
        else:
            messages.error(request, 'There was an error in the billing form submission.')

    else:
        # Handling search request (GET)
        search_query = request.GET.get('search_query', '')  # Get the search query
        billing_data = None

        if search_query:
            # Search by ticket_id or invoice_no (case insensitive)
            billing_data = BillingModel.objects.filter(
                Q(ticket_id__icontains=search_query) | Q(invoice_no__icontains=search_query)
            ).first()  # Get the first match, or None if not found

        # If found, populate the form with existing details, else a fresh form
        form = BillingModelForm(instance=billing_data) if billing_data else BillingModelForm()

    return render(request, 'core/billing.html', {'form': form, 'billing_data': billing_data})


import logging

logger = logging.getLogger(__name__)

# Billing search view (to handle search via a GET request)
def search_billing(request):
    search_query = request.GET.get('search_query', '')
    billing_data = None

    if search_query:
        # Search for the billing entry by ticket_id or invoice_no
        billing_data = BillingModel.objects.filter(
            Q(ticket_id__icontains=search_query) | Q(invoice_no__icontains=search_query)
        )

    return render(request, 'core/billing.html', {'billing_data': billing_data, 'search_query': search_query})


# Billing SAVE view (to handle Save)
def save_billing(request):
    if request.method == 'POST':
        form = BillingModelForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Billing entry saved successfully!')
            return redirect('billing')  # Redirect to the billing page after saving
        else:
            messages.error(request, 'There was an error in the billing form submission.')

    else:
        form = BillingModelForm()

    return render(request, 'core/billing.html', {'form': form})





# Login view using Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'core/login.html'

# Logout view using Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('dashboard')

# Home view (for a welcome message or custom homepage)
def home(request):
    return HttpResponse("Welcome to my website!")

# Admin register view (admin registration)
def admin_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_superuser = True  # Make the user an admin
            user.is_staff = True  # Give the user access to the admin panel
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# Search user view
def search_user(request):
    search_query = request.GET.get('query', '')
    user_info = None

    if search_query:
        results = UserInfo.objects.filter(
            Q(user_name__icontains=search_query) | Q(node__icontains=search_query)
        ).first()

        if results:
            user_info = {
                'user_name': results.user_name,
                'full_name': results.full_name,
                'phone_no': results.phone_no,
                'email': results.email,
                'node': results.node,
                'branch': results.branch,
                'ext_no': results.ext_no,
                'port_ip': results.port_ip,
                'password': results.password,
                'power_broker_id': results.power_broker_id,
                'applied_rating_id': results.applied_rating_id,
                'user_creation_date': results.user_creation_date,
                'suspended_date': results.suspended_date,
                'status': results.status,
                'history': results.history
            }
        else:
            messages.error(request, 'No user found matching your search criteria.')
            user_info = None

    return render(request, 'core/dashboard.html', {'user_info': user_info})

# User logout view
def user_logout(request):
    logout(request)
    return redirect('login')
