# Generated by Django 3.0.3 on 2021-03-16 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ville',
            name='etablissement',
        ),
        migrations.AddField(
            model_name='etablissementdipbacplus2',
            name='ville',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.Ville'),
        ),
    ]