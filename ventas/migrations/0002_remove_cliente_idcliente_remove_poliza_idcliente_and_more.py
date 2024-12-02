# Generated by Django 5.1.3 on 2024-11-28 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='idcliente',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='idcliente',
        ),
        migrations.CreateModel(
            name='ObjetoAsegurado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idobjeto', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('placa', models.CharField(max_length=10)),
                ('numpoliza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.poliza')),
            ],
        ),
    ]
