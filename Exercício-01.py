#Exercícios de Tuplas — Python

from collections import namedtuple
import math

# EXERCÍCIO 1 — BÁSICO

print("---Exercício 01---")

# a) Criar tupla e acessar elementos
estacoes = ("Primavera", "Verão", "Outono", "Inverno")
print("a) 2ª estação:", estacoes[1])                   # índice 1 = 2º elemento
print("a) duas últimas:", estacoes[-2:])               # fatiamento pega os 2 últimos
print("a) quantidade:", len(estacoes))                 # len() conta os elementos