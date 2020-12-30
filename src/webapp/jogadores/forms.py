from django import forms
from .models import Jogador

class JogadorForm(forms.ModelForm):
	class Meta:
		model = Jogador
		exclude = ['jogador_id']


class SearchJogadorForm(forms.Form):
		nome = forms.CharField(label='',
			widget=forms.TextInput(attrs={'placeholder': 'Pesquisar jogador'}))