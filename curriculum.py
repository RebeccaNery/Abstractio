CURRICULUM = [
    {
        "id": 0,
        "title": "Módulo 1 — Introdução",
        "short": "Introdução",
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
                "title": "Classes",
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
                "title": "Objetos",
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
                "title": "Métodos",
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
        ],
    },
    {
        "id": 1,
        "title": "Módulo 2 — Conceitos Avançados",
        "short": "Avançado",
        "sections": [
            {
                "id": "1-0",
                "title": "Encapsulamento",
                "icon": "🔒",
                "theory": """
## Encapsulamento

**Encapsulamento** é o princípio de esconder os detalhes internos de um objeto e expor apenas o necessário através de uma interface controlada.

Em Python, convenções de nomenclatura indicam visibilidade:

| Prefixo | Visibilidade | Exemplo |
|---|---|---|
| `atributo` | Público | `self.nome` |
| `_atributo` | Protegido (convenção) | `self._agencia` |
| `__atributo` | Privado (name mangling) | `self.__saldo` |

```python
class ContaCorrente:
    def __init__(self, titular, saldo):
        self.titular = titular     # público
        self._agencia = "0001"     # protegido
        self.__saldo = saldo       # privado

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

conta = ContaCorrente("João", 500)
print(conta.titular)      # João — OK
print(conta.get_saldo())  # 500 — OK via getter
# conta.__saldo           # AttributeError!
```

### `@property` — getters e setters elegantes

```python
@property
def saldo(self):
    return self.__saldo

@saldo.setter
def saldo(self, valor):
    if valor >= 0:
        self.__saldo = valor
```
""",
                "exercise": {
                    "question": "Qual é o principal objetivo do encapsulamento em POO?",
                    "options": [
                        "Permitir que qualquer parte do código acesse e modifique os dados livremente.",
                        "Esconder os detalhes internos do objeto e controlar o acesso aos seus dados.",
                        "Fazer com que uma classe herde comportamentos de outra.",
                        "Substituir funções globais por métodos de classe.",
                    ],
                    "correct": 1,
                    "explanation": "Correto! Encapsulamento protege os dados internos e expõe apenas uma interface controlada e segura.",
                },
            },
            {
                "id": "1-1",
                "title": "Herança",
                "icon": "🧬",
                "theory": """
## Herança

**Herança** permite que uma classe filha (subclasse) herde atributos e métodos de uma classe pai (superclasse), promovendo reuso e especialização.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def respirar(self):
        return f"{self.nome} está respirando."

    def fazer_som(self):
        return "..."

class Cachorro(Animal):    # herda de Animal
    def fazer_som(self):   # sobrescreve (override)
        return f"{self.nome} diz: Au au!"

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} diz: Miau!"

rex = Cachorro("Rex")
print(rex.respirar())   # Rex está respirando. ← herdado
print(rex.fazer_som())  # Rex diz: Au au!     ← sobrescrito
```

### `super()` — acessando a classe pai

```python
class AnimalDomestico(Animal):
    def __init__(self, nome, dono):
        super().__init__(nome)  # chama Animal.__init__
        self.dono = dono
```

Python também suporta **herança múltipla**: `class Anfibio(Terrestre, Aquatico): pass`
""",
                "exercise": {
                    "question": "O que acontece quando uma subclasse define um método com o mesmo nome que a superclasse?",
                    "options": [
                        "Ocorre um erro de execução.",
                        "O método da subclasse sobrescreve (override) o da superclasse para aquela instância.",
                        "Ambos os métodos são executados simultaneamente.",
                        "O método da superclasse sempre tem prioridade.",
                    ],
                    "correct": 1,
                    "explanation": "Correto! Isso se chama override (sobrescrita). A subclasse redefine o comportamento para suas próprias instâncias.",
                },
            },
            {
                "id": "1-2",
                "title": "Abstração",
                "icon": "🌀",
                "theory": """
## Abstração

**Abstração** é o processo de focar nos aspectos essenciais, ignorando detalhes irrelevantes. Em Python, implementamos via **classes abstratas** com o módulo `abc`.

Uma classe abstrata define um **contrato**: todas as subclasses *devem* implementar certos métodos.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def descrever(self):  # método concreto compartilhado
        return f"Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}"

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * self.raio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.raio

class Retangulo(Forma):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimetro(self):
        return 2 * (self.w + self.h)

formas = [Circulo(5), Retangulo(4, 6)]
for f in formas:
    print(f.descrever())  # Polimorfismo em ação!
```

### Vantagens
- Força um contrato entre classes
- Habilita **polimorfismo**: tratar `Circulo` e `Retangulo` uniformemente como `Forma`
- Separa *o quê* fazer do *como* fazer
""",
                "exercise": {
                    "question": "O que caracteriza uma **classe abstrata** em Python?",
                    "options": [
                        "Uma classe que não pode ter nenhum método implementado.",
                        "Uma classe que herda de `ABC` e define métodos abstratos que as subclasses são obrigadas a implementar.",
                        "Uma classe que só pode ser instanciada uma única vez.",
                        "Uma classe privada que não pode ser importada por outros módulos.",
                    ],
                    "correct": 1,
                    "explanation": "Perfeito! Classes abstratas (ABC) definem contratos. Métodos com @abstractmethod obrigam as subclasses a implementá-los.",
                },
            },
        ],
    },
]


def get_flat_sections():
    """Returns list of (module_idx, section_idx, section_dict)."""
    flat = []
    for m_idx, module in enumerate(CURRICULUM):
        for s_idx, section in enumerate(module["sections"]):
            flat.append((m_idx, s_idx, section))
    return flat


def get_total_sections():
    return sum(len(m["sections"]) for m in CURRICULUM)
