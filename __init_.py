from pt_conjugator import enum_verbs_conjugator
from pt_conjugator import irregular_verbs_patterns
from pt_conjugator.enum_verbs_conjugator import TenseEndings


class NotInfinitiveError(ValueError):
    pass


def make_past_participle(word):
    """
    Method returns past participle form a verb
    :param word: verb whose past participle form need to be created
    :return: past participle form of a verb
    """
    if word.endswith('ar'):
        return word[:-2] + 'ado'
    elif word.endswith('er') or word.endswith('ir'):
        return word[:-2] + 'ido'


def pretérito_perfeito_composto(word):
    pass


def conjugate_add_endings_to_the_end(word):
    """
    The method conjugate verbs by adding to its root adequate grammatical endings.
    :param word: Verb to be conjugated
    :return: list of conjugated forms of all grammatical tenses
    """
    tenses_number = 2
    conjugated_forms = []

    for ending in enum_verbs_conjugator.TenseEndings.CONDICIONAL_AND_FUTURO_ENDINGS_COMMON_FOR_EVERY_ENDING.value:
        for e in ending:
            conjugated_forms.append(word + e)

    final_conjugated_forms = list(
        zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value * tenses_number, conjugated_forms))

    for e in final_conjugated_forms:
        print(e)


def conjugate_change_last_two_letters(word, endings):
    """
    :param word:
    :param endings:
    :return:
    """
    tenses_number = 6
    conjugated_forms = []
    for tens, terminations in enumerate(endings):
        for e in terminations:
            conjugated_forms.append(word[:-2] + e)

    final_conjugated_forms = list(
        zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value * tenses_number, conjugated_forms))

    for e in final_conjugated_forms:
        print(e)


def conjugate_verb(word):  # main method
    """

    :param word:
    :return:
    """
    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.ENDINGS_IR.value

    conjugate_change_last_two_letters(word, endings)
    conjugate_add_endings_to_the_end(word)


if __name__ == '__main__':

    try:
        # word = input('Enter a verb to be conjugated\n').lower()
        word = 'encontrar'
        if not word.isalpha():
            raise TypeError('A entrada incorreta | An incorrect input')

        if not word.endswith(('ar', 'er', 'ir')):
            raise NotInfinitiveError('A palavra inserida não é infinitivo | Not an infinitive')

    except NotInfinitiveError as nie:
        print(nie)
    except TypeError as t_err:
        print(t_err)

    conjugate_verb(word)
