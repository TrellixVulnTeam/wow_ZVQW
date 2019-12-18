from django.shortcuts import render
from .models import Dinolist

# Create your views here.
def dlist(request):
	dinolists = Dinolist.objects

	return render(request, 'list.html',
	{'dinolists' : dinolists.all })

