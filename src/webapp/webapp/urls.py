"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import index_view, changelog_view, xml_view
from campeonatos.views import table_campeonatos_view, campeonato_view
from jogos.views import table_jogos_view, game_jogos_view
from equipas.views import table_equipas_view, team_equipas_view
from jogadores.views import table_jogadores_view, profile_jogador_view, new_jogador_view

urlpatterns = [
	path('', index_view, name='index'),
    path('changelog/', changelog_view, name='changelog'),
    path('xml/', xml_view, name='xml'),
	path('campeonatos/', table_campeonatos_view, name='campeonatos'),
    path('campeonatos/<int:id>', campeonato_view, name='campeonato_campeonatos'),
    path('jogos/', table_jogos_view, name='jogos'),
    path('jogos/<int:id>', game_jogos_view, name='jogo_jogos'),
    path('equipas/', table_equipas_view, name='equipas'),
    path('equipas/<int:id>', team_equipas_view, name='equipa_equipas'),
    path('jogadores/', table_jogadores_view, name='jogadores'),
    path('jogadores/<int:id>', profile_jogador_view, name="perfil_jogador"),
    path('jogadores/novo', new_jogador_view, name="novo_jogador"),
    path('admin/', admin.site.urls),
]
