# Generated by Django 2.2 on 2020-05-14 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('nombre', models.CharField(max_length=20)),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=20)),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('titulo', models.CharField(max_length=20)),
                ('editorial', models.CharField(max_length=20)),
                ('paginas', models.IntegerField(max_length=20)),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('localizacion', models.CharField(max_length=20)),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Usuario')),
            ],
        ),
    ]
