# Generated by Django 3.0.4 on 2020-08-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_storage', '0003_auto_20200810_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brainquantificationimport',
            name='csv_file',
            field=models.FileField(upload_to='static/'),
        ),
    ]