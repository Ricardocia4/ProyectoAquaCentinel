# accounts/urls.py
from django.urls import path
from .forms import RegistrationForm
from .views import signUp


urlpatterns = [
    path("signup/", signUp, name="signup"),
]