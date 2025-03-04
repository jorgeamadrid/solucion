# Generated by Django 5.1.6 on 2025-02-18 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_miembro_iglesia'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='miembro',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='miembro',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
