#!/usr/bin/env python3

"""
Docstring will go here

"""

import enum_conjugator
import irregular_verbs
import logging

# Ordinary logs

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('conjugator.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# =====================================================================================

# Error logs

error_logger = logging.getLogger(__name__)
error_logger.setLevel(logging.ERROR)

error_formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

error_file_handler = logging.FileHandler('conjugator.log')
error_file_handler.setFormatter(error_formatter)

error_stream_handler = logging.StreamHandler()
error_stream_handler.setFormatter(error_formatter)

error_logger.addHandler(error_file_handler)
error_logger.addHandler(error_stream_handler)


class NotInfinitiveError(ValueError):
    pass


def link_conjugated_forms_with_grammatical_persons(tenses_number, conjugated_forms):
    """
    Method links conjugated forms of a verb with respective grammatical persons names.
    :param tenses_number: number of tenses
    :param conjugated_forms: a list of conjugated forms of a verb
    :return: a list of tuples with pairs grammatical person name, conjugated wrb
    """
    return list(zip(enum_conjugator.GrammaticalPersons.PERSONS.value * tenses_number, conjugated_forms))


def print_conjugation(conjugation):
    for e in conjugation:
        print(e)


def is_regular_verb(word):
    """
    The method checks whether a verb is regular or not by looking it up in a dictionary of all existent irregular verbs.
    :param word: a verb to be checked
    :return: True if a verb is regular otherwise False
    """
    return True if word not in irregular_verbs.all_irregular_verbs_dict \
                   and word not in irregular_verbs.basic_irregular_verbs else False


def create_gerundium(word):
    """
    Method returns a gerundium form of a verb by changing the last two letters to an appropriate ending.
    :param word:
    :return: gerundium of a verb
    """
    return word[:-1] + 'ndo'


def create_past_participle(word):
    """
    Method returns a past participle form a verb by changing the last two letters to an appropriate ending.
    :param word: verb whose past participle form need to be created
    :return: past participle form of a verb
    """
    return word[:-2] + 'ado' if word.endswith('ar') else word[:-2] + 'ido'


def conjugate_compound_tenses(word):
    """
    Method create conjugations of all compund tenses with use of auxiliary verb 'ter'
    There's a past participle created based on a verb and linked with an adequate form o a verb ter.
    The method makes use of a create_past_participle() function to create a past participle form.
    :param word: a verb to be conjugated
    :return: list of conjugated forms
    """
    final_conjugated_forms = []
    past_participle = create_past_participle(word)

    # Verb 'ter' is an auxiliary verb, its conjugation is imported from irregular_verbs.py module
    # and omitting unnecessary tenses conjugations

    for index, auxiliary_verb in enumerate(
            irregular_verbs.ter):
        if index != 1 and index != 3 and index != 9 and index != 10:
            for e in auxiliary_verb:
                final_conjugated_forms.append(e + ' ' + past_participle)

    return final_conjugated_forms


def conjugate_add_endings_to_the_end(word):
    """
    The method conjugate verbs by adding to its infinitive form
    adequate grammatical endings depending on a type of a tense.
    :param word: a verb to be conjugated
    :return: list of conjugated forms of all grammatical tenses
    """
    tenses_number = 2  # number of tenses created by adding an ending to an infinitive
    conjugated_forms = []

    for ending in enum_conjugator.TenseEndings.CONDITIONAL_AND_FUTURE_SIMPLE_ENDINGS.value:  # adding endings
        for e in ending:
            conjugated_forms.append(word + e)

    # linking all conjugated forms with corresponding grammatical persons
    final_conjugated_forms = link_conjugated_forms_with_grammatical_persons(tenses_number, conjugated_forms)

    return final_conjugated_forms


def conjugate_change_last_two_letters(word, endings):
    """
    The method conjugate verbs by adding to its root an adequate grammatical endings depending on a type of a tense.
    :param word: a verb to be conjugated
    :param endings:
    :return: a dictionary with tenses names as keys and a list of conjugated forms as a value.
    """

    tenses_names = list(enum_conjugator.TenseEndings.Endings.value._fields)

    tenses_number = 8
    grammatical_persons_number = 6
    conjugated_forms = []

    for tens, terminations in enumerate(endings):
        for e in terminations:
            conjugated_forms.append(word[:-2] + e)

    # linking conjugated verbs with grammatical persons names
    conjugated_forms = link_conjugated_forms_with_grammatical_persons(tenses_number, conjugated_forms)

    # list of conjugations divided by tenses
    conjugations_divided_by_tenses = [conjugated_forms[x:x + grammatical_persons_number] for x in
                                      range(0, len(conjugated_forms), grammatical_persons_number)]

    final_conjugated_forms = dict(zip(tenses_names, conjugations_divided_by_tenses))

    return final_conjugated_forms  # słownik


def conjugate_irregular_verb(word):
    """
    Method
    :param word:
    :return: list of c
    """

    # Checing whehter a verb is in the list of irregular verbs whcih don't follow any conjugation pattern.
    # If present, its complete conjugation is returned from the dictionary

    if word in irregular_verbs.basic_irregular_verbs.keys():
        return irregular_verbs.basic_irregular_verbs.get(word)
    elif word not in irregular_verbs.basic_irregular_verbs.keys() \
            and irregular_verbs.all_irregular_verbs_dict.get(word) is None:  # if True a verb not yet added to the dict

        verb_ending = ''
        conjugation = []

        # going through a list of verbs that serve as a conjugation pattern for others.
        # Their complete conjugations are used entirely as an ending added to a its root.
        for verb in irregular_verbs.basic_irregular_verbs.keys():
            if word.endswith(verb):
                verb_ending, conjugation = verb, irregular_verbs.basic_irregular_verbs.get(
                    verb)

        base = word[:-len(verb_ending)]
        final_conjugated_forms = []

        for tense in conjugation:
            for form in tense:
                final_conjugated_forms.append(base + form)

        return final_conjugated_forms  # lista
    else:
        return irregular_verbs.all_irregular_verbs_dict.get(word)  # lista


def conjugate_regular_verb(word):
    """

    :param word:
    :return:
    """

    def imperative(word, imperative_endings):
        """

        :param word:
        :param imperative_endings:
        :return:
        """

        imperative_affirmative = []
        imperative_negative = []

        for ending in imperative_endings:
            imperative_affirmative.append(word[:-2] + ending)

        presente_de_subjuntivo_list = list(
            conjugate_change_last_two_letters(word, endings).get('Presente_de_Subjuntivo'))
        for ending in presente_de_subjuntivo_list[1:]:
            imperative_negative.append('não ' + ending[1])

        return imperative_affirmative, imperative_negative  # lista

    if word.endswith('ar'):
        endings = enum_conjugator.TenseEndings.ENDINGS_AR.value
        imperative_endings = enum_conjugator.TenseEndings.AFFIRMATIVE_IMPERATIVE_ENDINGS.value.ar_endings
    elif word.endswith('er'):
        endings = enum_conjugator.TenseEndings.ENDINGS_ER.value
        imperative_endings = enum_conjugator.TenseEndings.AFFIRMATIVE_IMPERATIVE_ENDINGS.value.er_endings
    elif word.endswith('ir'):
        endings = enum_conjugator.TenseEndings.ENDINGS_IR.value
        imperative_endings = enum_conjugator.TenseEndings.AFFIRMATIVE_IMPERATIVE_ENDINGS.value.ir_endings

    return conjugate_change_last_two_letters(word, endings), conjugate_add_endings_to_the_end(
        word), conjugate_compound_tenses(word), create_gerundium(word), create_past_participle(word), imperative(word,
                                                                                                                 imperative_endings)


def conjugate_verb(word):  # main method
    """
    Main method which evaluates whether a verb is regular or not and produces a corresponding
    list of conjugations in all grammatical tenses.
    :param word: a verb to be conjugated
    :return: a list of conjugations in all grammatical tenses
    """

    if is_regular_verb(word):
        return conjugate_regular_verb(word)
    else:
        return conjugate_irregular_verb(word)


if __name__ == '__main__':

    try:
        # word = input('Enter a verb to be conjugated\n').lower()
        word = 'achar'
        if not word.isalpha():
            raise TypeError

        if not word.endswith(('ar', 'er', 'ir')):
            raise NotInfinitiveError

    except NotInfinitiveError as nie:
        error_logger.exception('A palavra inserida não é infinitivo | Not an infinitive')

    except TypeError as te:
        error_logger.exception('A entrada incorreta | An incorrect input')
