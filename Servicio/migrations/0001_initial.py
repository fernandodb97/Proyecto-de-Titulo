# Generated by Django 2.2.3 on 2022-06-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defensiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.CharField(max_length=30)),
                ('entradas', models.IntegerField()),
                ('intercepcion', models.IntegerField()),
                ('despeje', models.IntegerField()),
                ('bloqueos', models.IntegerField()),
                ('faltas', models.IntegerField()),
                ('partido', models.CharField(max_length=2)),
                ('sustituto', models.BooleanField()),
            ],
            options={
                'verbose_name': 'defensiva',
                'verbose_name_plural': 'defensivas',
            },
        ),
        migrations.CreateModel(
            name='Distribucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.CharField(max_length=30)),
                ('pases', models.IntegerField()),
                ('p_preciso', models.IntegerField()),
                ('p_clave', models.IntegerField()),
                ('centros', models.IntegerField()),
                ('centro_preciso', models.IntegerField()),
                ('p_largo', models.IntegerField()),
                ('p_largo_preciso', models.IntegerField()),
                ('p_hueco', models.IntegerField()),
                ('p_hueco_preciso', models.IntegerField()),
                ('partido', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'distribucion',
                'verbose_name_plural': 'distribuciones',
            },
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.CharField(max_length=30)),
                ('posicion', models.CharField(max_length=20)),
                ('minutos', models.IntegerField()),
                ('partido', models.CharField(max_length=2)),
                ('sustituto', models.BooleanField()),
            ],
            options={
                'verbose_name': 'general',
                'verbose_name_plural': 'generales',
            },
        ),
        migrations.CreateModel(
            name='Ofensiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.CharField(max_length=30)),
                ('tiros', models.IntegerField()),
                ('t_preciso', models.IntegerField()),
                ('p_clave', models.IntegerField()),
                ('regates', models.IntegerField()),
                ('faltas_f', models.IntegerField()),
                ('offside', models.IntegerField()),
                ('perdidas_b', models.IntegerField()),
                ('p_fail', models.IntegerField()),
                ('goles', models.IntegerField()),
                ('asistencias', models.IntegerField()),
                ('partidos', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'ofensiva',
                'verbose_name_plural': 'ofensivas',
            },
        ),
    ]
