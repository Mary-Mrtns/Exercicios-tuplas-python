# Exercício 2 — Desempacotamento

print("=== Exercício 02 ===")

# a) Desempacotar tupla simples
dados = ("Ana Silva", 25, "Python", 9.5)
nome, idade, linguagem, nota = dados
print("\na)", nome, idade, linguagem, nota)

# b) Desempacotamento com * (star expression)
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
primeiro, *meio, ultimo = numeros
print("\nb) primeiro:", primeiro)
print("b) meio", meio)
print("b) último:", ultimo)

# c) Função que retorna tupla (quociente, resto)
def dividir_e_resto(a, b):
    return a // b, a % b    # o return com vírgula já cria a tupla

q, r = dividir_e_resto(17, 5)   # desempacotando o retorno da função
print("\nc) quociente:", q, "| resto:", r)

# d) Swap de três variáveis em uma linha 
a, b, c = 1, 2, 3
a, b, c = c, a, b   # o lado direito monta uma tupla temporária (3,1,2) antes de atribuir
print("\nd) a =", a, "b =", b, "c =", c)