# Generated by Django 2.1.5 on 2020-03-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zbozi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=30)),
                ('cena', models.FloatField(max_length=10)),
            ],
        ),
    ]
