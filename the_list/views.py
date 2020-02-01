from django.shortcuts import render
from .models import ListItem


# Create your views here.
def index(request):
    the_list = ListItem.objects.all()
    return render(request, 'the_list/index.html', {'the_list': the_list})
