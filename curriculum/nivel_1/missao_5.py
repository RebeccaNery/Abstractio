MISSAO = {
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
}
