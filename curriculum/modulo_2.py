NIVEL_2 = {
    "id": 1,
    "title": "Nível 2 — As leis do mundo",
    "short": "Pilares",
    "missoes": [
        {
            "id": "1-0",
            "title": "Introdução ao nível",
            "icon": "🌍",
            "theory": """
## As leis do mundo — Os 4 Pilares da POO

Se o Nível 1 te ensinou a **criar** objetos, este nível te ensina as **leis** que governam como bons objetos se comportam.

Os 4 pilares não são recursos isolados — são princípios que trabalham juntos para tornar o código:

- **Organizado** — cada coisa no seu lugar
- **Reutilizável** — escreva uma vez, use muitas vezes
- **Seguro** — proteja dados sensíveis
- **Flexível** — troque partes sem quebrar o todo

### Os 4 Pilares

| Pilar | Palavra-chave | Pergunta que responde |
|---|---|---|
| **Abstração** | Simplificar | O que este objeto *precisa* expor? |
| **Encapsulamento** | Proteger | Quem pode acessar os dados internos? |
| **Herança** | Reutilizar | Como reaproveitar comportamentos existentes? |
| **Polimorfismo** | Uniformizar | Como tratar objetos diferentes da mesma forma? |

> Cada missão a seguir explora um pilar com exemplos práticos. Ao final, você verá como eles se complementam.
""",
            "exercise": {
                "question": "Qual é o principal objetivo dos 4 pilares da POO?",
                "options": [
                    "Aumentar o número de linhas de código para tornar o sistema mais robusto.",
                    "Tornar o código organizado, reutilizável, seguro e flexível.",
                    "Substituir completamente a programação procedural em todos os casos.",
                    "Garantir que todas as classes herdem de uma única superclasse.",
                ],
                "correct": 1,
                "explanation": "Correto! Os pilares são princípios que, juntos, produzem código de qualidade: organizado, reutilizável, seguro e flexível.",
            },
        },
        {
            "id": "1-1",
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
    print(f.descrever())
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
        {
            "id": "1-2",
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
            "id": "1-3",
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
            "id": "1-4",
            "title": "Polimorfismo",
            "icon": "🎭",
            "theory": """
## Polimorfismo

**Polimorfismo** significa "muitas formas". É a capacidade de tratar objetos de tipos diferentes de forma uniforme, desde que compartilhem uma interface comum.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome}: Au au!"

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome}: Miau!"

class Pato(Animal):
    def fazer_som(self):
        return f"{self.nome}: Quack!"

# Polimorfismo em ação — mesmo código, comportamentos diferentes
animais = [Cachorro("Rex"), Gato("Mia"), Pato("Donald")]

for animal in animais:
    print(animal.fazer_som())
# Rex: Au au!
# Mia: Miau!
# Donald: Quack!
```

### Duck Typing — polimorfismo sem herança

Python é flexível: se o objeto tem o método esperado, funciona — independente da hierarquia.

```python
class Robo:
    def fazer_som(self):
        return "Robo: Bip bip!"

# Robo não herda de Animal, mas funciona na mesma lista
todos = [Cachorro("Rex"), Robo()]
for x in todos:
    print(x.fazer_som())
```

> "Se anda como pato e grasna como pato, é um pato." — Duck Typing

### Por que polimorfismo importa?

- Código genérico que funciona com tipos futuros sem modificação
- Reduz condicionais (`if isinstance(...)`)
- Facilita extensão do sistema
""",
            "exercise": {
                "question": "O que é Duck Typing em Python?",
                "options": [
                    "Uma forma de herança múltipla exclusiva do Python.",
                    "A capacidade de usar um objeto em qualquer contexto desde que ele possua os métodos esperados, independente de sua hierarquia de classes.",
                    "Um padrão de projeto para criar objetos do tipo 'pato'.",
                    "Uma verificação estrita de tipos feita em tempo de compilação.",
                ],
                "correct": 1,
                "explanation": "Correto! Duck Typing permite que qualquer objeto seja usado polimorficamente desde que implemente a interface esperada, sem precisar herdar de uma classe específica.",
            },
        },
        {
            "id": "1-5",
            "title": "Resumo",
            "icon": "📋",
            "theory": """
## Resumo — Os 4 Pilares

Você dominou as leis que governam objetos bem projetados. Veja o quadro completo:

| Pilar | Mecanismo em Python | Para que serve |
|---|---|---|
| **Abstração** | `ABC`, `@abstractmethod` | Define contratos, esconde complexidade |
| **Encapsulamento** | `__attr`, `@property` | Protege dados, controla acesso |
| **Herança** | `class Filho(Pai)`, `super()` | Reusa e especializa comportamentos |
| **Polimorfismo** | Override, Duck Typing | Trata objetos distintos uniformemente |

### Os 4 pilares juntos

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):            # Abstração
    def __init__(self, marca):
        self.__marca = marca   # Encapsulamento

    @property
    def marca(self):
        return self.__marca

    @abstractmethod
    def mover(self):           # contrato
        pass

class Carro(Veiculo):          # Herança
    def mover(self):
        return f"{self.marca} rodando na estrada."

class Barco(Veiculo):          # Herança
    def mover(self):
        return f"{self.marca} navegando no mar."

frota = [Carro("Toyota"), Barco("Yamaha")]
for v in frota:
    print(v.mover())           # Polimorfismo
```

> Próximo nível: como objetos se **relacionam** entre si — sobrescrita, contratos e associações.
""",
            "exercise": {
                "question": "Qual pilar garante que código genérico possa operar sobre diferentes tipos de objeto sem precisar conhecê-los individualmente?",
                "options": [
                    "Encapsulamento, porque protege os dados de cada objeto.",
                    "Herança, porque todos os objetos descendem de uma mesma classe.",
                    "Polimorfismo, porque permite tratar objetos distintos de forma uniforme.",
                    "Abstração, porque define quais métodos cada classe deve ter.",
                ],
                "correct": 2,
                "explanation": "Correto! O polimorfismo é o pilar que permite escrever código genérico que funciona com diferentes tipos — sem precisar de condicionais para cada um.",
            },
        },
    ],
}
