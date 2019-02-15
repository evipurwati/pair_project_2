from django.contrib import admin        
from .models import Stuff, Category

my_model = [Stuff, Category]
admin.site.register(my_model)
