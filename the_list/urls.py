from django.urls import path

from . import views

app_name = 'the_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_item, name='add_item'),
    path('save', views.save_item, name='save_item')
]
