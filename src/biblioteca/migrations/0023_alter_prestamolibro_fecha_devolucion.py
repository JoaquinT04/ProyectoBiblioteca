# Generated by Django 4.2.1 on 2023-06-07 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0022_alter_prestamolibro_fecha_devolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamolibro',
            name='fecha_devolucion',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 23, 31, 49, 687423, tzinfo=datetime.timezone.utc)),
        ),
    ]
