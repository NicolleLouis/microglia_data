from django.db import models
from django.contrib import admin


class BrainQuantificationImport(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    csv_file = models.FileField()


class BrainQuantificationImportAdmin(admin.ModelAdmin):
    list_display = (
        "csv_file",
    )
