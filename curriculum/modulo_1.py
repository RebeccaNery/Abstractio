MODULO_1 = {
    "id": 0,
    "title": "Módulo 1 — Fundamentos",
    "short": "Fundamentos",
    "sections": [
        {
            "id": "0-0",
            "title": "O que é POO?",
            "icon": "🧩",
            "theory": """
## O que é Programação Orientada a Objetos?

A **Programação Orientada a Objetos (POO)** é um paradigma que organiza o software em torno de **objetos** — entidades que combinam dados (atributos) e comportamentos (métodos).

Em vez de uma sequência linear de instruções, você pensa em um conjunto de objetos que colaboram entre si.

### Os 4 pilares da POO

| Pilar | Definição |
|---|---|
| **Encapsulamento** | Esconder a complexidade interna |
| **Herança** | Reutilizar e estender comportamentos |
| **Polimorfismo** | Tratar objetos distintos de forma uniforme |
| **Abstração** | Focar no essencial, ignorar detalhes |

### Exemplo inicial

```python
class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return f"{self.nome} diz: Au au!"

rex = Cachorro("Rex")
print(rex.latir())  # Rex diz: Au au!
```
""",
            "exercise": {
                "question": "Qual das alternativas melhor define a Programação Orientada a Objetos?",
                "options": [
                    "Uma sequência linear de instruções que o computador executa.",
                    "Um paradigma que organiza o software em torno de objetos com atributos e métodos.",
                    "Uma linguagem de programação específica como Python ou Java.",
                    "Um método exclusivo para criar interfaces gráficas.",
                ],
                "correct": 1,
                "explanation": "Correto! POO é um paradigma que organiza o código em objetos com atributos (dados) e métodos (comportamentos).",
            },
        },
        {
            "id": "0-1",
            "title": "Classe",
            "icon": "📐",
            "theory": """
## Classes

Uma **classe** é uma estrutura que define um tipo de dado composto. Ela descreve atributos (estado) e métodos (comportamentos) que os objetos dessa classe terão.

> **Analogia:** A classe é o molde/planta; o objeto é o produto construído a partir dela.

- **Classe** = molde que descreve propriedades e comportamentos
- **Objeto** = instância concreta da classe, com valores específicos
- **Membros comuns:** atributos, métodos, construtor (`__init__`)

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, sou {self.nome}, {self.idade} anos."

p1 = Pessoa("Ana", 25)
p2 = Pessoa("Carlos", 30)

print(p1.apresentar())  # Olá, sou Ana, 25 anos.
print(p2.apresentar())  # Olá, sou Carlos, 30 anos.
```
""",
            "exercise": {
                "question": "Escolha a alternativa que melhor define o que é uma **classe**:",
                "options": [
                    "Um objeto específico criado em tempo de execução.",
                    "Um molde que descreve as propriedades e comportamentos de um tipo de objeto.",
                    "Uma biblioteca externa usada para executar a linguagem.",
                    "Um erro de sintaxe comum em Python.",
                ],
                "correct": 1,
                "explanation": "Exato! Uma classe é um molde. A partir dela criamos quantos objetos (instâncias) quisermos.",
            },
        },
        {
            "id": "0-2",
            "title": "Objeto",
            "icon": "🔵",
            "theory": """
## Objetos

Um **objeto** é uma instância concreta de uma classe. Se a classe é o molde, o objeto é o produto criado a partir desse molde.

Cada objeto tem seu próprio conjunto de valores para os atributos, mas compartilha os métodos da classe.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        return f"{self.modelo} ligado!"

    def desligar(self):
        self.ligado = False
        return f"{self.modelo} desligado."

fusca = Carro("Volkswagen", "Fusca")
gol   = Carro("Volkswagen", "Gol")

print(fusca.ligar())  # Fusca ligado!
print(gol.ligar())    # Gol ligado!
```

### Três características de todo objeto

| Característica | Significado |
|---|---|
| **Identidade** | O que diferencia um objeto do outro (referência em memória) |
| **Estado** | Valores atuais dos atributos (`fusca.ligado = True`) |
| **Comportamento** | O que o objeto pode fazer (seus métodos) |
""",
            "exercise": {
                "question": "Dado `class Gato`, qual opção cria corretamente **dois objetos distintos**?",
                "options": [
                    "`gato1 = Gato` e `gato2 = Gato`",
                    "`gato1 = Gato()` e `gato2 = Gato()`",
                    "`gato1 = new Gato()` e `gato2 = new Gato()`",
                    "`Gato.gato1()` e `Gato.gato2()`",
                ],
                "correct": 1,
                "explanation": "Correto! Em Python, instanciamos objetos chamando a classe como função: `Gato()`. Cada chamada cria uma instância independente.",
            },
        },
        {
            "id": "0-3",
            "title": "Método",
            "icon": "⚙️",
            "theory": """
## Métodos

**Métodos** são funções definidas dentro de uma classe que descrevem os comportamentos dos objetos. Eles sempre recebem `self` como primeiro parâmetro — uma referência ao objeto que os chamou.

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado."

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= valor
        return f"Saque de R${valor:.2f} realizado."

conta = ContaBancaria("Maria", 100.0)
print(conta.depositar(50))  # Depósito de R$50.00 realizado.
print(conta.sacar(30))      # Saque de R$30.00 realizado.
print(conta.saldo)          # 120.0
```

### Por que `self`?

- `self` é a referência ao objeto atual
- Permite acessar e modificar atributos da instância específica
- O Python injeta `self` automaticamente — você não o informa ao chamar o método
""",
            "exercise": {
                "question": "Por que todo método de instância em Python deve ter `self` como primeiro parâmetro?",
                "options": [
                    "É uma convenção opcional que melhora apenas a legibilidade.",
                    "Para que o método acesse e modifique os atributos do objeto específico que o chamou.",
                    "Porque o Python exige que toda função tenha ao menos um parâmetro.",
                    "Para indicar que o método é público e acessível externamente.",
                ],
                "correct": 1,
                "explanation": "Correto! `self` é uma referência à instância. Sem ele, o método não saberia qual objeto está manipulando.",
            },
        },
        {
            "id": "0-4",
            "title": "Construtor",
            "icon": "🏗️",
            "theory": """
## Construtor

O **construtor** é um método especial chamado automaticamente no momento em que um objeto é criado. Em Python, ele se chama `__init__`.

Sua responsabilidade é **inicializar o estado do objeto** — definir os valores iniciais dos atributos.

```python
class Produto:
    def __init__(self, nome, preco, estoque=0):
        self.nome    = nome
        self.preco   = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} — R${self.preco:.2f} ({self.estoque} em estoque)"

p1 = Produto("Caneta", 2.50, 100)
p2 = Produto("Caderno", 15.00)   # estoque usa valor padrão: 0

print(p1)  # Caneta — R$2.50 (100 em estoque)
print(p2)  # Caderno — R$15.00 (0 em estoque)
```

### Recursos do construtor

| Recurso | Descrição |
|---|---|
| Parâmetros obrigatórios | `def __init__(self, nome)` |
| Parâmetros com padrão | `def __init__(self, estoque=0)` |
| `__str__` | Define como o objeto é exibido ao ser impresso |

### Destrutor

Python também possui `__del__`, chamado quando o objeto é destruído — mas raramente é necessário usá-lo.

```python
def __del__(self):
    print(f"{self.nome} foi removido da memória.")
```
""",
            "exercise": {
                "question": "O que acontece quando você executa `p = Produto('Caneta', 2.50)`?",
                "options": [
                    "Nada — é preciso chamar `p.init()` manualmente depois.",
                    "O Python chama `__init__` automaticamente, inicializando os atributos do objeto.",
                    "Um erro é lançado porque `__init__` não foi chamado explicitamente.",
                    "O objeto é criado, mas seus atributos ficam como `None` até serem definidos.",
                ],
                "correct": 1,
                "explanation": "Correto! `__init__` é chamado automaticamente pelo Python no momento da criação do objeto. Você não precisa invocá-lo.",
            },
        },
        {
            "id": "0-5",
            "title": "Resumo",
            "icon": "📋",
            "theory": """
## Resumo — Fundamentos

Você concluiu o primeiro módulo! Veja os conceitos que domina agora:

### O que você aprendeu

| Conceito | Em uma linha |
|---|---|
| **POO** | Paradigma que organiza código em objetos com dados e comportamentos |
| **Classe** | Molde que define atributos e métodos de um tipo de objeto |
| **Objeto** | Instância concreta de uma classe, com estado próprio |
| **Método** | Função definida dentro de uma classe; recebe `self` |
| **Construtor** | `__init__` — inicializa o estado do objeto na criação |

### Tudo junto

```python
class Livro:
    def __init__(self, titulo, autor, paginas):  # construtor
        self.titulo  = titulo                    # atributos
        self.autor   = autor
        self.paginas = paginas
        self.lido    = False

    def marcar_lido(self):                       # método
        self.lido = True
        return f'"{self.titulo}" marcado como lido!'

    def __str__(self):
        status = "✓ lido" if self.lido else "pendente"
        return f"{self.titulo} ({self.autor}) — {status}"

# Criando objetos
livro1 = Livro("Clean Code", "Robert Martin", 431)
livro2 = Livro("O Poder do Hábito", "Charles Duhigg", 288)

print(livro1.marcar_lido())  # "Clean Code" marcado como lido!
print(livro1)                # Clean Code (Robert Martin) — ✓ lido
print(livro2)                # O Poder do Hábito (Charles Duhigg) — pendente
```

> Próximo módulo: os **4 pilares da POO** — os princípios que tornam o código orientado a objetos poderoso.
""",
            "exercise": {
                "question": "Qual sequência representa corretamente a relação entre classe, construtor e objeto?",
                "options": [
                    "O objeto é criado → o construtor define a classe → a classe armazena atributos.",
                    "A classe é o molde → o construtor inicializa o estado → o objeto é a instância resultante.",
                    "O construtor cria a classe → a classe instancia objetos → os objetos chamam métodos.",
                    "A classe herda do objeto → o construtor é opcional → os métodos definem os atributos.",
                ],
                "correct": 1,
                "explanation": "Exato! A classe define o molde, o construtor (`__init__`) prepara o estado inicial, e o objeto é a instância concreta criada a partir disso.",
            },
        },
    ],
}
