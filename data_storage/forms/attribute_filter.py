from django import forms

from data_storage.models.brain_quantification import BrainQuantification


class AttributeFilterForm(forms.Form):
    attribute = forms.ChoiceField(
        choices=BrainQuantification.get_all_attributes()
    )
