# Exercício 3 — Tupla vs. Lista
# Para cada situação, justifique se usaria tupla ou lista.

print("=== Exercício 03 ===")

resposta_ex03 = """
a) Notas de uma turma que pode crescer -> LISTA
a quantidade de notas muda ao longo do semestre, então precisa de uma 
estrutura que aceite adicionar/remover elementos.

b) Coordenadas (latitude, longitude) -> TUPLA
sempre são exatamente 2 valores fixos, que juntos representam um único
ponto: não faz sentido "crescer" ou reordenar.

c) Dias da semana -> TUPLA
é uma sequência fixa que nunca muda, 
sempre os mesmo 7 dias, na mesma ordem.

d) Invetário de um personagem de jogo -> LISTA
itens são adicionados e removidos o tempo todo 
durante o jogo, não tem nada fixo.

e) Atributos (nome, raça, classe) de um personagem -> TUPLA
depois que o personagem é criado, esse conjunto de dados não muda de 
estrutura, é um "pacote fixo" de informações.

f) Sequência de movimentos numa partida de xadrez -> LISTA
os movimentos vão sendo adicionados um a um conforme a partida acontece.
"""
print(resposta_ex03)