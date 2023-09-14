# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:50:39 2023

@author: Javier
"""

venta = input('Que carro quieres?\n')
carro1 = {
    'año' : '2004',
    'modelo' : 'Ford GT',
    'Precio' : '10,000,000$'
            }
N1 = carro1

carro2 = {
    'año' : '2005',
    'modelo' : 'Chevrolet Corvette',
    'Precio' : '1,000,000$'
            }
N2 = carro2

for x in carro2:
    print('Carro numero 2\n', carro2[x])
else:
    for y in carro1:
        print('\n Carro numero 1\n', carro1[y])
        