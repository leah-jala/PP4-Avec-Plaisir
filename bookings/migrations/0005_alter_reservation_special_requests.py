# Generated by Django 3.2.16 on 2023-01-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_reservation_number_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='special_requests',
            field=models.TextField(blank=True),
        ),
    ]
