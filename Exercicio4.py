# Exercício 4 — Named Tuples

from collections import namedtuple

print("=== Exercício 4 ===")

# a) Criar named tuple e instanciar 3 produtos
Produto = namedtuple("Produto", "nome preco estoque categoria")
p1 = Produto("Notebook", 2500.00, 5, "Eletrônicos")
p2 = Produto("Caneta", 3.50, 100, "Papelaria")
p3 = Produto("Mouse", 80.00, 20, "Eletrônicos")
print("\na)", p1)
print("a)", p2)
print("a)", p3)

# b) Lista de produtos + list comprehensions
produtos = [p1, p2, p3]
caros = [p for p in produtos if p.preco > 100]
print("\nb) produto acima de R$100:", caros)

valores_totais = [(p.nome, p.preco * p.estoque) for p in produtos]
print("b) valor total por produto:", valores_totais)

mais_caro = max(produtos, key=lambda p: p.preco)
print("b) produto mais caro:", mais_caro)

# c) Named tuple para o Dungeon Quest
Habilidade = namedtuple("Habilidade", "nome descricao custo_mp dano")

habilidade_guerreiro = Habilidade("Golpe Poderoso","Um ataque físico pesado", 10, 25)
habilidade_mago = Habilidade("Bola de fogo", "Ataque mágico de fogo em área", 20, 35)
habilidade_arqueiro = Habilidade("Tiro Certeiro", "Flecha precisa com bônus de crítico", 15, 20)

print("\nc)", habilidade_guerreiro)
print("c)", habilidade_mago)
print("c)", habilidade_arqueiro)