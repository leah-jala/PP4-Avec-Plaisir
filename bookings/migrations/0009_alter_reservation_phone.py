# Generated by Django 3.2.16 on 2023-01-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_alter_reservation_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
