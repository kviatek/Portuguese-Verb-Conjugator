import enum_verbs_conjugator


def is_string_check(word):
    if not isinstance(word, str):
        # print('Entrada de dados incorreta | An incorrect input value')
        return False


def conjugate_change_last_two_letters(endings, word):
    conjugated_forms = []
    for ending in endings:
        conjugated_forms.append(word[:-2] + ending)
        final_conjugated_forms = dict(zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value, conjugated_forms))
    print(final_conjugated_forms)


def conjugate_add_endings_to_the_end(word, tense):
    """
    The method conjugate verbs by adding to its root adequate grammatical endings.
    :param word: Verb to conjugated
    :param tense: Enter two possibilites: 'futuro' or 'condicional' which decides about used endings
    :return:
    """
    word = word.lower()

    if tense == 'futuro':
        if word.endswith(('ar', 'er', 'ir')):
            conjugated_forms = []
            for ending in enum_verbs_conjugator.TenseEndings.FUTURO_SIMPLES_INDICATIVO_ENDINGS.value:
                conjugated_forms.append(word + ending)
                final_conjugated_forms = dict(zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value,
                                                  conjugated_forms))
            print(final_conjugated_forms)
        else:
            print('A palavra inserida não é infinitivo de um verbo | Not a verb infinitive')
            return
    elif tense == 'condicional':
        if word.endswith(('ar', 'er', 'ir')):
            conjugated_forms = []
            for ending in enum_verbs_conjugator.TenseEndings.CONDICIONAL_SIMPLES_ENDIGNS.value:
                conjugated_forms.append(word + ending)
                final_conjugated_forms = dict(zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value,
                                                  conjugated_forms))
            print(final_conjugated_forms)
        else:
            print('A palavra inserida não é infinitivo de um verbo | Not a verb infinitive')
            return


def conjugate_presente_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.INDICATIVO_PRESENTE_ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.INDICATIVO_PRESENTE_ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.INDICATIVO_PRESENTE_ENDINGS_IR.value
    else:
        print('A palavra inserida não é infinitivo de um verbo | Not a verb infinitive')
        return

    conjugate_change_last_two_letters(endings, word)


def conjugate_preterito_perfeito_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_PERFEITO_INDICATIVO_ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_PERFEITO_INDICATIVO_ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_PERFEITO_INDICATIVO_ENDINGS_IR.value
    else:
        print('A palavra inserida não é infinitivo de um verbo | Not a verb infinitive')
        return

    conjugate_change_last_two_letters(endings, word)


def conjugate_preterito_imperfeito_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_IMPERFEITO_INDICATIVO_ENDINGS_AR.value
    elif word.endswith('er') or word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_IMPERFEITO_INDICATIVO_ENDINGS_ER_IR.value
    else:
        print('A palavra inserida não é infinitivo de um verbo | Not a verb infinitive')
        return

    conjugate_change_last_two_letters(endings, word)


def conjugate_preterito_mais_que_perfeito_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_IR.value
    else:
        print('A palavra inserida não é infinitivo de um verbo | Not a verb infinitive')
        return

    conjugate_change_last_two_letters(endings, word)


def conjugate_futuro_simples_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word == 'trazer':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_TRAZER.value)
    elif word == 'ser':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_SER.value)
    elif word == 'dizer':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_DIZER.value)
    elif word == 'fazer':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_FAZER.value)
    else:
        conjugate_add_endings_to_the_end(word, 'futuro')


def conjugate_condicional_simples(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word == 'trazer':
        print(enum_verbs_conjugator.FixedConjugations.CONDICIONAL_TRAZER.value)
    elif word == 'dizer':
        print(enum_verbs_conjugator.FixedConjugations.CONDICIONAL_DIZER.value)
    elif word == 'fazer':
        print(enum_verbs_conjugator.FixedConjugations.CONDICIONAL_FAZER.value)
    else:
        conjugate_add_endings_to_the_end(word, 'condicional')


if __name__ == '__main__':
    word = input('Enter averb to be conjugated\n')

    conjugate_presente_indicativo(word)
    conjugate_preterito_mais_que_perfeito_indicativo(word)
    conjugate_preterito_perfeito_indicativo(word)
    conjugate_preterito_imperfeito_indicativo(word)
    conjugate_condicional_simples(word)
    conjugate_futuro_simples_indicativo(word)


