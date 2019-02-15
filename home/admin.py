from django.contrib import admin
from .models import Post, Category

# Register your models here.
post_model = [Post, Category]
admin.site.register(post_model)