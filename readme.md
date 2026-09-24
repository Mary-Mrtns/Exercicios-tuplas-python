# Exercícios de Tuplas em Python

## Sobre mim

Sou Mariany (Mary), estudante de Engenharia de Software na ULBRA. Este repositório é parte do meu portfólio, onde documento os projetos e exercícios que vou desenvolvendo ao longo do curso.

## Por que estou postando isso

Este repositório reúne exercícios que resolvi enquanto estudava **tuplas em Python**, atividade da disciplina de **Laboratório de Programação em Python**, do 2º semestre da minha faculdade, desde os conceitos básicos (criação, imutabilidade) até tópicos mais avançados como desempacotamento, `namedtuple` e cálculo de estatísticas manualmente. Estou documentando aqui como parte do meu processo de aprendizado e para deixar registrado no meu portfólio o que venho estudando em Engenharia de Software.

## Como usar

1. Clone este repositório:
   ```bash
   git clone <link-do-seu-repositorio>
   ```
2. Entre na pasta do projeto:
   ```bash
   cd nome-da-pasta
   ```
3. Execute o arquivo do exercício que quiser ver, com Python 3 instalado:
   ```bash
   python3 exercicio1.py
   python3 exercicio2.py
   python3 exercicio3.py
   python3 exercicio4.py
   python3 exercicio5.py
   ```
4. Cada arquivo exibe no terminal as respostas do exercício correspondente.

> Não é necessário instalar nenhuma biblioteca externa — o código usa apenas recursos nativos do Python (`collections.namedtuple` e `math`).

---

## Enunciados

### Exercício 1 — Básico

a) Crie uma tupla com as estações do ano. Exiba a 2ª estação, as duas últimas e quantas estações existem.

b) Tente modificar o 2° elemento da tupla. O que acontece?

c) Qual a diferença entre `(42)` e `(42,)`? Verifique com `type()`.

d) Crie uma tupla de cores RGB: `(255, 0, 0)` (vermelho). Desempacote em variáveis `r, g, b`. Calcule o brilho: `(r + g + b) / 3`.

### Exercício 2 — Desempacotamento

a) Dada a tupla `dados = ("Ana Silva", 25, "Python", 9.5)`, desempacote em `nome, idade, linguagem, nota`.

b) Dada `numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`, use `*` para separar o primeiro, o último e o resto do meio.

c) Escreva uma função `dividir_e_resto(a, b)` que retorna uma tupla `(quociente, resto)`. Use desempacotamento ao chamar a função.

d) Faça o swap de três variáveis `a, b, c = 1, 2, 3` → `a=3, b=1, c=2` em uma única linha.

### Exercício 3 — Tupla vs. Lista

Para cada situação, justifique se usaria **tupla** ou **lista**:

a) Uma coleção de notas de uma turma que pode crescer ao longo do semestre.

b) As coordenadas (latitude, longitude) de uma cidade.

c) Os dias da semana.

d) O inventário de um personagem de jogo.

e) Os atributos (nome, raça, classe) de um personagem criado na criação de conta.

f) A sequência de movimentos numa partida de xadrez.

### Exercício 4 — Named Tuples

a) Crie um named tuple `Produto(nome, preco, estoque, categoria)`. Instancie 3 produtos diferentes e exiba-os.

b) Crie uma lista de `Produto` e use list comprehension para:
- Filtrar apenas os que custam mais de R$ 100.
- Calcular o valor total em estoque de cada produto.
- Encontrar o produto mais caro.

c) Adicione ao Dungeon Quest um `namedtuple Habilidade(nome, descricao, custo_mp, dano)` e defina as habilidades de cada classe.

### Exercício 5 — Desafio

Crie uma função `estatisticas(numeros)` que retorna uma named tuple `Stats(media, mediana, minimo, maximo, desvio_padrao)`. Implemente o desvio padrão manualmente (sem `statistics`):

```python
desvio = sqrt(sum((x - media)**2 for x in dados) / len(dados))
```

---

📁 O código com as resoluções está dividido em um arquivo por exercício:
[`exercicio1.py`](./exercicio1.py) · [`exercicio2.py`](./exercicio2.py) · [`exercicio3.py`](./exercicio3.py) · [`exercicio4.py`](./exercicio4.py) · [`exercicio5.py`](./exercicio5.py)