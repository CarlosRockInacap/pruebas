# Generated by Django 5.1.1 on 2024-11-25 23:07

import core.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_usuario_qr_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locomocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metro', models.CharField(blank=True, max_length=100, null=True)),
                ('transantiago', models.CharField(blank=True, max_length=100, null=True)),
                ('colectivos', models.CharField(blank=True, max_length=100, null=True)),
                ('taxi', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LugarInteres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='qr',
            name='mapa',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_to_map),
        ),
        migrations.AddField(
            model_name='qr',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_to_qr),
        ),
        migrations.AddField(
            model_name='qr',
            name='seguridad',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='qr',
            name='locomocion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.locomocion'),
        ),
        migrations.AddField(
            model_name='qr',
            name='lugares_interes',
            field=models.ManyToManyField(blank=True, to='core.lugarinteres'),
        ),
        migrations.AddField(
            model_name='qr',
            name='negocios',
            field=models.ManyToManyField(blank=True, to='core.negocio'),
        ),
        migrations.AddField(
            model_name='qr',
            name='servicios',
            field=models.ManyToManyField(blank=True, to='core.servicio'),
        ),
    ]
