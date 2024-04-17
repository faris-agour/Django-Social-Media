from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['body', 'image', 'created','slug']
    list_filter = ['created']

