# Generated by Django 2.0.4 on 2020-02-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0002_auto_20200206_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=20)),
                ('znacka', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='zanr',
        ),
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.DeleteModel(
            name='Zanr',
        ),
    ]
