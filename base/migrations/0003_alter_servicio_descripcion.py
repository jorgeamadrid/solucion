# Generated by Django 5.1.6 on 2025-02-14 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_categoria_servicio_miembro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
