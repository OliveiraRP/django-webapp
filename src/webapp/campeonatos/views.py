from django.shortcuts import render
from .models import Campeonato
from equipas.models import Equipa
from jogadores.models import Jogador

# Create your views here.
def table_campeonatos_view(request, *args, **kwargs):

	objects_campeonatos = Campeonato.objects.raw('SELECT * FROM list_campeonatos')

	context = {
	'objects_campeonatos': objects_campeonatos,
	}

	return render(request, "campeonatos/table.html", context)


def campeonato_view(request, id):

	campeonato = Campeonato.objects.get(campeonato_id=id)

	top_marc = 0
	top_adfut = 0
	top_ad = 0

	if campeonato.modalidade_id == 1:
		classific = Equipa.objects.raw("SELECT * FROM Classificacao_fut("+str(id)+")")
		top_marc = Jogador.objects.raw("SELECT * FROM melhores_marcadores("+str(id)+")")
		top_adfut = Jogador.objects.raw("SELECT * FROM mais_cartoes("+str(id)+")")
	elif campeonato.modalidade_id == 2:
		classific = Equipa.objects.raw("SELECT * FROM Classificacao_basquet("+str(id)+")")
		top_marc = Jogador.objects.raw("SELECT * FROM melhores_marcadores_basquet("+str(id)+")")
		top_ad = Jogador.objects.raw("SELECT * FROM mais_exclusoes("+str(id)+")")
	elif campeonato.modalidade_id == 3:
		classific = Equipa.objects.raw("SELECT * FROM Classificacao_andebol("+str(id)+")")
		top_marc = Jogador.objects.raw("SELECT * FROM melhores_marcadores_volei("+str(id)+")")
		top_ad = Jogador.objects.raw("SELECT * FROM mais_exclusoes("+str(id)+")")
	elif campeonato.modalidade_id == 4:
		classific = Equipa.objects.raw("SELECT * FROM torneio_tenis("+str(id)+")")
	elif campeonato.modalidade_id == 5:
		classific = Equipa.objects.raw("SELECT * FROM Classificacao_basquet("+str(id)+")")
		top_marc = Jogador.objects.raw("SELECT * FROM melhores_marcadores_volei("+str(id)+")")
		top_ad = Jogador.objects.raw("SELECT * FROM mais_exclusoes("+str(id)+")")

	vencedor = Equipa.objects.get(equipa_id = classific[0].equipa_id)

	context = {
	'campeonato': campeonato,
	'classific': classific,
	'vencedor': vencedor,
	'top_marc': top_marc,
	'top_ad': top_ad,
	'top_adfut': top_adfut
	}

	return render(request, "campeonatos/camp.html", context)