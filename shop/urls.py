from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.shop, name='shop'),
    path('shop/<int:stuff_id>', views.detail_stuff, name='detail_stuff'),
    path('category/<int:category_id>', views.show_by_category, name='show_by_category'),
]