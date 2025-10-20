'''
Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings
para documentar nossas funções, argumentos opcionais para dar mais dinamismo
em funções Python, escopo de variáveis e retorno de resultados.
'''


def somar(a, b):
    """
    --> A Função soma os números e printa na tela
    :param a: numero a ser soma
    :param b: numero a ser soma
    :return: não há retorno
    """
    c = a + b
    print(f'A soma entre {a} e {b} é {a+b}', f'\nE é {c}')


c = 10
somar(c, 9)
print(f'"c" vale {c}')