# Generated by Django 5.1.6 on 2025-02-14 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_servicio_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
