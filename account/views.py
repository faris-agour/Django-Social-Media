from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
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
from django.contrib.auth.decorators import login_required
from posts.models import Post  # Absolute import for Post model from the 'posts' app


def custom_logout_view(request):
    # Handle logout logic here (if needed)
    logout(request)
    # Render the logout.html template
    return render(request, 'registration/logout.html')



@login_required
def dashboard(request, user_id=None):
    if user_id is None:
        user_id = request.user.id

    user = get_object_or_404(User, id=user_id)
    my_posts = Post.objects.filter(user=user)
    received_friendships = user.received_friendships.filter(from_user=request.user, accepted=True)

    context = {
        'my_posts': my_posts,
        'user': user,
        'received_friendships': received_friendships,
    }

    return render(request, 'account/dashboard.html', context)


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
                return redirect("../")
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
            return redirect("../")
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

