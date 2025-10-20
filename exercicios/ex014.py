'''
Exercício Python 14: Escreva um programa que converta uma temperatura
digitando em graus Celsius e converta para graus Fahrenheit.
'''

celcius = float(input('Digite a temperatura °C: '))
print(f'Convertido para Fahrenheit {(celcius*1.8) + 32:.1f}°F\nConvertido para Kelvin: {celcius + 273.15:.1f}K')