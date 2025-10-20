def aumentar(n, i, formato=False):
    """
    -> Aumenta o valor de acordo com a taxa
    :param n: o valor que quer reajustar
    :param i: a taxa de acréscimo
    :param formato: se a pessoa deseja que a saida seja formatada
    :return: retorna o valor de acordo com a taxa, formatado ou não
    """
    n = n + (n * (i / 100))
    if formato:
        return moeda(n)
    return n


def diminuir(n, i, formato=False):
    """
    -> Diminui o valor de acordo com a taxa
    :param n: o valor que quer reajustar
    :param i: a taxa de decréscimo
    :param formato: se a pessoa deseja que a saida seja formatada
    :return: retorna o valor de acordo com a taxa, formatado ou não
    """
    n = n - (n * (i / 100))
    if formato:
        return moeda(n)
    return n


def dobro(n, formato=False):
    """
    -> Calcula o dobro do valor
    :param n: o valor a ser dobrado
    :param formato: se a pessoa deseja que a saida seja formatada
    :return: retorna o dobro do valor
    """
    if formato:
        return moeda(n * 2)
    return n * 2


def metade(n, formato=False):
    """
    -> Calcula a metade do valor
    :param n: o valor a será dividido
    :param formato: se a pessoa deseja que a saida seja formatada
    :return: retorna a metade do valor
    """
    if formato:
        return moeda(n / 2)
    return n / 2


def moeda(n):
    """
    -> Formata o valor fornecido
    :param n: valor a ser formatado
    :return: retorna o valor formatado em R$
    """
    return f'R${n:.2f}'.replace('.', ',')