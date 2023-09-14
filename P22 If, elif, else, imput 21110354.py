# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:49:01 2023

@author: Javier
"""

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 17:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')
else:
    print('Edad no valida')

    