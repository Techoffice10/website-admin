"""
URL configuration for website_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth import views as auth_views  # For user login/logout auth functionality
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.admin_register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Use the custom login view
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard URL
    #path('dashboard/usercreation/', views.user_creation, name='user_creation'),  # New User Creation URL
    path('dashboard/usercreation/', views.user_creation_view, name='user_creation'), # ========================New UserCreation.html form===========
    path('dashboard/billing/', views.billing_view, name='billing'),  # Billing form and search URL
    path('search_billing/', views.search_billing, name='search_billing'),  # Search billing entry
    path('save_billing/', views.save_billing, name='save_billing'),
    path('', include('core.urls')),  # Include core app URLs (if any)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Log out using Django's auth system
    path('search_user/', views.search_user, name='search_user'),  # Search user functionality
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'core/static')
