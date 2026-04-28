MISSAO = {
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
}
