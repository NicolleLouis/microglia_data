from django import forms

from data_storage.service.brain_quantification import BrainQuantificationService


class AttributeFilterForm(forms.Form):
    attribute = forms.ChoiceField(
        choices=BrainQuantificationService.get_all_attributes()
    )
