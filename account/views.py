from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignUpForm


def custom_logout_view(request):
    # Handle logout logic here (if needed)
    logout(request)
    # Render the logout.html template
    return render(request, 'registration/logout.html')


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm  # Adjust this import based on your actual form location


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("../profile/")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})
