# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


@login_required
def feeds(request):
    posts = Post.objects.all().order_by('-created')  # Order by creation date (newest first)
    return render(request, "feeds.html", {"posts": posts})



@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Post added successfully")
            return redirect("../")
        else:
            messages.error(request, "Error adding post. Please check the form.")
    else:
        form = PostForm()

    return render(request, "create.html", {"form": form})
