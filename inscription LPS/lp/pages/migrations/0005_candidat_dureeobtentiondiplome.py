# Generated by Django 3.0.3 on 2021-03-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210313_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidat',
            name='dureeObtentionDiplome',
            field=models.CharField(choices=[('2', '2'), ('3', '3')], default='2', max_length=1),
        ),
    ]