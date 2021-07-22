# Generated by Django 3.0.7 on 2021-05-23 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procesador',
            name='marca',
        ),
        migrations.AddField(
            model_name='procesador',
            name='marcaProcesador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.MarcaProcesador'),
        ),
    ]
