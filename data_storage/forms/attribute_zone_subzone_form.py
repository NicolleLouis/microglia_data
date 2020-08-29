from django import forms

from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.brain_zone import BrainZone
from data_storage.models.brain_quantification import BrainQuantification


class AttributeZoneSubzoneForm(forms.Form):
    attribute = forms.ChoiceField(
        choices=BrainQuantification.get_all_attributes()
    )
    zone = forms.MultipleChoiceField(
        choices=BrainZone.choices()
    )
    sub_zone = forms.MultipleChoiceField(
        choices=BrainSubZone.choices()
    )

