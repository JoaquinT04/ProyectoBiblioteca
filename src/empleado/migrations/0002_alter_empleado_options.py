# Generated by Django 4.2.1 on 2023-05-21 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['apellido', 'nombre']},
        ),
    ]
