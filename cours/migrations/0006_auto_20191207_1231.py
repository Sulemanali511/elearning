# Generated by Django 3.0 on 2019-12-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0005_auto_20191207_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenuvideo',
            name='video_url',
            field=models.URLField(verbose_name="Ajouter l'url de la video"),
        ),
    ]
