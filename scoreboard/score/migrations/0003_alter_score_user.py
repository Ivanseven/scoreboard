# Generated by Django 4.1.7 on 2023-04-05 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('score', '0002_rename_score_score_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player'),
        ),
    ]
