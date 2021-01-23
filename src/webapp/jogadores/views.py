from django.shortcuts import render
from django.db import connection
from .forms import JogadorForm, SearchJogadorForm
from .models import Jogador
from equipas.models import Plantel, Equipa
from jogos.models import Convocatoria, Evento

# Create your views here.
def table_jogadores_view(request, *args, **kwargs):

	form = SearchJogadorForm()
	if request.method == 'POST': # Search Form
		form = SearchJogadorForm(request.POST)
		objects_jogadores = Jogador.objects.raw("SELECT * FROM search_jogador('" + request.POST['nome'] + "')")

	else:
		objects_jogadores = Jogador.objects.all()

	context = {
		'objects_jogadores': objects_jogadores,
		'form': form
	}

	return render(request, "jogadores/table.html", context)


def profile_jogador_view(request, id):

	jogador = Jogador.objects.get(jogador_id=id)
	
	# List equipas
	lista_equipas = Plantel.objects.raw("SELECT * FROM get_equipa_by_jogador(" + str(id) + ")")

	# List estatísticas
	stats_futebol = []
	stats_basquetebol = []
	stats_voleibol = []
	stats_tenis = []
	stats_andebol = []

	for equipa in lista_equipas:
		if equipa.modalidade == 'Futebol':
			stats_futebol = Convocatoria.objects.raw("SELECT * FROM get_estatisticas_jogador_futebol(" + str(id) + ")")
		elif equipa.modalidade == 'Basquetebol':
			stats_basquetebol = Convocatoria.objects.raw("SELECT * FROM get_estatisticas_jogador_basquetebol(" + str(id) + ")")
		elif equipa.modalidade == 'Ténis':
			stats_tenis = Convocatoria.objects.raw("SELECT * FROM get_estatisticas_jogador_tenis(" + str(id) + ")")
		elif equipa.modalidade == 'Voleibol':
			stats_voleibol = Convocatoria.objects.raw("SELECT * FROM get_estatisticas_jogador_voleibol(" + str(id) + ")")
		elif equipa.modalidade == 'Andebol':
			stats_andebol = Convocatoria.objects.raw("SELECT * FROM get_estatisticas_jogador_andebol(" + str(id) + ")")

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM get_idade("+str(id)+")")
		idade = cursor.fetchone()[0]
		cursor.execute("SELECT * FROM get_total_jogos_jogador("+str(id)+")")
		total_jogos = cursor.fetchone()[0]
		cursor.execute("SELECT * FROM get_total_golos("+str(id)+")")
		total_golos = cursor.fetchone()[0]
		cursor.execute("SELECT * FROM get_total_carama("+str(id)+")")
		total_carama = cursor.fetchone()[0]
		cursor.execute("SELECT * FROM get_total_carver("+str(id)+")")
		total_carver = cursor.fetchone()[0]


	# List eventos
	eventos = Evento.objects.raw("SELECT * FROM get_eventos_jogador(" + str(id) + ")")

	# Delete jogador
	if request.method == 'POST':
		with connection.cursor() as cursor:
			cursor.execute("CALL delete_jogador(" + str(id) + ")")

	context = {
		"lista_equipas": lista_equipas,
		"stats_futebol": stats_futebol,
		"stats_basquetebol": stats_basquetebol,
		"stats_voleibol": stats_voleibol,
		"stats_tenis": stats_tenis,
		"stats_andebol": stats_andebol,
		"idade": idade,
		"total_golos": total_golos,
		"total_carver": total_carver,
		"total_carama": total_carama,
		"total_jogos": total_jogos,
		"eventos": eventos,
		"jogador": jogador
	}

	return render(request, "jogadores/profile.html", context)


def new_jogador_view(request):

	form = JogadorForm(request.POST or None)
	if form.is_valid():
		nome = form.cleaned_data['nome']
		genero = form.cleaned_data['genero']
		datanasc = str(form.cleaned_data['datanasc'])
		with connection.cursor() as cursor:
			cursor.execute("CALL insert_jogador('" + nome + "','" + genero + "','" + datanasc + "')")


	context = {
		'form': form
	}

	return render(request, "jogadores/new.html", context)