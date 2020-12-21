from django.shortcuts import render
from .models import Campeonato

# Create your views here.
def table_campeonatos_view(request, *args, **kwargs):

	objects_campeonatos = Campeonato.objects.raw('SELECT * FROM Campeonato')

	context = {
	'objects_campeonatos': objects_campeonatos,
	}

	return render(request, "campeonatos/table.html", context)