from django.contrib import admin
import django.contrib.auth.models
from django.contrib import auth

from data_storage.models.brain_quantification import BrainQuantification, BrainQuantificationAdmin

admin.site.register(BrainQuantification, BrainQuantificationAdmin)

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
