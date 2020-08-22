from enum import Enum


class Sex(Enum):
    Male = 'Male'
    Female = 'Female'
    Unknown = 'Unknown'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_all_sex(cls):
        return [key.value for key in cls]
