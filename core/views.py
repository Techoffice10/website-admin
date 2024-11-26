from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse
from .forms import UserInfoForm, BillingModelForm
from .models import UserInfo
from django.contrib import messages
from django.db.models import Q

User = get_user_model()

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

def user_creation(request):
    return render(request, 'core/usercreation.html')

def billing(request):
    return render(request, 'core/billing.html')

def billing_view(request):
    if request.method == 'POST':
        form = BillingModelForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Billing entry created successfully!')
            return redirect('billing')  # Redirect to the billing page or another view
        else:
            messages.error(request, 'There was an error in the billing form submission.')
    else:
        form = BillingModelForm()

    return render(request, 'core/billing.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'core/login.html'

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('dashboard')

def home(request):
    return HttpResponse("Welcome to my website!")

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

def user_logout(request):
    logout(request)
    return redirect('login')
