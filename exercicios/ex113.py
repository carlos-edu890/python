'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

from uteis import cor, cor_msg

def leiaInt(msg=''):
    """
    -> Converte string para inteiro
    :param msg: texto que aparecerá na tela
    :return: retorna o valor inteiro
    """
    while True:
        try:
            n = str(input(msg)).strip()
            return int(n)
        except (ValueError, TypeError):
            print(f'{cor_msg('Vermelho', msg='ERRO! Digite um número real válido.')}')
        except KeyboardInterrupt:
            print(f'\n{cor('Vermelho')}Usuário preferiu não digitar esse número.\033[m')
            return 0


def leiaFloat(msg=''):
    """
    -> Converte string para inteiro
    :param msg: texto que aparecerá na tela
    :return: retorna o valor inteiro
    """
    while True:
        try:
            n = str(input(msg)).strip()
            return float(n)
        except (ValueError, TypeError):
            print(f'{cor_msg('Vermelho', msg='ERRO! Digite um número real válido.')}')
        except KeyboardInterrupt:
            print(f'\n{cor('Vermelho')}Usuário preferiu não digitar esse número.\033[m')
            return 0


n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
