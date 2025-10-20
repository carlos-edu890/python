from uteis import cor

def titulo(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)


def menu_principal():
    try:
        while True:
            titulo('MENU PRINCIPAL')
            print(f'{cor('Amarelo claro')}1\033[m - {cor('Azul claro')}Ver pessoas cadastradas\033[m')
            print(f'{cor('Amarelo claro')}2\033[m - {cor('Azul claro')}Cadastrar nova Pessoa\033[m')
            print(f'{cor('Amarelo claro')}3\033[m - {cor('Azul claro')}Sair do Sistema\033[m')
            print('-'*40)
            try:
                n = int(input(f'{cor('Amarelo claro')}Sua opção:\033[m '))
                if n == 1:
                    listar_pessoas()
                elif n == 2:
                    cadastrar_pessoa()
                elif n == 3:
                    break
                else:
                    print(f'{cor('Vermelho')}ERRO! Opção inválida.\033[m')
            except (ValueError, TypeError):
                print(f'{cor('Vermelho')}ERRO! Opção inválida.\033[m')
    except KeyboardInterrupt:
        print('')
    finally:
        titulo('Saindo do sistema... Até logo!')

def listar_pessoas():
    titulo('PESSOAS CADASTRADAS')
    try:
        with open('texto.txt', 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip().split()
                e = ''
                for pos, i in enumerate(linha):
                    if i.isnumeric():
                        e += f'{i:>3} anos'
                    elif (len(linha) - 2) == pos:
                        e += f'{i:<30}'
                    else:
                        e += f'{i} '
                print(e)
    except FileNotFoundError:
        print(f'{cor('Vermelho')}ERRO! Arquivo não encontrado.\033[m')


def cadastrar_pessoa():
    titulo('NOVO CADASTRO')
    nome = input('Nome: ')
    while True:
        try:
            idade = input('Idade: ')
            int(idade)
            break
        except (ValueError, TypeError):
            print(f'{cor('Vermelho')}ERRO! Digite um número.\033[m')
        except KeyboardInterrupt:
            titulo('Saindo do sistema... Até logo!')
    try:
        with open('texto.txt', 'a') as arquivo:
            arquivo.write(f'\n{nome} {idade}')
            print(f'Novo registro de {nome} adicionado.')
    except FileNotFoundError:
        print(f'{cor('Vermelho')}ERRO! Arquivo não encontrado.\033[m')