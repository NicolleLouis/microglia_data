from django import forms

from data_storage.enums.brain_subzone import BrainSubZone
from data_storage.enums.brain_zone import BrainZone
from data_storage.enums.sex_form import SexForm
from data_storage.models.brain_quantification import BrainQuantification


class AttributeZoneSubzoneSexForm(forms.Form):
    attribute = forms.ChoiceField(
        choices=BrainQuantification.get_all_numeric_attributes()
    )
    zone = forms.ChoiceField(
        choices=BrainZone.choices()
    )
    sub_zone = forms.ChoiceField(
        choices=BrainSubZone.choices()
    )
    sex = forms.ChoiceField(
        choices=SexForm.choices_without_comparison()
    )

