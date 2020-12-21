from django.db import models
from equipas.models import Equipa

# Create your models here.
class Campeonato(models.Model):
    campeonato_id = models.AutoField(primary_key=True)
    modalidade = models.ForeignKey('Modalidade', models.DO_NOTHING)
    nome = models.CharField(max_length=100)
    epoca = models.CharField(max_length=20)
    datainicio = models.DateField(blank=True, null=True)
    datafim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campeonato'


class Modalidade(models.Model):
    modalidade_id = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'modalidade'


class Participante(models.Model):
    equipa = models.OneToOneField(Equipa, models.DO_NOTHING, primary_key=True)
    campeonato = models.ForeignKey(Campeonato, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'participante'
        unique_together = (('equipa', 'campeonato'),)