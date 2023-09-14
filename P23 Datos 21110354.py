# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:18:01 2023

@author: Javier
"""

entrada = input("introduce el nombre de la bebida\n")
bebidas = ['ron', 'vodka', 'tequila', 'whisky', 'cerveza']
if entrada in bebidas:
    print('la bebida si esta en la lista')
else:
    print('la bebida no esta en la lista')

