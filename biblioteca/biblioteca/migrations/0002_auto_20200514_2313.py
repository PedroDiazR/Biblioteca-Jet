# Generated by Django 2.2 on 2020-05-14 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplar',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='ejemplar',
            field=models.ManyToManyField(to='biblioteca.Ejemplar'),
        ),
    ]
