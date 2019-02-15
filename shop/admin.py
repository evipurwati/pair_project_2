from django.contrib import admin        
from .models import Stuff

my_model = [Stuff]
admin.site.register(my_model)
