from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(db_index=True, unique=True, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"
 
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
