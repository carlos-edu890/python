def aumentar(n, i, format=False):
    n = n + (n * (i / 100))
    if format:
        return moeda(n)
    return n


def diminuir(n, i, format=False):
    n = n - (n * (i / 100))
    if format:
        return moeda(n)
    return n


def dobro(n, format=False):
    if format:
        return moeda(n * 2)
    return n * 2


def metade(n, format=False):
    if format:
        return moeda(n / 2)
    return n / 2


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n, au=0, me=0):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)
    print(f'{'Preço analisado:':<20}{moeda(n)}')
    print(f'{'Dobro do preço:':<20}{dobro(n, True)}')
    print(f'{'Metdade do preço:':<20}{metade(n, True)}')
    if au >= 1:
        print(f'{f'{au}% de aumento:':<20}{aumentar(n, au, True)}')
    if me >= 1:
        print(f'{f'{me}% de redução:':<20}{diminuir(n, me, True)}')
    print('-'*30)