from enum import Enum


# This module is a collection of all names of grammatical persons and tense endings.


class GrammaticalPersons(Enum):
    PERSONS = ('Eu/I', 'Tu/You', 'Ele/Ela/você/He/She/It', 'Nós/We', "Else/Elas/vocês/They")


class TenseEndings(Enum):
    # indicativo_presente_endings

    INDICATIVO_PRESENTE_ENDINGS_AR = ('o', 'as', 'a', 'amos', 'am')
    INDICATIVO_PRESENTE_ENDINGS_ER = ('o', 'es', 'e', 'emos', 'em')
    INDICATIVO_PRESENTE_ENDINGS_IR = ('o', 'es', 'e', 'imos', 'em')

    # PAST TENSES
    # preterito_perfeito_endings

    PRETERITO_PERFEITO_INDICATIVO_ENDINGS_AR = ('ei', 'aste', 'ou', 'amos', 'aram')
    PRETERITO_PERFEITO_INDICATIVO_ENDINGS_ER = ('i', 'este', 'eu', 'emos', 'eram')
    PRETERITO_PERFEITO_INDICATIVO_ENDINGS_IR = ('i', 'iste', 'iu', 'imos', 'iram')

    # preterito_imperfeito_endings

    PRETERITO_IMPERFEITO_INDICATIVO_ENDINGS_AR = ('ava', 'avas', 'ava', 'ávamos', 'avam')
    PRETERITO_IMPERFEITO_INDICATIVO_ENDINGS_ER_IR = ('ia', 'ias', 'ia', 'íamos', 'iam')

    # preterito mais que perfeito_endings

    PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_AR = ('ara', 'aras', 'ara', 'áramos', 'aram')
    PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_ER = ('era', 'eras', 'era', 'êramos', 'eram')
    PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_IR = ('ira', 'iras', 'ira', 'íramos', 'iram')

    # futuro_simples_indicativo

    FUTURO_SIMPLES_INDICATIVO_ENDINGS = ('ei', 'ás', 'á', 'emos', 'ão')

    # condicional_simples

    CONDICIONAL_SIMPLES_ENDIGNS = ('ia', 'ias', 'ia', 'íamos', 'iam')
