from django.shortcuts import render
from .models import Dinolist
# Create your views here.
def dlist(request):
	dinolists = Dinolist.objects.all

	print(dinolists)
	print("343242")

	return render(request, 'list.html', {'dinolists' : dinolists})
