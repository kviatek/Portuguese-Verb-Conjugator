from enum import Enum


class GrammaticalPersons(Enum):
    first_person_sing = 'Eu/I'
    second_person_sing = 'Tu/You'
    third_person_sing = 'Ele/Ela/você/He/She/It'
    first_person_plural = 'Nós/We'
    second_person_plural = 'Else/Elas/vocês/They'


class GrammaticalEndings(Enum):

    # indicativo_presente_endings

    indicativo_presente_endings_ar = ('o', 'as', 'a', 'amos', 'am')
    indicativo_presente_endings_er = ('o', 'es', 'e', 'emos', 'em')
    indicativo_presente_endings_ir = ('o', 'es', 'e', 'imos', 'em')

    # preterito_perfeito_endings

    preterito_perfeito_endings_ar = ('ei', 'aste', 'ou', 'amos', 'aram')
    preterito_perfeito_endings_er = ('i', 'este', 'eu', 'emos', 'eram')
    preterito_perfeito_endings_ir = ('i', 'iste', 'iu', 'imos', 'iram')

    # preterito_imperfeito_endings

    preterito_imperfeito_endings_ar = ('ava', 'avas', 'ava', 'ávamos', 'avam')
    preterito_imperfeito_endings_er_ir = ('ia', 'ias', 'ia', 'íamos', 'iam')

    # futuro_simples_indicativo

    futuro_simples_indicativo_endings = ('ei', 'ás', 'á', 'emos', 'ão')

    # condicional_simples

    condicional_simples_endigns = ('ia', 'ias', 'ia', 'íamos', 'iam')
