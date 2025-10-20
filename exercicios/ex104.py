'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''

def leiaInt(msg=''):
    """
    -> Converte string para inteiro
    :param msg: texto que aparecerá na tela
    :return: retorna o valor inteiro
    """
    n = str(input(msg))
    while not n.isnumeric():
        print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        n = str(input(msg))
    return int(n)


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')