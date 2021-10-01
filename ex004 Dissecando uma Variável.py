# Faça um programa que leia algo pelo teclado
# E mostre na tela o seu tipo primitivo
# E todas as informações possíveis sobre ele.

a = input('digite algo: ')
print(' o tipo primitivo desse valor é', type(a))
print('So tem espacos: ', a.isspace())
print('é um numero? ', a.isnumeric())
print('e alfabetico? ',a.isalpha())
print('é alfanumerico?', a.isalnum())
print('esta em maiscula? ',a.isupper())
print('esta em minusculo? ' ,a.islower())
print('esta capitalizada? ',a.istitle())
