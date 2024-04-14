from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm  # Adjust this import based on your actual form location
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, ProfileEditForm, UserEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileEditForm, UserEditForm  # Adjust the import based on your actual forms



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
                Profile.objects.create(user=user)
                return redirect("../profile/")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})



@login_required
def edit(request):
    if request.method == "POST":
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated ' 'successfully')
        else:
            messages.error(request, 'Error updating your profile')
            # Redirect to a success page or another view
            # return redirect("profile")  # Replace with the name of your profile view
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
