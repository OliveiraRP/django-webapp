from django.shortcuts import render
from .models import Equipa, Plantel
from jogos.models import Resultado
from jogadores.models import Jogador

# Create your views here.
def table_equipas_view(request, *args, **kwargs):

	objects_equipas = Equipa.objects.raw('SELECT * FROM Equipa')

	context = {
	'objects_equipas': objects_equipas,
	}

	return render(request, "equipas/table.html", context)


def team_equipas_view(request, id):

	equipa = Equipa.objects.get(equipa_id=id)

	plantel = Plantel.objects.raw("SELECT * FROM get_plantel(" + str(id) + ")")

	ultimos_resultados = Resultado.objects.raw("SELECT * FROM get_ultimos_resultados(" + str(id) + ")")

	mais_utilizados = Jogador.objects.raw("SELECT * FROM get_mais_utilizados(" + str(id) + ")")

	melhores_marcadores = Jogador.objects.raw("SELECT * FROM get_melhores_marcadores(" + str(id) + ")")

	context = {
		"equipa": equipa,
		"plantel": plantel,
		"ultimos_resultados": ultimos_resultados,
		"mais_utilizados": mais_utilizados,
		"melhores_marcadores": melhores_marcadores
	}

	return render(request, "equipas/team.html", context)