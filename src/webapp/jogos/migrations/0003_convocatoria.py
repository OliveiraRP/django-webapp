# Generated by Django 3.1.4 on 2020-12-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipas', '0001_initial'),
        ('jogos', '0002_auto_20201221_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('equipa', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='equipas.equipa')),
            ],
            options={
                'db_table': 'convocatoria',
                'managed': False,
            },
        ),
    ]
