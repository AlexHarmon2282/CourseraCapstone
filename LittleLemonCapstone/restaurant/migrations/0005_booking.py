# Generated by Django 4.2.2 on 2023-06-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField()),
            ],
        ),
    ]
