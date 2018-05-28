from enum import Enum


# This module is a collection of all names of grammatical persons and tense endings.

class GrammaticalPersons(Enum):
    PERSONS = ('Eu/I', 'Tu/You', 'Ele/Ela/você/He/She/It', 'Nós/We', "Else/Elas/vocês/They")


class TenseEndings(Enum):
    AR_ENDINGS = {'INDICATIVO PRESENTE': ('o', 'as', 'a', 'amos', 'am'),
                  'PRETERITO_PERFEITO_INDICATIVO': ('ei', 'aste', 'ou', 'amos', 'aram'),
                  'PRETERITO_IMPERFEITO_INDICATIVO': ('ava', 'avas', 'ava', 'ávamos', 'avam'),
                  'PRETERITO_MAIS_QUE_PERFEITO': ('ara', 'aras', 'ara', 'áramos', 'aram'),
                  }

    ENDINGS_ER = {'INDICATIVO_PRESENTE': ('o', 'es', 'e', 'emos', 'em'),
                  'PRETERITO_PERFEITO_INDICATIVO': ('i', 'este', 'eu', 'emos', 'eram'),
                  'PRETERITO_IMPERFEITO_INDICATIVO': ('ia', 'ias', 'ia', 'íamos', 'iam'),
                  'PRETERITO_MAIS_QUE_PERFEITO': ('era', 'eras', 'era', 'êramos', 'eram'),
                  }

    ENDINGS_IR = {'INDICATIVO_PRESENTE': ('o', 'es', 'e', 'imos', 'em'),
                  'PRETERITO_PERFEITO_INDICATIVO': ('i', 'iste', 'iu', 'imos', 'iram'),
                  'PRETERITO_IMPERFEITO_INDICATIVO': ('ia', 'ias', 'ia', 'íamos', 'iam'),
                  'PRETERITO_MAIS_QUE_PERFEITO': ('ira', 'iras', 'ira', 'íramos', 'iram'),
                  }

    CONDICIONAL_AND_FUTURO_ENDINGS_COMMON_FOR_EVERY_ENDING = {
        'FUTURO_SIMPLES_INDICATIVO': ('ei', 'ás', 'á', 'emos', 'ão'),
        'CONDICIONAL_SIMPLES': ('ia', 'ias', 'ia', 'íamos', 'iam')}
