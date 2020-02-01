from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import ListItem


# Create your views here.
def index(request):
    the_list = ListItem.objects.all()
    return render(request, 'the_list/index.html', {'the_list': the_list})


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
