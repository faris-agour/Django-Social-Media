from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("logged in successfully")
                else:
                    return HttpResponse("Disabled Account")
            else:
                # Use a proper error message for security reasons
                return HttpResponse("Wrong account or password")
    else:
        form = LoginForm()  # Instantiate the form outside of the 'POST' condition

    # If the form is invalid or it's a GET request, render the form template
    return render(request, "login.html", {'form': form})
