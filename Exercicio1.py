#Exercícios de Tuplas — Python

# EXERCÍCIO 1 — BÁSICO

print("---Exercício 01---")

# a) Criar tupla e acessar elementos
estacoes = ("Primavera", "Verão", "Outono", "Inverno")
print("a) 2ª estação:", estacoes[1])                   # índice 1 = 2º elemento
print("a) duas últimas:", estacoes[-2:])               # fatiamento pega os 2 últimos
print("a) quantidade:", len(estacoes))                 # len() conta os elementos

# b) Tentar modificar a tupla (isso dá erro, por isso está comentado)
# estacoes[1] = "Verão trocado"
# Ao rodar a linha acima descomentada, o python lança:
# TyperError: 'tuple' object does not support item assignment
# Isso acontece porque tuplas são IMUTÁVEIS - depois de criadas,
# seus valores não podem ser alterados.

# c) Diferença entre (42) e (42,)
a = (42)    # os parênteses aqui só agrupam a expressão, não criam tupla
b = (42,)   # a vírgula é o que cria a tupla de fato
print("\nc) type(a):", type(a))   
print("c) type(b):", type(b))   
# Em python é a vírgula que define uma tupla, não os parênteses.

# d) Tupla RGB e desempacotamento
cor = (255, 0, 0)
r, g, b_ = cor               # desempacotamento (usei b_ pra não confundir com o 'b' de cima)
brilho = (r + g + b_) / 3
print("\nd) r,g,b:", r, g, b_)
print("d) brilho:", brilho)