# Generated by Django 4.2.6 on 2023-10-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
