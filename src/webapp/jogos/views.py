from django.shortcuts import render
from .models import Jogo, Evento, Resultado

# Create your views here.
def table_jogos_view(request, *args, **kwargs):

	
	objects_jogos = Jogo.objects.raw('SELECT * FROM lista_jogos ORDER BY diajogo DESC')

	context = {
	'objects_jogos': objects_jogos,
	}

	return render(request, "jogos/table.html", context)


def game_jogos_view(request, id):

	jogo = Jogo.objects.get(jogo_id=id)

	result = Resultado.objects.raw("SELECT * FROM get_resultado_por_jogo("+str(id)+")")

	eventos = Evento.objects.raw("SELECT * FROM get_eventos_por_jogo("+str(id)+")")

	context = {
	'jogo': jogo,
	'result': result,
	'eventos': eventos
	}

	return render(request, "jogos/game.html", context)