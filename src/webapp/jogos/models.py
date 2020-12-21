from django.db import models
from campeonatos.models import Campeonato
from equipas.models import Equipa
from jogadores.models import Jogador

# Create your models here.
class Jogo(models.Model):
    jogo_id = models.AutoField(primary_key=True)
    campeonato = models.ForeignKey(Campeonato, models.DO_NOTHING)
    tempojogo = models.CharField(max_length=20, blank=True, null=True)
    campo = models.CharField(max_length=50, blank=True, null=True)
    espetadores = models.IntegerField(blank=True, null=True)
    diajogo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogo'


class ParteJogo(models.Model):
    parte_jogo_id = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'parte_jogo'


class TipoEvento(models.Model):
    tipo_evento_id = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_evento'


class Evento(models.Model):
    evento_id = models.AutoField(primary_key=True)
    parte_jogo = models.ForeignKey(ParteJogo, models.DO_NOTHING)
    jogo = models.ForeignKey(Jogo, models.DO_NOTHING)
    jogador = models.ForeignKey(Jogador, models.DO_NOTHING)
    tipo_evento = models.ForeignKey(TipoEvento, models.DO_NOTHING)
    tempo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'       


class Resultado(models.Model):
    jogo = models.OneToOneField(Jogo, models.DO_NOTHING, primary_key=True)
    equipa = models.ForeignKey(Equipa, models.DO_NOTHING)
    resultado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultado'
        unique_together = (('jogo', 'equipa'),)


class Convocatoria(models.Model):
    equipa = models.OneToOneField(Equipa, models.DO_NOTHING, primary_key=True)
    jogador = models.ForeignKey(Jogador, models.DO_NOTHING)
    jogo = models.ForeignKey(Jogo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'convocatoria'
        unique_together = (('equipa', 'jogador', 'jogo'),)