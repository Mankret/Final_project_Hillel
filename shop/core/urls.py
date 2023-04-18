"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from shop_app.views import RegisterFormView, UserProfileView, UpdateProfileView, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop_app.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegisterFormView.as_view(), name="register"),
    path("accounts/profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("accounts/update_profile/", UpdateProfileView.as_view(), name="update_profile"),
    path("accounts/password", PasswordsChangeView.as_view(template_name='registration/change_password.html'),
         name='change_password'),

]
