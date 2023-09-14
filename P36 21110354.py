# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:22:02 2023

@author: Javier
"""

class Carro:
    modelo = ''
    año = ''
    
    def compra(self):
     print('Modelo:', self.modelo, '\nAño:', self.año)
    
carro001 = Carro()

carro001.modelo = 'Ford GT40'
carro001.año = '1967'

carro001.compra()
    
