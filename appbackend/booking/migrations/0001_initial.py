# Generated by Django 2.2.13 on 2020-07-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('moviename', models.CharField(max_length=25)),
                ('screenname', models.CharField(max_length=25)),
                ('eventname', models.CharField(max_length=25)),
                ('timing', models.CharField(max_length=25)),
                ('seatclass', models.CharField(max_length=5)),
                ('showtime', models.CharField(max_length=25)),
                ('timestamp', models.TimeField(auto_now_add=True)),
                ('seat', models.IntegerField(default=10)),
                ('cost', models.IntegerField(default=10)),
                ('eventtype', models.CharField(max_length=25)),
            ],
        ),
    ]
