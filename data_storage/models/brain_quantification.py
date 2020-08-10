from django.db import models
from django.contrib import admin


from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.brain_subzone import BrainSubZone


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
    Area = models.FloatField(
        blank=True,
        null=True
    )


class BrainQuantificationAdmin(admin.ModelAdmin):
    list_display = (
        "zone",
        "sub_zone",
        "ki_pos",
        "ki_neg"
    )
