from enum import Enum


class SexForm(Enum):
    Empty = 'Empty'
    Male = 'Male'
    Female = 'Female'
    SexComparison = 'SexComparison'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_all_sex_form(cls):
        return [key.value for key in cls]

    @classmethod
    def choices_without_comparison(cls):
        return [(key.value, key.name) for key in cls if key.name != 'SexComparison']
