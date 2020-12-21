from django.shortcuts import render
from .models import Equipa

# Create your views here.
def table_equipas_view(request, *args, **kwargs):

	objects_equipas = Equipa.objects.raw('SELECT * FROM Equipa')

	context = {
	'objects_equipas': objects_equipas,
	}

	return render(request, "equipas/table.html", context)