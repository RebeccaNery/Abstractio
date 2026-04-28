MISSAO = {
    "id": "0-5",
    "title": "Resumo",
    "icon": "📋",
    "theory": """
## Resumo — Fundamentos

Você concluiu o primeiro nível! Veja os conceitos que domina agora:

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

> Próximo nível: os **4 pilares da POO** — os princípios que tornam o código orientado a objetos poderoso.
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
}
