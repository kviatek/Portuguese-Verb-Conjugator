from pt_conjugator import enum_verbs_conjugator
from pt_conjugator import irregular_verbs_patterns
from pt_conjugator.enum_verbs_conjugator import TenseEndings


class NotInfinitiveError(ValueError):
    pass


def conjugate_add_endings_to_the_end(word):
    """
    The method conjugate verbs by adding to its root adequate grammatical endings.
    :param word: Verb to conjugated
    :return:
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


def conjugate_ar_ended_verb(word):
    endings = enum_verbs_conjugator.TenseEndings.AR_ENDINGS.value
    conjugate_change_last_two_letters(word, endings)
    conjugate_add_endings_to_the_end(word)


def conjugate_er_ended_verb(word):
    endings = enum_verbs_conjugator.TenseEndings.ENDINGS_ER.value
    conjugate_change_last_two_letters(word, endings)
    conjugate_add_endings_to_the_end(word)


def conjugate_ir_ended_verb(word):
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

    conjugate_ar_ended_verb('encontrar')

