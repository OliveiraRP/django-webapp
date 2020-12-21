from django.db import models

# Create your models here.
class Jogador(models.Model):
    jogador_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=5, blank=True, null=True)
    datanasc = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogador'