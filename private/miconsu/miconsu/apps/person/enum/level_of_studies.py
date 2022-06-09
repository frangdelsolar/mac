from enum import Enum

class LevelOfStudiesEnum(Enum):
    ILLITERATE = 'Analfabeto'
    PRIMARY_INCOMPLETE = 'Primario incompleto'
    PRIMARY_COMPLETE = 'Primario completo'
    SECONDARY_INCOMPLETE = 'Secundario incompleto'
    SECONDARY_COMPLETE = 'Secundario completo'
    TERTIARY_INCOMPLETE = 'Terciario incompleto'
    TERTIARY_COMPLETE = 'Terciario completo'