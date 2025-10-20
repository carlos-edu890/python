from uteis import cor

def leiaDinheiro(msg):
    while True:
        n = str(input(msg)).strip().replace(',', '.')
        try:
            return float(n)
        except (ValueError, TypeError):
            print(f'{cor('vermelho'.capitalize())}ERRO: "{n}" é um preço inválido!\033[m')