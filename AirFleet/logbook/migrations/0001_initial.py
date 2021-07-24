# Generated by Django 3.2.5 on 2021-07-24 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copilot_name', models.CharField(blank=True, max_length=200)),
                ('rental_company', models.CharField(blank=True, max_length=200)),
                ('flight_date', models.DateField(auto_now_add=True)),
                ('manufacturer', models.CharField(max_length=200)),
                ('aircraft_model', models.CharField(max_length=200)),
                ('aircraft_id_num', models.CharField(blank=True, max_length=10)),
                ('from_dest', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(regex='!@#$%^&*()_-+=~`:;,<.>/?""')])),
                ('to_dest', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(regex='!@#$%^&*()_-+=~`:;,<.>/?""1234567890')])),
                ('duration', models.DurationField()),
                ('category_and_class', models.CharField(max_length=100)),
                ('remarks_and_endorsements', models.CharField(max_length=1000)),
                ('picture_with_plane', models.ImageField(blank=True, upload_to='aircraft_images')),
            ],
        ),
    ]