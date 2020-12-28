from django.shortcuts import render
from .models import Jogador

# Create your views here.
def table_jogadores_view(request, *args, **kwargs):

	objects_jogadores = Jogador.objects.raw('SELECT * FROM Jogador')

	context = {
	'objects_jogadores': objects_jogadores,
	}

	return render(request, "jogadores/table.html", context)


def dynamic_jogador_view(request, id):

	jogador = Jogador.objects.get(jogador_id=id)
	context = {
		"jogador": jogador
	}

	return render(request, "jogadores/perfil.html", context)