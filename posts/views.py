# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post, Friendship


@login_required
def feeds(request):
    friends_list = Friendship.objects.filter(from_user = request.user, accepted = True).values_list('to_user', flat=True)
    my_posts = Post.objects.filter(user = request.user)  # Order by creation date (newest first)
    friends_posts = Post.objects.filter(user__in=friends_list)  # Order by creation date (newest first)
    posts = my_posts | friends_posts
    posts = posts.order_by("-created")
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


@login_required
def add_friend(request, id):
    from_user = request.user
    to_user = get_object_or_404(User, id=id)
    friend_request, created = Friendship.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return messages.success(request, f"Friend request sent to {to_user.username}")
    else:
        return messages.info(request, "friend request was already sent!")


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User


@login_required
def add_friend(request, to_user_id):
    from_user = request.user
    to_user = get_object_or_404(User, id=to_user_id)

    # Check if friend request already exists
    friend_request, created = Friendship.objects.get_or_create(from_user=from_user, to_user=to_user)

    if created:
        messages.success(request, f"Friend request sent to {to_user.username}")
    elif friend_request.accepted:
        messages.info(request, f"{to_user.username} is already your friend!")
    else:
        messages.info(request, "Friend request was already sent!")

    return redirect('post:friends')


@login_required
def accept_friend(request, friendship_id):
    friend_request = get_object_or_404(Friendship, id=friendship_id, to_user=request.user)

    # Update friendship to accepted
    friend_request.accepted = True
    friend_request.save()

    messages.success(request, "Friend request accepted")
    return redirect('post:friends')


@login_required
def friends(request):
    # Get all accepted friendships where the logged-in user is the 'from_user'
    all_friends = Friendship.objects.filter(from_user=request.user, accepted=True)

    # Extract the 'to_user' from these friendships to get the list of friends
    friends_list = [friendship.to_user for friendship in all_friends]

    # Get all pending friend requests where the logged-in user is the 'to_user'
    friend_requests = Friendship.objects.filter(to_user=request.user, accepted=False)

    return render(request, 'friends.html', {'friends_list': friends_list, 'friend_requests': friend_requests})



@login_required
def search_for_friends(reqest):
    q = reqest.GET.get('query')
    if q:
        friends_list = User.objects.filter(
            Q(username__icontains=q)|
            Q(first_name__icontains=q)|
            Q(last_name__icontains=q)
        ).exclude(id = reqest.user.id)
    else:
        friends_list = []
    return render(reqest,"search_for_friends.html",{"friends_list":friends_list})