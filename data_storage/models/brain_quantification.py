from django.db import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.stage import Stage

csv_order = [
    "ki_pos",
    "ki_neg",
    "zone",
    "sub_zone",
    "area",
    "brain_name",
    "stage",
    "slice_thickness",
]

class BrainQuantification(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    ki_pos = models.IntegerField(
        blank=True,
        null=True
    )
    ki_neg = models.IntegerField(
        blank=True,
        null=True
    )
    zone = models.CharField(
        max_length=12,
        choices=BrainZone.choices(),
    )
    sub_zone = models.CharField(
        max_length=12,
        choices=BrainSubZone.choices(),
        default=BrainSubZone.Empty
    )
    area = models.FloatField(
        blank=True,
        null=True
    )
    brain_name = models.CharField(
        max_length=20,
        default=""
    )
    stage = models.CharField(
        max_length=20,
        choices=Stage.choices()
    )
    slice_thickness = models.IntegerField(
        blank=True,
        null=True
    )

    def to_csv(self):
        return list(map(lambda field_name: str(self.__getattribute__(field_name)), csv_order))


class BrainQuantificationResource(resources.ModelResource):
    class Meta:
        model = BrainQuantification


class BrainQuantificationAdmin(ImportExportModelAdmin):
    resource_class = BrainQuantificationResource

    list_display = (
        "stage",
        "zone",
        "sub_zone",
        "ki_pos",
        "ki_neg"
    )
