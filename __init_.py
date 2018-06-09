#!/usr/bin/env python

"""
Docstring will go here

"""

from app import enum_verbs_conjugator
from app import irregular_verbs_patterns
from app.enum_verbs_conjugator import TenseEndings
from collections import namedtuple


class NotInfinitiveError(ValueError):
    pass


def print_final_conjugated_forms(final_conjugated_forms):
    for tense in final_conjugated_forms:
        print(tense)


def create_gerundium(word):
    """
    Method creates gerundium of a verb
    :param word:
    :return: gerundium of a verb
    """
    return word[:-1] + 'ndo'


def create_past_participle(word):
    """
    Method returns past participle form a verb
    :param word: verb whose past participle form need to be created
    :return: past participle form of a verb
    """
    return word[:-2] + 'ado' if word.endswith('ar') else word[:-2] + 'ido'


def conjugate_compound_tenses(word):
    """

    :param word:
    :return:
    """

    final_conjugated_forms = []
    past_participle = create_past_participle(word)
    for index, auxiliary_verb in enumerate(irregular_verbs_patterns.ter):
        if index != 1 and index != 3 and index != 9 and index != 10:
            for e in auxiliary_verb:
                final_conjugated_forms.append(e + ' ' + past_participle)

    print_final_conjugated_forms(final_conjugated_forms)


def conjugate_add_endings_to_the_end(word):
    """
    The method conjugate verbs by adding to its root adequate grammatical endings.
    :param word: Verb to be conjugated
    :return: list of conjugated forms of all grammatical tenses
    """
    tenses_number = 2
    conjugated_forms = []

    for ending in enum_verbs_conjugator.TenseEndings.CONDITIONAL_AND_FUTURE_ENDINGS.value:
        for e in ending:
            conjugated_forms.append(word + e)

    final_conjugated_forms = list(
        zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value * tenses_number, conjugated_forms))

    print_final_conjugated_forms(final_conjugated_forms)


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


def conjugate_irregular_verb(word):
    """

    :param word:
    :return:
    """

    if irregular_verbs_patterns.all_irregular_verbs_dict.get(word) == None:

        verb_ending = ''
        conjugation = []

        for verb in irregular_verbs_patterns.basic_irregular_verbs_complete_conjugations.keys():
            if word.endswith(verb):
                verb_ending, conjugation = verb, irregular_verbs_patterns.basic_irregular_verbs_complete_conjugations.get(
                    verb)

        base = word[:-len(verb_ending)]
        final_conjugated_list = []

        for tense in conjugation:
            for form in tense:
                final_conjugated_list.append(base + form)

        return final_conjugated_list
    else:
        return irregular_verbs_patterns.all_irregular_verbs_dict.get(word)


def conjugate_verb(word):  # main method
    """

    :param word:
    :return:
    """

    def is_regular_verb(word):  # sprawdzam, czy regularny
        """

        :param word:
        :return:
        """
        return True if word not in irregular_verbs_patterns.all_irregular_verbs_dict else False

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.ENDINGS_IR.value

    conjugate_change_last_two_letters(word, endings)
    conjugate_compound_tenses(word)
    conjugate_add_endings_to_the_end(word)
    print(conjugate_irregular_verb(word))
    print(create_gerundium(word))
    print(create_past_participle(word))


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

    print(conjugate_irregular_verb('consumir'))

    #
    # for index, verb in enumerate(
    #         irregular_verbs_patterns.basic_irregular_verbs_complete_conjugations._fields):  # ZJEBANE
    #     if 'supor'.endswith(verb):
    #         print(verb)
    #     else:
    #         print(irregular_verbs_patterns.all_irregular_verbs_dict.get(verb))
