# Generated by Django 3.0.3 on 2021-03-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210316_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diplomebacplus2',
            name='lp',
        ),
        migrations.AddField(
            model_name='diplomebacplus2',
            name='lp',
            field=models.ManyToManyField(to='pages.LPs'),
        ),
    ]
