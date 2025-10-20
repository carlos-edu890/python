'''
Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação (opcional)
'''

def notas(* notas, sit=False):
    """
    -> Funçãopara analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas do aluno (aceita várias)
    :param sit: valor opicional, indicando se deve ou não adicionar a situação
    :return: dicionário com vária informações sobre a situação da turma (caso algum valor seja passado)
    """
    if len(notas) >= 1:
        dict = {}
        soma = sum(notas)
        media = soma / len(notas)
        dict['total'] = len(notas)
        dict['maior'] = max(notas)
        dict['menor'] = min(notas)
        dict['média'] = media
        if sit:
            if media >= 7:
                dict['situação'] = 'BOA'
            elif media >= 5:
                dict['situação'] = 'RAZOAVEL'
            else:
                dict['situação'] = 'RUIM'
        return dict
    else:
        return 'Não foi passado nenhum valor.'


print('-'*40)
res = notas()
print(res)