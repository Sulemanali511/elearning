# Generated by Django 3.0 on 2019-12-07 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0006_auto_20191207_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='theme',
        ),
        migrations.AddField(
            model_name='cours',
            name='matiere',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cours', to='cours.Matieres'),
            preserve_default=False,
        ),
    ]
