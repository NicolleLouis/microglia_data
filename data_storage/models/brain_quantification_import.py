from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.stage import Stage
from data_storage.service.csv_reader_service import CSVReaderService
from data_storage.service.file_service import FileService


class BrainQuantificationImport(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    csv_file = models.FileField(
        upload_to='static/'
    )
    stage = models.CharField(
        max_length=20,
        choices=Stage.choices()
    )
    slice_thickness = models.IntegerField(
        blank=True,
        null=True
    )
    zone = models.CharField(
        max_length=12,
        choices=BrainZone.choices(),
    )


class BrainQuantificationImportAdmin(admin.ModelAdmin):
    list_display = (
        "stage",
        "zone",
    )


@receiver(post_save, sender=BrainQuantificationImport)
def save_csv(sender, instance, **kwargs):
    data = CSVReaderService.get_data_from_csv(instance.csv_file)
    CSVReaderService.save_brain_quantification_from_csv_data(
        csv_data=data,
        stage=instance.stage,
        slice_thickness=instance.slice_thickness,
        zone=instance.zone,
        sub_zone=BrainSubZone.Empty.value,
    )
    FileService.delete_all_static_files()

