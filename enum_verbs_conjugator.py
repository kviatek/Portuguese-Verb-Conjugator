from enum import Enum


# This module is a collection of all names of grammatical persons and tense endings.

class GrammaticalPersons(Enum):
    PERSONS = ['Eu/I', 'Tu/You', 'Ele/Ela/você/He/She/It', 'Nós/We', "Else/Elas/vocês/They"]


class TenseEndings(Enum):

    ENDINGS_AR = [['o', 'as', 'a', 'amos', 'am'],
                  ['ei', 'aste', 'ou', 'amos', 'aram'],
                  ['ava', 'avas', 'ava', 'ávamos', 'avam'],
                  ['ara', 'aras', 'ara', 'áramos', 'aram'],
                  ['e', 'es', 'e', 'emos', 'em'],
                  ['asse', 'asses', 'asse', 'ássemos', 'assem'],
                  ]

    ENDINGS_ER = [['o', 'es', 'e', 'emos', 'em'],
                  ['i', 'este', 'eu', 'emos', 'eram'],
                  ['ia', 'ias', 'ia', 'íamos', 'iam'],
                  ['era', 'eras', 'era', 'êramos', 'eram'],
                  ['a', 'as', 'a', 'amos', 'am'],
                  ['esse', 'esses', 'esse', 'êssemos', 'essem'],
                  ]

    ENDINGS_IR = [['o', 'es', 'e', 'imos', 'em'],
                  ['i', 'iste', 'iu', 'imos', 'iram'],
                  ['ia', 'ias', 'ia', 'íamos', 'iam'],
                  ['ira', 'iras', 'ira', 'íramos', 'iram'],
                  ['a', 'as', 'a', 'amos', 'am'],
                  ['isse', 'isses', 'isse', 'íssemos', 'issem'],
                  ]

    CONDICIONAL_AND_FUTURO_ENDINGS_COMMON_FOR_EVERY_ENDING = {
        'FUTURO_SIMPLES_INDICATIVO': ('ei', 'ás', 'á', 'emos', 'ão'),
        'CONDICIONAL_SIMPLES': ('ia', 'ias', 'ia', 'íamos', 'iam')}
