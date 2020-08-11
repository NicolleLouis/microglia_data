from enum import Enum


class Stage(Enum):
    E12_5 = 'E12.5'
    E14_5 = 'E14.5'
    E16_5 = 'E16.5'
    E18_5 = 'E18.5'
    P0 = 'P0'
    P3 = 'P3'
    P5 = 'P5'
    P6 = 'P6'
    P7 = 'P7'
    P9 = 'P9'
    P14 = 'P14'
    P20 = 'P20'
    P60 = 'P60'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_all_stage(cls):
        return [key.value for key in cls]
