# Exercício 5 — Desafio

from collections import namedtuple
import math

print("=== Exercício 5 ===")

Stats = namedtuple("Stats", "media mediana minimo maximo desvio_padrao")

def estatisticas(numeros):
    n = len(numeros)

    #média
    media = sum(numeros) / n 

    #mediana 
    ordenados = sorted(numeros)
    if n % 2 == 0:
        #quantidade par
        mediana = (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
    else:
        #quantidade ímpar
        mediana = ordenados[n // 2]

    minimo = min(numeros)
    maximo = max(numeros)

    # desvio padrão, seguindo a fórmula dada:
    # sqrt( soma((x - media)^2) / n )    
    desvio_padrao = math.sqrt(sum((x - media) ** 2 for x in numeros) / n)

    return Stats(media, mediana, minimo, maximo, desvio_padrao)

numeros_teste = [4, 8, 15, 16, 23, 42]
resultado = estatisticas(numeros_teste)
print("Stats:", resultado)
print("Média:", resultado.media)
print("Mediana:", resultado.mediana)
print("Mínimo:", resultado.minimo)
print("Máximo:", resultado.maximo)
print("Desvio padrão:", resultado.desvio_padrao)