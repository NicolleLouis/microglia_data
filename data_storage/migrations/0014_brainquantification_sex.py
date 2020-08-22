# Generated by Django 3.0.4 on 2020-08-22 12:01

import data_storage.enums.sex
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_storage', '0013_auto_20200822_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='brainquantification',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown')], default=data_storage.enums.sex.Sex['Unknown'], max_length=20),
        ),
    ]
