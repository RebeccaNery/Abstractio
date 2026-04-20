MODULO_4 = {
    "id": 3,
    "title": "Módulo 4 — O arquiteto mestre",
    "short": "Arquitetura",
    "sections": [
        {
            "id": "3-0",
            "title": "Introdução ao módulo",
            "icon": "🏛️",
            "theory": """
## O arquiteto mestre — Engenharia e Qualidade

Você sabe criar objetos, aplicar os pilares e modelar relações. Agora é hora de pensar como um **arquiteto de software** — alguém que projeta sistemas que resistem ao tempo.

Código que funciona hoje, mas que ninguém consegue manter amanhã, não é bom código. Este módulo trata de princípios e ferramentas que tornam sistemas **sustentáveis**.

### O que você vai aprender

| Conceito | O que resolve |
|---|---|
| **Coesão** | Cada classe faz uma coisa só — e bem |
| **Acoplamento** | Reduzir dependências entre partes do sistema |
| **SOLID** | 5 princípios para design orientado a objetos de qualidade |
| **Generics** | Código que funciona com qualquer tipo com segurança |
| **Design Patterns** | Soluções consagradas para problemas recorrentes |

### A metáfora do arquiteto

Um bom arquiteto não apenas empilha tijolos — ele projeta estruturas que:
- São fáceis de **modificar** sem derrubar tudo
- Podem **crescer** sem se tornarem caóticas
- São **compreensíveis** por qualquer pessoa da equipe

> Esses princípios são o que diferencia desenvolvedores juniores de sêniores.
""",
            "exercise": {
                "question": "O que caracteriza um sistema com boa qualidade de design em POO?",
                "options": [
                    "Ter o maior número possível de classes e métodos.",
                    "Ser fácil de modificar, crescer e entender sem quebrar partes não relacionadas.",
                    "Usar sempre todos os 4 pilares da POO em cada classe.",
                    "Evitar o uso de herança e composição para reduzir complexidade.",
                ],
                "correct": 1,
                "explanation": "Correto! Um bom design é aquele que permite evolução sem colapso — modificável, extensível e compreensível.",
            },
        },
        {
            "id": "3-1",
            "title": "Coesão",
            "icon": "🎯",
            "theory": """
## Coesão

**Coesão** mede o quanto os elementos de uma classe estão relacionados entre si. Alta coesão significa que a classe tem **um único propósito bem definido**.

### Baixa coesão — o problema

```python
# Classe faz demais — baixa coesão
class Usuario:
    def __init__(self, nome, email):
        self.nome  = nome
        self.email = email

    def salvar_no_banco(self): ...       # responsabilidade de banco
    def enviar_email_boas_vindas(self): ...  # responsabilidade de email
    def gerar_relatorio_pdf(self): ...   # responsabilidade de relatório
    def validar_cpf(self): ...           # responsabilidade de validação
```

Quando qualquer coisa mudar (banco, email, PDF), você mexe em `Usuario` — arriscando quebrar as outras funcionalidades.

### Alta coesão — a solução

```python
class Usuario:
    def __init__(self, nome, email):
        self.nome  = nome
        self.email = email

class RepositorioUsuario:
    def salvar(self, usuario: Usuario): ...

class ServicoEmail:
    def boas_vindas(self, usuario: Usuario): ...

class ValidadorCPF:
    def validar(self, cpf: str) -> bool: ...
```

Agora cada classe tem **uma razão para mudar**. Isso é o princípio SRP (Single Responsibility) do SOLID.

### Como medir coesão?

Faça a pergunta: **"O que esta classe faz?"**
- Se a resposta tem muitos "e também..." → baixa coesão
- Se a resposta é uma frase curta e precisa → alta coesão

| Sinal | Coesão |
|---|---|
| Métodos usam os mesmos atributos | Alta |
| Métodos ignoram atributos da classe | Baixa |
| Classe difícil de nomear | Baixa |
""",
            "exercise": {
                "question": "Como identificar que uma classe tem **baixa coesão**?",
                "options": [
                    "A classe tem poucos métodos e atributos.",
                    "A classe é difícil de nomear e seus métodos têm responsabilidades não relacionadas entre si.",
                    "A classe herda de mais de uma superclasse.",
                    "A classe usa muitas outras classes do sistema.",
                ],
                "correct": 1,
                "explanation": "Correto! Baixa coesão se manifesta quando a classe acumula responsabilidades diferentes — o que a torna difícil de nomear, testar e manter.",
            },
        },
        {
            "id": "3-2",
            "title": "Acoplamento",
            "icon": "🔓",
            "theory": """
## Acoplamento

**Acoplamento** mede o grau de dependência entre classes. **Alto acoplamento** significa que mudanças em uma classe forçam mudanças em outras — o sistema vira uma "bola de neve".

### Alto acoplamento — o problema

```python
class Pedido:
    def finalizar(self):
        db = MySQLConexao("localhost", "root", "senha")  # dependência direta
        db.salvar(self)
        smtp = SMTPEmailSender("smtp.gmail.com", 587)    # dependência direta
        smtp.enviar("Pedido confirmado!")
```

`Pedido` conhece detalhes de banco e email. Trocar MySQL por PostgreSQL exige mexer em `Pedido`.

### Baixo acoplamento — a solução (Injeção de Dependência)

```python
from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, pedido): pass

class Notificador(ABC):
    @abstractmethod
    def enviar(self, msg: str): pass

class Pedido:
    def __init__(self, repo: Repositorio, notif: Notificador):
        self.repo  = repo   # recebe dependência de fora
        self.notif = notif

    def finalizar(self):
        self.repo.salvar(self)
        self.notif.enviar("Pedido confirmado!")

# Trocar implementações sem tocar em Pedido:
class MySQLRepositorio(Repositorio):
    def salvar(self, pedido): ...

class EmailNotificador(Notificador):
    def enviar(self, msg): ...

pedido = Pedido(MySQLRepositorio(), EmailNotificador())
pedido.finalizar()
```

### Coesão x Acoplamento

| | Alta Coesão | Baixo Acoplamento |
|---|---|---|
| Foco | Dentro da classe | Entre classes |
| Meta | Classe com propósito único | Classes com poucas dependências |
| Benefício | Fácil de manter | Fácil de trocar partes |

> O objetivo é sempre: **alta coesão + baixo acoplamento**.
""",
            "exercise": {
                "question": "O que é Injeção de Dependência e como ela reduz o acoplamento?",
                "options": [
                    "É uma técnica de herança que injeta métodos de uma classe em outra automaticamente.",
                    "É passar as dependências de uma classe de fora para dentro (via construtor ou método), em vez de criá-las internamente.",
                    "É um padrão que aumenta o acoplamento para garantir mais controle sobre as dependências.",
                    "É injetar código diretamente no banco de dados para reduzir chamadas externas.",
                ],
                "correct": 1,
                "explanation": "Correto! Injeção de dependência desacopla a classe de suas implementações concretas — ela recebe o que precisa de fora, facilitando troca e testes.",
            },
        },
        {
            "id": "3-3",
            "title": "SOLID",
            "icon": "🪨",
            "theory": """
## SOLID

**SOLID** é um acrônimo com 5 princípios de design orientado a objetos, definidos por Robert C. Martin. São guias para código limpo, manutenível e extensível.

| Letra | Princípio | Em uma linha |
|---|---|---|
| **S** | Single Responsibility | Uma classe, uma razão para mudar |
| **O** | Open/Closed | Aberta para extensão, fechada para modificação |
| **L** | Liskov Substitution | Subclasses devem poder substituir a superclasse |
| **I** | Interface Segregation | Interfaces específicas > uma interface genérica |
| **D** | Dependency Inversion | Dependa de abstrações, não de implementações |

### S — Single Responsibility

```python
# Ruim: duas responsabilidades
class Relatorio:
    def calcular(self): ...
    def salvar_pdf(self): ...

# Bom: separadas
class CalculadoraRelatorio:
    def calcular(self): ...

class ExportadorPDF:
    def salvar(self, relatorio): ...
```

### O — Open/Closed

```python
# Extensível sem modificar o código existente
class Desconto(ABC):
    @abstractmethod
    def aplicar(self, preco): pass

class DescontoVIP(Desconto):
    def aplicar(self, preco): return preco * 0.8

class DescontoEstudante(Desconto):
    def aplicar(self, preco): return preco * 0.9
```

### L — Liskov Substitution

```python
# Subclasse deve funcionar onde a superclasse é esperada
def calcular_area(forma: Forma) -> float:
    return forma.area()  # funciona com Circulo, Retangulo, etc.
```

### I — Interface Segregation

```python
# Ruim: interface geral demais
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self): pass
    @abstractmethod
    def comer(self): pass  # robôs não comem!

# Bom: interfaces específicas
class Trabalhavel(ABC):
    @abstractmethod
    def trabalhar(self): pass

class Alimentavel(ABC):
    @abstractmethod
    def comer(self): pass
```

### D — Dependency Inversion

```python
# Dependa da abstração (Repositorio), não da implementação (MySQL)
class Servico:
    def __init__(self, repo: Repositorio):  # abstração
        self.repo = repo
```
""",
            "exercise": {
                "question": "O princípio **Open/Closed** diz que classes devem ser:",
                "options": [
                    "Abertas para modificação e fechadas para extensão.",
                    "Abertas para extensão (novos comportamentos via subclasses) e fechadas para modificação do código existente.",
                    "Abertas apenas para herança múltipla e fechadas para composição.",
                    "Fechadas para qualquer tipo de mudança após a primeira versão.",
                ],
                "correct": 1,
                "explanation": "Correto! Open/Closed significa que você adiciona funcionalidade criando novas classes (extensão), sem modificar as existentes — protegendo o que já funciona.",
            },
        },
        {
            "id": "3-4",
            "title": "Generics",
            "icon": "🧪",
            "theory": """
## Generics

**Generics** (ou tipos genéricos) permitem criar classes e funções que funcionam com **qualquer tipo**, mantendo segurança de tipos verificável por ferramentas como `mypy`.

Em Python, usamos o módulo `typing`.

### O problema sem generics

```python
class Pilha:
    def __init__(self):
        self._itens = []

    def empilhar(self, item):
        self._itens.append(item)

    def desempilhar(self):
        return self._itens.pop()

p = Pilha()
p.empilhar(42)
p.empilhar("oops")  # mistura de tipos — sem aviso!
```

### Com Generics

```python
from typing import Generic, TypeVar

T = TypeVar("T")  # T representa qualquer tipo

class Pilha(Generic[T]):
    def __init__(self):
        self._itens: list[T] = []

    def empilhar(self, item: T) -> None:
        self._itens.append(item)

    def desempilhar(self) -> T:
        return self._itens.pop()

    def topo(self) -> T:
        return self._itens[-1]

# Pilha de inteiros
p_int: Pilha[int] = Pilha()
p_int.empilhar(1)
p_int.empilhar(2)
print(p_int.desempilhar())  # 2

# Pilha de strings
p_str: Pilha[str] = Pilha()
p_str.empilhar("ola")
p_str.empilhar("mundo")
print(p_str.topo())  # mundo
```

### Funções genéricas

```python
from typing import TypeVar, Sequence

T = TypeVar("T")

def primeiro(sequencia: Sequence[T]) -> T:
    return sequencia[0]

print(primeiro([1, 2, 3]))       # 1
print(primeiro(["a", "b", "c"])) # a
```

### Benefícios dos Generics

| Benefício | Descrição |
|---|---|
| Reuso | Uma implementação para qualquer tipo |
| Segurança | Erros de tipo detectados antes de rodar |
| Documentação | O tipo comunica a intenção da classe |
""",
            "exercise": {
                "question": "Qual o principal benefício de usar Generics em vez de usar o tipo `object` (ou nenhum tipo)?",
                "options": [
                    "Generics fazem o código rodar mais rápido em tempo de execução.",
                    "Generics permitem reutilizar a implementação para qualquer tipo com segurança — ferramentas detectam inconsistências antes de rodar o código.",
                    "Generics eliminam a necessidade de testes unitários.",
                    "Generics só funcionam com tipos primitivos como int e str.",
                ],
                "correct": 1,
                "explanation": "Correto! Generics combinam reuso (mesma implementação para qualquer tipo) com segurança (erros detectados estaticamente pelo type checker).",
            },
        },
        {
            "id": "3-5",
            "title": "Design Patterns",
            "icon": "🗺️",
            "theory": """
## Design Patterns

**Design Patterns** (Padrões de Projeto) são soluções consagradas para problemas recorrentes em design de software. Foram catalogados por Erich Gamma et al. no livro "Design Patterns" (Gang of Four).

Não são código pronto — são **modelos de solução** adaptáveis ao contexto.

### As 3 categorias

| Categoria | Foco | Exemplos |
|---|---|---|
| **Criacionais** | Como objetos são criados | Factory, Singleton, Builder |
| **Estruturais** | Como classes se organizam | Adapter, Decorator, Facade |
| **Comportamentais** | Como objetos se comunicam | Strategy, Observer, Command |

---

### Strategy — comportamento intercambiável

```python
from abc import ABC, abstractmethod

class EstrategiaOrdenacao(ABC):
    @abstractmethod
    def ordenar(self, dados: list) -> list: pass

class BubbleSort(EstrategiaOrdenacao):
    def ordenar(self, dados):
        d = dados[:]
        for i in range(len(d)):
            for j in range(len(d) - i - 1):
                if d[j] > d[j+1]:
                    d[j], d[j+1] = d[j+1], d[j]
        return d

class PythonSort(EstrategiaOrdenacao):
    def ordenar(self, dados):
        return sorted(dados)

class Processador:
    def __init__(self, estrategia: EstrategiaOrdenacao):
        self._estrategia = estrategia

    def processar(self, dados):
        return self._estrategia.ordenar(dados)

p = Processador(PythonSort())
print(p.processar([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
```

---

### Observer — notificação de eventos

```python
class EventoEstoque:
    def __init__(self):
        self._observadores = []

    def assinar(self, obs):
        self._observadores.append(obs)

    def notificar(self, produto, quantidade):
        for obs in self._observadores:
            obs.atualizar(produto, quantidade)

class AlertaEmail:
    def atualizar(self, produto, qtd):
        print(f"📧 Email: {produto} — restam {qtd} unidades.")

class AlertaSMS:
    def atualizar(self, produto, qtd):
        print(f"📱 SMS: Estoque baixo de {produto}!")

evento = EventoEstoque()
evento.assinar(AlertaEmail())
evento.assinar(AlertaSMS())
evento.notificar("Caneta", 3)
```

---

### Factory — criação centralizada

```python
class ConexaoBanco(ABC):
    @abstractmethod
    def conectar(self): pass

class MySQL(ConexaoBanco):
    def conectar(self): return "Conectado ao MySQL"

class PostgreSQL(ConexaoBanco):
    def conectar(self): return "Conectado ao PostgreSQL"

def fabrica_banco(tipo: str) -> ConexaoBanco:
    bancos = {"mysql": MySQL, "postgres": PostgreSQL}
    return bancos[tipo]()

db = fabrica_banco("postgres")
print(db.conectar())
```
""",
            "exercise": {
                "question": "O padrão **Strategy** é mais adequado quando:",
                "options": [
                    "Você precisa garantir que uma classe tenha apenas uma instância no sistema.",
                    "Você quer poder trocar o algoritmo ou comportamento de um objeto em tempo de execução sem alterar o código que o usa.",
                    "Você precisa notificar múltiplos objetos quando o estado de outro muda.",
                    "Você quer criar objetos complexos passo a passo.",
                ],
                "correct": 1,
                "explanation": "Correto! Strategy encapsula algoritmos intercambiáveis — o objeto que os usa não precisa saber qual estratégia está ativa, apenas chamá-la.",
            },
        },
        {
            "id": "3-6",
            "title": "Resumo",
            "icon": "📋",
            "theory": """
## Resumo — O arquiteto mestre

Parabéns! Você concluiu a trilha completa de Orientação a Objetos.

### O que você domina agora

| Módulo | Conquista |
|---|---|
| **Fundamentos** | Criar classes, objetos, métodos e construtores |
| **Pilares** | Aplicar abstração, encapsulamento, herança e polimorfismo |
| **Relações** | Modelar sistemas com sobrescrita, contratos e relacionamentos |
| **Arquitetura** | Projetar com coesão, baixo acoplamento, SOLID, generics e patterns |

### O checklist do arquiteto

Ao projetar uma classe, pergunte-se:

- [ ] **Coesão** — esta classe tem um propósito único?
- [ ] **Acoplamento** — ela depende de abstrações, não de implementações?
- [ ] **SRP** — há apenas uma razão para ela mudar?
- [ ] **OCP** — posso estendê-la sem modificar o código existente?
- [ ] **LSP** — as subclasses respeitam o contrato da superclasse?
- [ ] **ISP** — as interfaces são específicas o suficiente?
- [ ] **DIP** — as dependências são injetadas, não criadas internamente?

### O caminho não para aqui

Design de software é uma habilidade que se aprofunda com prática. Os próximos passos naturais são:

- **Clean Architecture** — organização de sistemas em camadas
- **Domain-Driven Design** — modelagem centrada no domínio do negócio
- **Test-Driven Development** — design guiado por testes

> *"Qualquer tolo pode escrever código que um computador entende. Bons programadores escrevem código que humanos entendem."* — Martin Fowler
""",
            "exercise": {
                "question": "Qual combinação representa o objetivo central do módulo de arquitetura?",
                "options": [
                    "Máximo de classes possível + mínimo de métodos por classe.",
                    "Alta coesão + baixo acoplamento + princípios SOLID.",
                    "Usar todos os design patterns disponíveis em cada projeto.",
                    "Evitar generics e abstrações para manter o código simples.",
                ],
                "correct": 1,
                "explanation": "Exato! Alta coesão (propósito único por classe) + baixo acoplamento (dependências via abstração) + SOLID é a fórmula do design orientado a objetos de qualidade.",
            },
        },
    ],
}
