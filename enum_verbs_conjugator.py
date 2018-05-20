from enum import Enum


# This module is a collection of all constants related to portuguese verbs conjugation,
# i.e. names of grammatical persons.


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


class FixedConjugations(Enum):
    # AUXILIAR VERBS
    VERBO_AUXILIAR_PRESENTE_INDICATIVO_TER = {'Eu/I': 'tenho', 'Tu/You': 'tens', 'Ele/Ela/você/He/She/It': 'tem',
                                              'Nós/We': 'temos',
                                              'Else/Elas/vocês/They': 'têm'}

    VERBO_AUXILIAR_PRESENTE_INDICATIVO_HAVER = {'Eu/I': 'hei', 'Tu/You': 'hás', 'Ele/Ela/você/He/She/It': 'há',
                                              'Nós/We': 'havemos',
                                              'Else/Elas/vocês/They': 'hão'}

    # FIXED CONJUGATIONS FOR CONDICIONAL SIMPLES TENSE
    CONDICIONAL_TRAZER = {'Eu/I': 'traria', 'Tu/You': 'trarias', 'Ele/Ela/você/He/She/It': 'traria',
                          'Nós/We': 'traríamos',
                          'Else/Elas/vocês/They': 'trariam'}

    CONDICIONAL_DIZER = {'Eu/I': 'diria', 'Tu/You': 'dirias', 'Ele/Ela/você/He/She/It': 'diria', 'Nós/We': 'diríamos',
                         'Else/Elas/vocês/They': 'diriam'}

    CONDICIONAL_FAZER = {'Eu/I': 'faria', 'Tu/You': 'farias', 'Ele/Ela/você/He/She/It': 'faria', 'Nós/We': 'faríamos',
                         'Else/Elas/vocês/They': 'fariam'}

    # FIXED CONJUGATIONS FOR FUTURO SIMPLES INDICATIVO TENSE

    FUTURO_SIMPLES_INDICATIVO_DIZER = {'Eu/I': 'direi', 'Tu/You': 'dirás', 'Ele/Ela/você/He/She/It': 'dirá',
                                       'Nós/We': 'diremos',
                                       'Else/Elas/vocês/They': 'dirão'}

    FUTURO_SIMPLES_INDICATIVO_FAZER = {'Eu/I': 'farei', 'Tu/You': 'farás', 'Ele/Ela/você/He/She/It': 'fará',
                                       'Nós/We': 'faremos',
                                       'Else/Elas/vocês/They': 'farão'}

    FUTURO_SIMPLES_INDICATIVO_SER = {'Eu/I': 'for', 'Tu/You': 'fores', 'Ele/Ela/você/He/She/It': 'for',
                                     'Nós/We': 'formos',
                                     'Else/Elas/vocês/They': 'forem'}

    FUTURO_SIMPLES_INDICATIVO_TRAZER = {'Eu/I': 'trarei', 'Tu/You': 'trarás', 'Ele/Ela/você/He/She/It': 'trará',
                                        'Nós/We': 'traremos',
                                        'Else/Elas/vocês/They': 'trarão'}


class IrregularVerbs(Enum):
    irregular_verbs = {
        'A': ('abster', 'acudir', 'adequar', 'aderir', 'adjazer', 'advertir', 'advir', 'afazer', 'aferir', 'agredir',
              'ansiar', 'antedar', 'antepor', 'antever', 'apor', 'aprazer', 'apropinquar', 'aspergir', 'assentir',
              'ater', 'atrair', 'atribuir', 'autodestruir', 'avir'),
        'B': ('bem-dizer', 'bem-fazer', 'bem-querer', 'bendizer', 'benfazer', 'benquerer', 'buir', 'bulir'),
        'C': ('caber', 'cair', 'cerzir', 'circumpor', 'circunver', 'cobrir', 'compelir', 'competir', 'compor',
              'comprazer', 'concernir', 'concluir', 'condizer', 'condoer', 'conferir', 'confugir', 'conseguir',
              'consentir', 'construir', 'consumir', 'conter', 'contradizer', 'contrafazer', 'contrair', 'contrapor',
              'contrapropor', 'contravir', 'convergir', 'convir', 'crer', 'cuspir'),
        'D': ('dar', 'decompor', 'deferir', 'delinquir', 'denegrir', 'depor', 'desafazer', 'desaguar', 'desapor',
              'desaprazer', 'desavir', 'descaber', 'descobrir', 'descompor', 'descomprazer', 'desconstruir',
              'desconvir', 'descrer', 'desdar', 'desdizer', 'desimpedir', 'desimpor', 'deslinguar', 'desmedir',
              'desmentir', 'desmobiliar', 'despedir', 'despir', 'despolir', 'despor', 'desprazer', 'desprecaver',
              'desprover', 'desquerer', 'dessaber', 'destruir', 'desvaler', 'desver', 'deter', 'devir', 'digerir',
              'disperder', 'dispor', 'distrair', 'divertir', 'dizer', 'doer', 'dormir'),
        'E': ('embair', 'emergir', 'encobrir', 'engolir', 'entredizer', 'entrefazer', 'entreouvir', 'entrepor',
              'entrequerer', 'entrever', 'entrevir', 'entupir', 'enxaguar', 'equivaler', 'escapulir', 'esfazer',
              'estar', 'estrear', 'esvair', 'expedir', 'expelir', 'expor', 'extrapor'),
        'F': ('fazer', 'ferir', 'fotocompor', 'fraguar', 'frigir', 'fugir'),
        'G': 'gelifazer',
        'H': 'haver',
        'I': ('idear', 'imergir', 'impedir', 'impelir', 'impor', 'incendiar', 'incluir', 'indispor', 'influir',
              'insatisfazer', 'inserir', 'interdizer', 'intermediar', 'interpor', 'interver', 'intervir', 'ir'),
        'J': ('jazer', 'justapor'),
        'L': ('ler', 'liquefazer'),
        'M': (
            'maisquerer', 'maldispor', 'maldizer', 'malfazer', 'malinguar', 'malparir', 'malquerer', 'manter', 'mediar',
            'medir', 'mentir', 'minguar', 'mobiliar', 'moer'),
        'O': ('obter', 'obvir', 'odiar', 'opor', 'ouvir'),
        'P': ('parir', 'pedir', 'perder', 'perfazer', 'perseguir', 'persentir', 'pleitear', 'poder', 'polir', 'pospor',
              'pôr', 'prazer', 'precluir', 'predispor', 'predizer', 'preferir', 'prepor', 'pressentir', 'pressupor',
              'preterir', 'prevenir', 'prever', 'progredir', 'propor', 'prossupor', 'prover', 'provir', 'pruir',
              'puir', 'putrefazer'),
        'Q': 'querer',
        'R': ('raer', 'rarefazer', 'readequar', 'reaver', 'reavir', 'recobrir', 'recompor', 'reconvir', 'redar',
              'redispor', 'redizer', 'reexpedir', 'reexpor', 'refazer', 'regredir', 'reimpor', 'reindispor', 'reler',
              'remediar', 'remedir', 'reobter', 'reouvir', 'repedir', 'repelir', 'repor', 'repropor', 'requerer',
              'resfolegar', 'ressentir', 'reter', 'retrair', 'retranspor', 'rever', 'revir', 'rir', 'ruir'),
        'S': ('saber', 'sacudir', 'sair', 'santiguar', 'satisfazer', 'seguir', 'sentir', 'ser', 'servir', 'sobpor',
              'sobre-expor', 'sobreexpor', 'sobrepor', 'sobrestar', 'sobrevir', 'soer', 'sorrir', 'sortear', 'sortir',
              'sotopor', 'subir', 'submergir', 'subpor', 'subtrair', 'sugerir', 'sumir', 'superexpor', 'superimpor',
              'superpor', 'supor', 'suster'),
        'T': ('telever', 'ter', 'torrefazer', 'tossir', 'trair', 'transfazer', ' transfugir', 'transgredir', 'transpor',
              'traspor', 'trazer', 'treler', 'tresler', 'trespor', 'tumefazer'),
        'V': ('valer', 'ver', 'vestir', 'vir')}
