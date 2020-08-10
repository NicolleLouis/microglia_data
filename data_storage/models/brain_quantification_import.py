import csv

from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

from data_storage.service.file_service import FileService


class BrainQuantificationImport(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    csv_file = models.FileField(
        upload_to='static/'
    )


class BrainQuantificationImportAdmin(admin.ModelAdmin):
    list_display = (
        "csv_file",
    )


@receiver(post_save, sender=BrainQuantificationImport)
def save_csv(sender, instance, **kwargs):
    with instance.csv_file.open('r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = []
        for row in csv_reader:
            data.append(row)
    FileService.delete_all_static_files()

