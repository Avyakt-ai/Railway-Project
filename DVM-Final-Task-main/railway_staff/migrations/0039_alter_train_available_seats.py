# Generated by Django 4.2.7 on 2024-01-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0038_alter_train_departure_station_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='available_seats',
            field=models.IntegerField(default=50),
        ),
    ]