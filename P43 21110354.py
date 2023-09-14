# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 00:45:17 2023

@author: Javier
"""

import math

area = lambda radio: (math.pi * radio * radio)

print(area(2))



def area(radio):
	resultado = math.pi * radio * radio
	print(resultado)

area(2)