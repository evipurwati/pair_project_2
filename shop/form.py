from django import form
from .models import PostStuff

class StuffForm(forms.ModelForm) :
    class Meta :
        model = PostStuff
        fields = '__all__'