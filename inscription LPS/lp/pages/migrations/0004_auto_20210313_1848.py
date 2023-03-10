# Generated by Django 3.0.3 on 2021-03-13 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210313_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidat',
            name='specialite',
        ),
        migrations.AddField(
            model_name='candidat',
            name='anneeObtentionDiplomeBacPlus2',
            field=models.CharField(choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')], default='2020', max_length=4),
        ),
        migrations.AddField(
            model_name='candidat',
            name='specialiteDiplome',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.Specialite'),
        ),
    ]
