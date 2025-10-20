'''
Exercício Python 8: Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros.
'''

metros = float(input('Digite um valor: '))
print(f'Em quilometros: {metros*0.001}\nEm equitometros: {metros*0.01}\nEm decametros: {metros*0.1:.1f}\nEm decimetros: {metros*10}\nEm centrimetros: {metros*100}\nEm milimetros: {metros*1000}')