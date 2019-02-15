from django.shortcuts import render
from .models import Stuff, Category
# from .form import PostStuff

def shop(request) :
    category = Category.objects.all()
    stuffs = Stuff.objects.all()
    return render(request, 'shop.html', {'stuffs' : stuffs, 'category':category})

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
    category = Category.objects.all()
    stuffs = Stuff.objects.get(pk=stuff_id)
    return render(request, 'detail_stuff.html', {'stuff': stuffs, 'category':category})

def show_by_category(request, category_id) :
    category = Category.objects.all()
    stuffs = Stuff.objects.filter(kategori=category_id)
    return render(request, 'show_by_category.html', {'stuffs': stuffs, 'category':category})