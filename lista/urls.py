# crud

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('add_item/', views.add_item, name='add_item'),
    path('itens/<int:id>/', views.itens, name='ver_item'),
    path('deleteitem/<int:id>/', views.delete_item, name='delete_item'),
    path('updateitem/<int:id>/', views.updateitem, name='update_item'),
]