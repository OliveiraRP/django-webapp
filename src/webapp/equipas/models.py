from django.db import models
from jogadores.models import Jogador

# Create your models here.
class Equipa(models.Model):
    equipa_id = models.AutoField(primary_key=True)
    faixa_etaria = models.ForeignKey('FaixaEtaria', models.DO_NOTHING)
    genero = models.ForeignKey('Genero', models.DO_NOTHING)
    modalidade = models.ForeignKey('Modalidade', models.DO_NOTHING)
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'equipa'


class FaixaEtaria(models.Model):
    faixa_etaria_id = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'faixa_etaria'


class Genero(models.Model):
    genero_id = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'genero'


class Plantel(models.Model):
    equipa = models.OneToOneField(Equipa, models.DO_NOTHING, primary_key=True)
    jogador = models.ForeignKey(Jogador, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'plantel'
        unique_together = (('equipa', 'jogador'),)


class Modalidade(models.Model):
    modalidade_id = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'modalidade'                          