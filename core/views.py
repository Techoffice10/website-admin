from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .forms import UserInfoForm
from .models import UserInfo  # Assuming this is the model for the 'core_userinfo' table
from django.contrib import messages
from django.db.models import Q

User = get_user_model()


@login_required
def dashboard(request):
    # Handle form submission and save to database
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            messages.success(request, 'Records saved successfully!')
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = UserInfoForm()

    # Render the template from 'core/templates/core/dashboard.html'
    return render(request, 'core/dashboard.html', {'form': form})


# Custom login view to specify a custom template
class CustomLoginView(LoginView):
    template_name = 'core/login.html'


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        # Redirect to the dashboard after login
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
    search_query = request.GET.get('query', '')  # Get the search query from the frontend
    
    # Initialize an empty result for the form
    user_info = None

    if search_query:
        # Search by username or node (case insensitive)
        results = UserInfo.objects.filter(
            Q(user_name__icontains=search_query) | Q(node__icontains=search_query)
        ).first()  # Get the first match
        
        if results:
            # Prepare data to return to populate the form
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
                'user_creation_date': results.user_creation_date.strftime('%Y-%m-%d'),
                'suspended_date': results.suspended_date.strftime('%Y-%m-%d') if results.suspended_date else '',
                'status': results.status,
            }
        else:
            messages.error(request, 'No user found matching your search criteria.')
    
    # Return the search results to the frontend, populated in the form
    return render(request, 'core/dashboard.html', {'user_info': user_info})


# Sample view function
def user_logout(request):
    logout(request)  # This will log the user out
    return redirect('login')  # Redirect to the login page
