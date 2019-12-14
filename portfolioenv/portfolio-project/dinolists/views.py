from django.shortcuts import render
from .models import Dinolist
# Create your views here.
def index(request):
	dinolists = Dinolist.objects

	return render(request, 'index.html', {'dinolists' : dinolists})
