# Generated by Django 2.2.3 on 2022-10-19 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicio', '0003_auto_20221008_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ofensiva',
            old_name='partidos',
            new_name='partido',
        ),
        migrations.RemoveField(
            model_name='ofensiva',
            name='p_fail',
        ),
        migrations.RemoveField(
            model_name='ofensiva',
            name='perdidas_b',
        ),
    ]
