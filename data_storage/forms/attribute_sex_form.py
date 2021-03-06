from django import forms

from data_storage.enums.sex_form import SexForm
from data_storage.models.brain_quantification import BrainQuantification


class AttributeSexForm(forms.Form):
    attribute = forms.ChoiceField(
        choices=BrainQuantification.get_all_attributes()
    )
    sex = forms.ChoiceField(
        choices=SexForm.choices()
    )
