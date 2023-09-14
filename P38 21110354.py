# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:49:45 2023

@author: Javier
"""

class Usuario:
	def __init__(self, nombre, apellidos):
        

            def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')

usuario002.nombre = 'Jacinto'

usuario002.imprime_datos()