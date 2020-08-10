from enum import Enum


class BrainSubZone(Enum):
    Empty = ''
    MZ = 'MZ'
    II_III = 'II_III'
    IV = 'IV'
    V = 'V'
    VI = 'VI'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
