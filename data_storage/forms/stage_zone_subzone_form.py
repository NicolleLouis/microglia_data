from django import forms

from data_storage.enums.stage import Stage
from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.brain_subzone import BrainSubZone


class StageZoneSubzoneForm(forms.Form):
    stage = forms.ChoiceField(
        choices=Stage.choices()
    )
    zone = forms.ChoiceField(
        choices=BrainZone.choices()
    )
    sub_zone = forms.ChoiceField(
        choices=BrainSubZone.choices()
    )
