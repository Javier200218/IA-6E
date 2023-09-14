# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:57:36 2023

@author: Javier
"""

class Usuarios:
 def __init__(self, nombre, apellidos)
		self.nombre = nombre
	self.apellidos = apellidos

    
        def imprime_datos(self):
		 print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios):
	pass