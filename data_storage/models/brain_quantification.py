from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.stage import Stage
from data_storage.enums.sex import Sex

csv_order = [
    "ki_pos_updated",
    "ki_pos",
    "ki_neg_updated",
    "ki_neg",
    "zone",
    "sub_zone",
    "area_measure",
    "area",
    "brain_name",
    "stage",
    "slice_thickness",
    "total",
    "percent_ki_67",
    "density",
    "density_ki67",
    "sex",
]


class BrainQuantification(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    ki_pos = models.IntegerField(
        blank=True,
        null=True
    )
    ki_pos_updated = models.FloatField(
        blank=True,
        null=True
    )
    ki_neg = models.IntegerField(
        blank=True,
        null=True
    )
    ki_neg_updated = models.FloatField(
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
    area_measure = models.FloatField(
        blank=True,
        null=True
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
    sex = models.CharField(
        max_length=20,
        choices=Sex.choices(),
        default=Sex.Unknown
    )
    slice_thickness = models.IntegerField(
        blank=True,
        null=True,
        default=60
    )
    total = models.FloatField(
        blank=True,
        null=True
    )
    percent_ki_67 = models.FloatField(
        blank=True,
        null=True
    )
    density = models.FloatField(
        blank=True,
        null=True
    )
    density_ki67 = models.FloatField(
        blank=True,
        null=True
    )

    @classmethod
    def get_all_attributes(cls):
        all_fields = cls._meta.fields
        return [(field.name, field.name) for field in all_fields]

    @classmethod
    def get_all_numeric_attributes(cls):
        all_fields = cls._meta.fields
        return [(field.name, field.name) for field in all_fields if
                field.get_internal_type() in ["FloatField", "IntegerField"]]

    def to_csv(self):
        return list(map(lambda field_name: str(self.__getattribute__(field_name)), csv_order))


class BrainQuantificationResource(resources.ModelResource):
    class Meta:
        model = BrainQuantification


class BrainQuantificationAdmin(ImportExportModelAdmin):
    resource_class = BrainQuantificationResource

    list_display = (
        'brain_name',
        "stage",
        "zone",
        "sub_zone",
        "sex",
    )


@receiver(pre_save, sender=BrainQuantification)
def compute_calculated_values(sender, instance, **kwargs):
    from data_storage.service.brain_quantification import BrainQuantificationService
    BrainQuantificationService.compute_calculated_values(instance)
