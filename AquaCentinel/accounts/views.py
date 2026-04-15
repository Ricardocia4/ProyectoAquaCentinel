from django.shortcuts import render, redirect

# import login
from django.contrib.auth import login

# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

# our custom form


def signUp(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("/")

    else:
        form = RegistrationForm()

    return render(request, "registration/signup.html", {"form": form})
