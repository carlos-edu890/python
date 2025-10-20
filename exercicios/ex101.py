'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(nasc):
    """
    -> Calcula a idade e retorna se a pessoa está
    apta a votar
    :param nasc: ano de nascimento
    :return: retorna a situação para a votação
    """
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade > 70:
        return 'VOTO OPCIONAL'
    elif idade < 18:
        return 'NÃO VOTA'
    else:
        return 'VOTO OBRIGATÓRIO'


print('-'*30)
print(voto(int(input('Digite o ano de nascimento: '))))