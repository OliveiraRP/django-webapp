from django import forms

class SearchJogadorForm(forms.Form):
		nome = forms.CharField(label='',
			widget=forms.TextInput(attrs={'placeholder': 'Pesquisar jogador'}))