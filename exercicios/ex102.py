'''
Exercício Python 102: Crie um programa que tenha uma
função fatorial() que receba dois parâmetros: o primeiro
que indique o número a calcular e outro chamado show, que
será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: numero a ser calculado
    :param show: mostra a conta(OPCIONAL)
    :return: o fatorial de n
    """
    print('-'*40)
    soma = 1
    e = ''
    for i in range(n, 0, -1):
        soma *= i
        if i != 1:
            e += str(f'{i} x ')
        else:
            e += str(f'{i} = {soma}')
    if show:
        return e
    return soma

print(fatorial(5, True))