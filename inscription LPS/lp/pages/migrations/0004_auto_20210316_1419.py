# Generated by Django 3.0.3 on 2021-03-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210316_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typebac',
            name='lp',
        ),
        migrations.AddField(
            model_name='typebac',
            name='lp',
            field=models.ManyToManyField(to='pages.LPs'),
        ),
    ]
