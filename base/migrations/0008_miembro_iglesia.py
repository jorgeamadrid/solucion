# Generated by Django 5.1.6 on 2025-02-17 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_categoria_servicio_id_iglesia_servicio_id_iglesia'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='iglesia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.iglesia'),
            preserve_default=False,
        ),
    ]
