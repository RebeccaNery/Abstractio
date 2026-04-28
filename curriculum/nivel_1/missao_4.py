MISSAO = {
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
}
