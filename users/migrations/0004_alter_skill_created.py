# Generated by Django 4.2.7 on 2023-12-02 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_ccreated_profile_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
