from django.shortcuts import render
from django.db import connection
from .forms import JogadorForm, SearchJogadorForm
from .models import Jogador

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
	context = {
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