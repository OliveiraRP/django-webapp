from django.shortcuts import render
from .models import Jogo

# Create your views here.
def table_jogos_view(request, *args, **kwargs):

	
	objects_jogos = Jogo.objects.raw('SELECT * FROM Jogo')

	context = {
	'objects_jogos': objects_jogos,
	}

	return render(request, "jogos/table.html", context)