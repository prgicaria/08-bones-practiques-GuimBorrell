#! usr/bin/env python

'''bones_practiques. Dona el quocient i el
residu a partir del divisor i el dividend

Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

El programa imprimeix per pantalla el quocient i el residu,
així com la expressió de la divisió del dividend i el divisor
'''
__author__ = "Guim Borrell"
__email__ = "gborrell@instituticaria.cat"
__date__ = "2024/10/23"


dividend = int(input("Entra el teu dividend:"))
divisor = int(input("Entra el teu divisor:"))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
