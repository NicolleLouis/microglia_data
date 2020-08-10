from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

from data_storage.service.csv_reader_service import CSVReaderService
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
    data = CSVReaderService.get_data_from_csv(instance.csv_file)
    CSVReaderService.save_brain_quantification_from_csv_data(data)
    FileService.delete_all_static_files()

