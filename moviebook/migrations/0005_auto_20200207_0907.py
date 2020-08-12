# Generated by Django 2.1.5 on 2020-02-07 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0004_auto_20200207_0722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Film', 'verbose_name_plural': 'Filmy'},
        ),
        migrations.AlterModelOptions(
            name='zanr',
            options={'verbose_name': 'Žánr', 'verbose_name_plural': 'Žánry'},
        ),
        migrations.RemoveField(
            model_name='zanr',
            name='film',
        ),
        migrations.AddField(
            model_name='film',
            name='zanr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moviebook.Zanr', verbose_name='Žánr'),
        ),
        migrations.AlterField(
            model_name='film',
            name='nazev',
            field=models.CharField(max_length=200, verbose_name='Název Filmu'),
        ),
        migrations.AlterField(
            model_name='film',
            name='rezie',
            field=models.CharField(max_length=180, verbose_name='Režie'),
        ),
        migrations.AlterField(
            model_name='zanr',
            name='nazev_zanru',
            field=models.CharField(max_length=80, verbose_name='Žánr'),
        ),
    ]
