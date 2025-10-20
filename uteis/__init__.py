def cor(cor_texto=39, estilo_texto=0, fundo=49):
    # Mapeamento de cores para texto
    cores_texto = {
        'Preto': '30',
        'Vermelho': '31',
        'Verde': '32',
        'Amarelo': '33',
        'Azul': '34',
        'Magenta': '35',
        'Ciano': '36',
        'Branco': '37',
        'Cinza escuro': '90',
        'Vermelho claro': '91',
        'Verde claro': '92',
        'Amarelo claro': '93',
        'Azul claro': '94',
        'Magenta claro': '95',
        'Ciano claro': '96',
        'Branco brilhante': '97'
    }

    # Mapeamento de cores para fundo
    cores_fundo = {
        'Preto': '40',
        'Vermelho': '41',
        'Verde': '42',
        'Amarelo': '43',
        'Azul': '44',
        'Magenta': '45',
        'Ciano': '46',
        'Branco': '47',
        'Cinza escuro': '100',
        'Vermelho claro': '101',
        'Verde claro': '102',
        'Amarelo claro': '103',
        'Azul claro': '104',
        'Magenta claro': '105',
        'Ciano claro': '106',
        'Branco brilhante': '107'
    }

    # Mapeamento de estilos
    estilos = {
        'normal': '0',
        'negrito': '1',
        'fraco': '2',
        'itálico': '3',
        'sublinhado': '4',
        'piscando': '5',
        'invertido': '7',
        'oculto': '8'
    }

    # Converter texto para código ANSI
    if cor_texto in cores_texto:
        codigo_texto = cores_texto[cor_texto]
    else:
        codigo_texto = cor_texto

    # Converter fundo para código ANSI
    if fundo in cores_fundo:
        codigo_fundo = cores_fundo[fundo]
    else:
        codigo_fundo = fundo

    # Converter estilo para código ANSI
    if estilo_texto in estilos:
        codigo_estilo = estilos[estilo_texto]
    else:
        codigo_estilo = '0'  # Padrão: normal

    # Construir a sequência de escape ANSI
    sequencia_ansi = f"\033[{codigo_estilo};{codigo_texto};{codigo_fundo}m"
    #reset_ansi = "\033[0m"

    return sequencia_ansi



def cor_msg(cor_texto=39, estilo_texto=0, fundo=49, msg=''):
    # Mapeamento de cores para texto
    cores_texto = {
        'Preto': '30',
        'Vermelho': '31',
        'Verde': '32',
        'Amarelo': '33',
        'Azul': '34',
        'Magenta': '35',
        'Ciano': '36',
        'Branco': '37',
        'Cinza escuro': '90',
        'Vermelho claro': '91',
        'Verde claro': '92',
        'Amarelo claro': '93',
        'Azul claro': '94',
        'Magenta claro': '95',
        'Ciano claro': '96',
        'Branco brilhante': '97'
    }

    # Mapeamento de cores para fundo
    cores_fundo = {
        'Preto': '40',
        'Vermelho': '41',
        'Verde': '42',
        'Amarelo': '43',
        'Azul': '44',
        'Magenta': '45',
        'Ciano': '46',
        'Branco': '47',
        'Cinza escuro': '100',
        'Vermelho claro': '101',
        'Verde claro': '102',
        'Amarelo claro': '103',
        'Azul claro': '104',
        'Magenta claro': '105',
        'Ciano claro': '106',
        'Branco brilhante': '107'
    }

    # Mapeamento de estilos
    estilos = {
        'normal': '0',
        'negrito': '1',
        'fraco': '2',
        'itálico': '3',
        'sublinhado': '4',
        'piscando': '5',
        'invertido': '7',
        'oculto': '8'
    }

    # Converter texto para código ANSI
    if cor_texto in cores_texto:
        codigo_texto = cores_texto[cor_texto]
    else:
        codigo_texto = cor_texto

    # Converter fundo para código ANSI
    if fundo in cores_fundo:
        codigo_fundo = cores_fundo[fundo]
    else:
        codigo_fundo = fundo

    # Converter estilo para código ANSI
    if estilo_texto in estilos:
        codigo_estilo = estilos[estilo_texto]
    else:
        codigo_estilo = '0'  # Padrão: normal

    # Construir a sequência de escape ANSI
    sequencia_ansi = f"\033[{codigo_estilo};{codigo_texto};{codigo_fundo}m{msg}\033[m"
    #reset_ansi = "\033[0m"

    return sequencia_ansi