# Generated by Django 4.0.6 on 2022-07-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuariosApp', '0002_alter_estudios_options_alter_experiencia_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudios',
            name='fechas',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='fechas',
            field=models.DateTimeField(),
        ),
    ]
