# Generated by Django 5.1.6 on 2025-02-18 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_miembro_activo_miembro_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol_ministerio',
            name='id_ministerio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles_disponibles', to='base.ministerio'),
        ),
    ]
