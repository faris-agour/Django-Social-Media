from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/username/filename
    return f'users/{instance.user.username}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True,related_name="friends")
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return self.user.username
