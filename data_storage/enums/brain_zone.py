from enum import Enum


class BrainZone(Enum):
    Cortex = 'Cortex'
    POA = 'POA'
    Striatum = 'Striatum'
    Hippocampus = 'Hippocampus'
    Triangulo = 'Triangulo'
    DG = 'DG'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
