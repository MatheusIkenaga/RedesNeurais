# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

entradas = np.array([1,7,5])
pesos = np.array([0.8,0.1,0])

def soma (e,p):
    return e.dot(p)
# chamado de dot product / produto escalar

s = soma (entradas, pesos)

def stepFuncion(soma):
    if (soma>= 1):
        return 1
    return 0

r = stepFuncion(s)