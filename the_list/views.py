from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, reverse
from .models import ListItem

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required

iterr = ['the_list.view_listitem', 'the_list.add_listitem']


# Create your views here.
@permission_required(iterr)
def home(request):
    the_list = ListItem.objects.all()
    return render(request, 'the_list/home.html', {'the_list': the_list})


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
@permission_required('the_list.add_listitem')
def add_item(request):
    if request.method == 'GET':
        return render(request, 'the_list/add_item.html')
    else:
        try:
            new_item_name = request.POST['item_name']
        except KeyError:
            print('BALLS!')
        else:
            ListItem(name=new_item_name).save()
            return HttpResponseRedirect(reverse('the_list:index'))
