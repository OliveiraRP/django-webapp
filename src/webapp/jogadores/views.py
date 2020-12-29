from django.shortcuts import render
from .forms import SearchJogadorForm
from .models import Jogador

# Create your views here.
def table_jogadores_view(request, *args, **kwargs):

	form = SearchJogadorForm()
	if request.method == 'POST': # Search Form
		form = SearchJogadorForm(request.POST)
		query = "SELECT * FROM search_jogador('" + request.POST['nome'] + "')"
		objects_jogadores = Jogador.objects.raw(query)

	else:
		objects_jogadores = Jogador.objects.all()

	context = {
		'objects_jogadores': objects_jogadores,
		'form': form
	}

	return render(request, "jogadores/table.html", context)


def dynamic_jogador_view(request, id):

	jogador = Jogador.objects.get(jogador_id=id)
	context = {
		"jogador": jogador
	}

	return render(request, "jogadores/perfil.html", context)