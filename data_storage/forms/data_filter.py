from django import forms

from data_storage.enums.stage import Stage
from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.brain_subzone import BrainSubZone


class DataFilterForm(forms.Form):
    stage = forms.MultipleChoiceField(
        choices=Stage.choices()
    )
    zone = forms.MultipleChoiceField(
        choices=BrainZone.choices()
    )
    sub_zone = forms.MultipleChoiceField(
        choices=BrainSubZone.choices()
    )
