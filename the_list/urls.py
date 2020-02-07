from django.urls import path

from . import views

app_name = 'the_list'
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_item, name='add_item'),
]
