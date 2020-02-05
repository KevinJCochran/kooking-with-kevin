from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, reverse
from .models import ListItem

from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    the_list = ListItem.objects.all()
    return render(request, 'the_list/index.html', {'the_list': the_list})


def start_session(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('the_list:index'))
    else:
        return HttpResponseForbidden()


# Render the add item page
def add_item(request):
    return render(request, 'the_list/add_item.html')


def save_item(request):
    try:
        new_item_name = request.POST['item_name']
    except KeyError:
        print('BALLS!')
    else:
        ListItem(name=new_item_name).save()
        return HttpResponseRedirect(reverse('the_list:index'))
