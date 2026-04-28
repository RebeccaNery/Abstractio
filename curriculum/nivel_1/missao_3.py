MISSAO = {
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
}
