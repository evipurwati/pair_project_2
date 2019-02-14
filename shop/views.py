from django.shortcuts import render
from .models import Stuff
# from .form import PostStuff

def shop(request) :
    stuffs = Stuff.objects.all()
    return render(request, 'shop.html', {'stuffs' : stuffs})

# def stuff(request) :
#     stuff = StuffPost.objects.all()
#     return render(request, 'shop.html', {'stuff'} : {'stuff'})

# def input_stuff(request) :
#     if request.method == "POST" :
#         form = StuffPost(request.POST)
#         if form.is_valid() :
#             form.save()
#             return redirect('stuff')
#     else :
#         form = StuffPost())
#     return render(request, 'shop/shop.html', {'form' : form})

def detail_stuff(request, stuff_id) :
    stuffs = Stuff.objects.get(pk=stuff_id)
    return render(request, 'detail_stuff.html', {'stuff': stuffs})