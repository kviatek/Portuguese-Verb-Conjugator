from enum import Enum


# This module is a collection of all constants related to portuguese verbs conjugation,
# i.e. names of grammatical persons.


class GrammaticalPersons(Enum):
    FIRST_PERSON_SINGULAR = 'Eu/I'
    SECOND_PERSON_SINGULAR = 'Tu/You'
    THIRD_PERSON_SINGULAR = 'Ele/Ela/você/He/She/It'
    FIRST_PERSON_PLURAL = 'Nós/We'
    SECOND_PERSON_PLURAL = 'Else/Elas/vocês/They'


class TenseEndings(Enum):
    # indicativo_presente_endings

    INDICATIVO_PRESENTE_ENDINGS_AR = ('o', 'as', 'a', 'amos', 'am')
    INDICATIVO_PRESENTE_ENDINGS_ER = ('o', 'es', 'e', 'emos', 'em')
    INDICATIVO_PRESENTE_ENDINGS_IR = ('o', 'es', 'e', 'imos', 'em')

    # preterito_perfeito_endings

    PRETERITO_PERFEITO_ENDINGS_AR = ('ei', 'aste', 'ou', 'amos', 'aram')
    PRETERITO_PERFEITO_ENDINGS_ER = ('i', 'este', 'eu', 'emos', 'eram')
    PRETERITO_PERFEITO_ENDINGS_IR = ('i', 'iste', 'iu', 'imos', 'iram')

    # preterito_imperfeito_endings

    PRETERITO_IMPERFEITO_ENDINGS_AR = ('ava', 'avas', 'ava', 'ávamos', 'avam')
    PRETERITO_IMPERFEITO_ENDINGS_ER_IR = ('ia', 'ias', 'ia', 'íamos', 'iam')

    # futuro_simples_indicativo

    FUTURO_SIMPLES_INDICATIVO_ENDINGS = ('ei', 'ás', 'á', 'emos', 'ão')

    # condicional_simples

    CONDICIONAL_SIMPLES_ENDIGNS = ('ia', 'ias', 'ia', 'íamos', 'iam')


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
