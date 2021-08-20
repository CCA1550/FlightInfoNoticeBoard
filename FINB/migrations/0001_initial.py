# Generated by Django 3.2.6 on 2021-08-20 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('entryTime', models.CharField(max_length=10)),
                ('takeOffTime', models.CharField(max_length=10)),
                ('SIDAps', models.CharField(max_length=10)),
                ('SIDApsICAO', models.CharField(max_length=10)),
                ('STARAps', models.CharField(max_length=10)),
                ('STARApsICAO', models.CharField(max_length=10)),
                ('flightDistance', models.CharField(max_length=10)),
                ('route', models.CharField(max_length=500)),
                ('planeType', models.CharField(max_length=50)),
                ('flightLevel', models.CharField(max_length=10)),
                ('cruiseSpeed', models.CharField(max_length=10)),
                ('remarks', models.CharField(max_length=500)),
            ],
        ),
    ]
