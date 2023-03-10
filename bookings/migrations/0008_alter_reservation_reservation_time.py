# Generated by Django 3.2.16 on 2023-01-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_reservation_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_time',
            field=models.IntegerField(choices=[(1, '10:00'), (2, '10:30'), (3, '11:00'), (4, '11:30'), (5, '12:00'), (6, '12:30'), (7, '13:00'), (8, '13:30'), (9, '14:00'), (10, '18:00'), (11, '18:30'), (12, '19:00'), (13, '19:30'), (14, '20:00'), (15, '20:30')], default=1),
        ),
    ]
