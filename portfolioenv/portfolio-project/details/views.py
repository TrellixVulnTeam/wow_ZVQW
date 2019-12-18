from django.shortcuts import render
from dinolists.models import Dinolist

# Create your views here.
def detail(request,name):

	dino = Dinolist.objects.get(name = name)
	return render(request,'index.html',
	{'name': dino.name ,
	'Overview':dino.overview, 
	'Character':dino.character, 
	'image':dino.image.url})

	