from enum import Enum
from collections import namedtuple

"""
This module is a collection of all names of grammatical persons and tense endings.
"""


class GrammaticalPersons(Enum):
    PERSONS = ('Eu/I', 'Tu/You', 'Ele/Ela/você/He/She/It', 'Nós/We', 'Vós/You', "Eles/Elas/vocês/They")


class TenseEndings(Enum):
    Endings = namedtuple('Endings',
                         ('Presente_Indicativo', 'Pretérito_Perfeito', 'Pretérito_Imperfeito',
                          'Pretérito_Mais_Que_Perfeito', 'Presente_de_Subjuntivo', 'Pretérito_Imperfeito_de_Subjuntivo',
                          'Futuro_de_Subjuntivo'))

    ENDINGS_AR = Endings(('o', 'as', 'a', 'amos', 'ais', 'am'),
                         ('ei', 'aste', 'ou', 'amos', 'astes', 'aram'),
                         ('ava', 'avas', 'ava', 'ávamos', 'áveis', 'avam'),
                         ('ara', 'aras', 'ara', 'áramos', 'áreis', 'aram'),
                         ('e', 'es', 'e', 'emos', 'eis', 'em'),
                         ('asse', 'asses', 'asse', 'ássemos', 'ásseis', 'assem'),
                         ('ar', 'ares', 'ar', 'armos', 'ardes', 'arem')
                         )

    ENDINGS_ER = Endings(('o', 'es', 'e', 'emos', 'eis', 'em'),
                         ('i', 'este', 'eu', 'emos', 'estes', 'eram'),
                         ('ia', 'ias', 'ia', 'íamos', 'íeis', 'iam'),
                         ('era', 'eras', 'era', 'êramos', 'êreis', 'eram'),
                         ('a', 'as', 'a', 'amos', 'am'),
                         ('esse', 'esses', 'esse', 'êssemos', 'essem'),
                         ('er', 'eres', 'er', 'ermos', 'erdes', 'erem')
                         )

    ENDINGS_IR = Endings(('o', 'es', 'e', 'imos', 'em'),
                         ('i', 'iste', 'iu', 'imos', 'iram'),
                         ('ia', 'ias', 'ia', 'íamos', 'iam'),
                         ('ira', 'iras', 'ira', 'íramos', 'iram'),
                         ('a', 'as', 'a', 'amos', 'am'),
                         ('isse', 'isses', 'isse', 'íssemos', 'issem'),
                         ('ir', 'ires', 'ir', 'irmos', 'irdes', 'irem')
                         )

    CONDITIONAL_MOOD_AND_FUTURE_INDICATIVE_MOOD = namedtuple('NAME_FUTURE_CONDITIONAL',
                                                             'conditional future_simple')

    CONDITIONAL_AND_FUTURE_ENDINGS = CONDITIONAL_MOOD_AND_FUTURE_INDICATIVE_MOOD(
        ('ei', 'ás', 'á', 'emos', 'des', 'ão'), ('ia', 'ias', 'ia', 'íamos', 'íeis', 'iam'))

    # IMPERATIVE_MOOD = namedtuple('imperative_mood', 'affirmative_imperative negative_imperative')
    #
    # IMPERATIVE_ENDINGS = IMPERATIVE_MOOD()
