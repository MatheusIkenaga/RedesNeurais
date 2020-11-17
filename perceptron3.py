#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:05:02 2020

@author: matheusikenaga
"""

import numpy as np
#Inputs and Outputs for  AND
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,0,0,1])

#Inputs and Outputs for  OR
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,1,1,1])

#Inputs and Outputs for XOR
# It is not posssible to solve a XOR Operator with this algorithm, because it's not linear
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,1,1,0])

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFuncion(soma):
    if (soma>= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFuncion(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            #abs faz o valor não ficar negativo
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j]* erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros:' + str(erroTotal))
                
treinar()
print("Rede neural treinada")
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))