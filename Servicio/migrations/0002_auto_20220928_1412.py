# Generated by Django 2.2.3 on 2022-09-28 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defensiva',
            name='sustituto',
        ),
        migrations.RemoveField(
            model_name='distribucion',
            name='p_preciso',
        ),
    ]
