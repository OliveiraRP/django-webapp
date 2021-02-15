from django.shortcuts import render
from django.db import connection
from .models import Jogo, Evento, Resultado, Equipa

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

	equipas = Equipa.objects.raw("SELECT equipa_id FROM resultado WHERE jogo_id = " + str(id))

	e1 = str(equipas[0].equipa_id)
	e2 = str(equipas[1].equipa_id)

	if request.method == 'POST':
		with connection.cursor() as cursor:
			cursor.execute("CALL trocar_jogadores("+e1+","+e2+")")

	eventos = Evento.objects.raw("SELECT * FROM get_eventos_por_jogo("+str(id)+")")

	context = {
	'jogo': jogo,
	'result': result,
	'eventos': eventos
	}

	return render(request, "jogos/game.html", context)