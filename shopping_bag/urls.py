from django.urls import path
from . import views

urlpatterns = [
    path('bag', views.view_shopping_bag, name='bag'),
    path('add_item/<int:product_id>', views.add_to_shopping_bag, name='add_item'),
    path('delete_item/<int:pid>', views.delete_from_shopping_bag, name='delete_item'),
    path('updatebag', views.update_bag, name='updatebag'),
]
