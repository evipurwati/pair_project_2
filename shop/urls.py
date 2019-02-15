from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    # path('form', views.input_post, name='input_post'),
    path('shop/<int:stuff_id>', views.detail_stuff, name='detail_stuff'),
    path('category/<int:category_id>', views.show_by_category, name='show_by_category'),
]