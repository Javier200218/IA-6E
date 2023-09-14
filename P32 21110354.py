# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:56:51 2023

@author: Javier
"""

venta = input('Que carro quieres?\n')
carro1 = {
    'año' : '2004',
    'modelo' : 'Ford GT',
    'Precio' : '10,000,000$'
            }

del carro1['año']
for x in carro1:
    print(carro1[x])