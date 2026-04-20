MODULO_3 = {
    "id": 2,
    "title": "Módulo 3 — A sociedade dos objetos",
    "short": "Relações",
    "sections": [
        {
            "id": "2-0",
            "title": "Introdução ao módulo",
            "icon": "🏙️",
            "theory": """
## A sociedade dos objetos — Mecânica e Relações

Nos módulos anteriores você aprendeu a criar objetos e a aplicar os 4 pilares. Agora vamos explorar como objetos **interagem entre si**.

Em sistemas reais, objetos raramente vivem isolados. Eles se comunicam, dependem uns dos outros e formam estruturas complexas — como uma sociedade.

### O que você vai aprender

| Conceito | O que é |
|---|---|
| **Sobrescrita** | Redefinir o comportamento de um método herdado |
| **Sobrecarga** | Adaptar um método para diferentes formas de chamada |
| **Contratos** | Interfaces e classes abstratas como acordos entre objetos |
| **Associação** | Um objeto *usa* outro |
| **Agregação** | Um objeto *tem* outro (relação fraca) |
| **Composição** | Um objeto *é composto de* outro (relação forte) |

### A analogia da sociedade

Pense em objetos como pessoas em uma cidade:
- Uma pessoa pode **sobrescrever** um hábito herdado da família
- Assinar um **contrato** a obriga a cumprir certas responsabilidades
- Ela pode **usar** um táxi (associação), **ter** um carro (agregação) ou **ter** um coração (composição)

> Entender relações é o que separa código amador de código profissional.
""",
            "exercise": {
                "question": "Por que é importante entender como objetos se relacionam em POO?",
                "options": [
                    "Porque objetos isolados são mais eficientes computacionalmente.",
                    "Porque sistemas reais são formados por objetos que colaboram — entender relações é essencial para modelar o mundo real.",
                    "Porque o Python exige que todos os objetos estejam conectados entre si.",
                    "Porque relações entre objetos substituem a necessidade de herança.",
                ],
                "correct": 1,
                "explanation": "Exato! Sistemas reais são redes de objetos colaborando. Modelar essas relações corretamente é o que torna um design robusto e manutenível.",
            },
        },
        {
            "id": "2-1",
            "title": "Sobrescrita",
            "icon": "✏️",
            "theory": """
## Sobrescrita (Override)

**Sobrescrita** ocorre quando uma subclasse redefine um método da superclasse com a mesma assinatura, substituindo o comportamento original.

```python
class Notificacao:
    def enviar(self, mensagem):
        return f"Enviando: {mensagem}"

class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem):          # sobrescreve
        return f"📧 Email: {mensagem}"

class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem):          # sobrescreve
        return f"📱 SMS: {mensagem}"

class NotificacaoPush(Notificacao):
    def enviar(self, mensagem):          # sobrescreve
        return f"🔔 Push: {mensagem}"

canais = [NotificacaoEmail(), NotificacaoSMS(), NotificacaoPush()]
for canal in canais:
    print(canal.enviar("Sua compra foi aprovada!"))
```

### Estendendo com `super()`

Você pode sobrescrever **e ainda aproveitar** o comportamento original:

```python
class NotificacaoAuditada(Notificacao):
    def enviar(self, mensagem):
        resultado = super().enviar(mensagem)  # chama o original
        print(f"[LOG] Notificação registrada.")
        return resultado
```

### Regras da sobrescrita

| Regra | Descrição |
|---|---|
| Mesmo nome | O método na subclasse deve ter o mesmo nome |
| `super()` opcional | Use para aproveitar o comportamento pai |
| Polimorfismo | Objetos distintos se comportam diferente pelo mesmo método |
""",
            "exercise": {
                "question": "Qual é a diferença entre sobrescrita e herança simples?",
                "options": [
                    "Não há diferença — sobrescrita é apenas outro nome para herança.",
                    "Herança passa atributos e métodos para a subclasse; sobrescrita redefine um método herdado com novo comportamento.",
                    "Sobrescrita elimina todos os métodos herdados da superclasse.",
                    "Herança só funciona com `super()`, enquanto sobrescrita não precisa.",
                ],
                "correct": 1,
                "explanation": "Correto! Herança é o mecanismo de transmissão. Sobrescrita é a decisão da subclasse de redefinir um comportamento específico que herdou.",
            },
        },
        {
            "id": "2-2",
            "title": "Sobrecarga",
            "icon": "🔀",
            "theory": """
## Sobrecarga (Overload)

**Sobrecarga** é a capacidade de um método aceitar diferentes conjuntos de argumentos. Em linguagens como Java e C++, isso é feito criando múltiplos métodos com o mesmo nome mas assinaturas diferentes.

Python não suporta sobrecarga tradicional — mas oferece mecanismos equivalentes e mais flexíveis.

### Abordagem 1 — Parâmetros com valor padrão

```python
class Calculadora:
    def somar(self, a, b, c=0):
        return a + b + c

calc = Calculadora()
print(calc.somar(2, 3))     # 5
print(calc.somar(2, 3, 4))  # 9
```

### Abordagem 2 — `*args` e `**kwargs`

```python
class Relatorio:
    def gerar(self, *titulos, formato="txt"):
        conteudo = " | ".join(titulos)
        return f"[{formato.upper()}] {conteudo}"

r = Relatorio()
print(r.gerar("Vendas"))                        # [TXT] Vendas
print(r.gerar("Vendas", "Estoque", formato="pdf"))  # [PDF] Vendas | Estoque
```

### Abordagem 3 — `@singledispatch` (sobrecarga por tipo)

```python
from functools import singledispatch

@singledispatch
def processar(dado):
    return f"Tipo desconhecido: {dado}"

@processar.register(int)
def _(dado):
    return f"Inteiro: {dado * 2}"

@processar.register(str)
def _(dado):
    return f"Texto: {dado.upper()}"

print(processar(5))       # Inteiro: 10
print(processar("ola"))   # Texto: OLA
```
""",
            "exercise": {
                "question": "Como Python simula sobrecarga de métodos de forma nativa?",
                "options": [
                    "Criando múltiplos métodos com o mesmo nome e assinaturas diferentes, como em Java.",
                    "Usando parâmetros com valor padrão, `*args`, `**kwargs` ou `@singledispatch`.",
                    "Python não suporta nenhuma forma de sobrecarga ou alternativa equivalente.",
                    "Usando herança múltipla para definir variações do mesmo método.",
                ],
                "correct": 1,
                "explanation": "Correto! Python usa parâmetros opcionais e empacotamento de argumentos como alternativa flexível à sobrecarga tradicional.",
            },
        },
        {
            "id": "2-3",
            "title": "Os Contratos",
            "icon": "📜",
            "theory": """
## Os Contratos

Em POO, um **contrato** é um acordo formal que define o que uma classe *deve* fazer — sem ditar *como* ela faz.

Quando uma classe assina um contrato, ela se compromete a implementar um conjunto de métodos. Isso garante que qualquer objeto que respeite o contrato possa ser usado de forma intercambiável.

### Por que contratos existem?

Imagine que você está construindo um sistema de pagamentos. Você quer aceitar Pix, cartão de crédito e boleto. Sem um contrato:

```python
# Sem contrato — caótico
class PagamentoPix:
    def pagar_pix(self, valor): ...

class PagamentoCartao:
    def processar_cartao(self, valor): ...

class PagamentoBoleto:
    def emitir_boleto(self, valor): ...
```

Cada classe tem um método diferente — impossível tratá-las uniformemente.

### Com um contrato

```python
from abc import ABC, abstractmethod

class MetodoPagamento(ABC):  # o contrato
    @abstractmethod
    def pagar(self, valor: float) -> str:
        pass

class Pix(MetodoPagamento):
    def pagar(self, valor):
        return f"✅ Pix de R${valor:.2f} enviado."

class Cartao(MetodoPagamento):
    def pagar(self, valor):
        return f"💳 Cartão cobrado: R${valor:.2f}."

class Boleto(MetodoPagamento):
    def pagar(self, valor):
        return f"📄 Boleto de R${valor:.2f} gerado."

def processar_pedido(metodo: MetodoPagamento, valor: float):
    return metodo.pagar(valor)  # funciona com qualquer método

print(processar_pedido(Pix(), 150.00))
print(processar_pedido(Cartao(), 89.90))
```

Em Python, contratos são implementados com **interfaces** (via ABC sem implementação) e **classes abstratas** (via ABC com implementação parcial).
""",
            "exercise": {
                "question": "Qual é o principal benefício de usar contratos (interfaces/classes abstratas) em um sistema?",
                "options": [
                    "Aumentar o desempenho do código em tempo de execução.",
                    "Garantir que diferentes classes implementem um conjunto comum de métodos, permitindo intercambialidade.",
                    "Impedir que subclasses adicionem novos métodos além dos definidos no contrato.",
                    "Substituir completamente a necessidade de herança no sistema.",
                ],
                "correct": 1,
                "explanation": "Correto! Contratos garantem que qualquer classe que os implemente possa ser usada de forma intercambiável, tornando o sistema extensível e previsível.",
            },
        },
        {
            "id": "2-4",
            "title": "Contratos — Interfaces",
            "icon": "🔌",
            "theory": """
## Interfaces

Uma **interface** é um contrato puro — define *o quê* deve ser feito, sem implementar *como*. Em Python, simulamos interfaces com classes que herdam de `ABC` e possuem apenas métodos abstratos.

```python
from abc import ABC, abstractmethod

class Serializavel(ABC):
    @abstractmethod
    def para_dict(self) -> dict:
        pass

    @abstractmethod
    def para_json(self) -> str:
        pass

class Autenticavel(ABC):
    @abstractmethod
    def autenticar(self, senha: str) -> bool:
        pass
```

### Implementando múltiplas interfaces

Python suporta herança múltipla — uma classe pode assinar vários contratos:

```python
import json

class Usuario(Serializavel, Autenticavel):
    def __init__(self, nome, senha_hash):
        self.nome = nome
        self._senha_hash = senha_hash

    def para_dict(self):
        return {"nome": self.nome}

    def para_json(self):
        return json.dumps(self.para_dict())

    def autenticar(self, senha):
        return hash(senha) == self._senha_hash

u = Usuario("Ana", hash("1234"))
print(u.para_json())           # {"nome": "Ana"}
print(u.autenticar("1234"))    # True
print(u.autenticar("errada"))  # False
```

### Interface vs Classe Abstrata

| | Interface (pura) | Classe Abstrata |
|---|---|---|
| Implementação | Nenhuma | Pode ter parcial |
| Propósito | Definir capacidades | Definir base comum |
| Herança | Múltipla (recomendada) | Geralmente única |
""",
            "exercise": {
                "question": "O que caracteriza uma interface pura em Python?",
                "options": [
                    "Uma classe com pelo menos um método implementado e um abstrato.",
                    "Uma classe que herda de `ABC` e contém apenas métodos abstratos, sem nenhuma implementação.",
                    "Uma classe que não pode ser herdada por outras classes.",
                    "Um módulo Python separado que define funções globais.",
                ],
                "correct": 1,
                "explanation": "Correto! Uma interface pura em Python é uma classe ABC com apenas @abstractmethod — ela define o contrato sem implementar nada.",
            },
        },
        {
            "id": "2-5",
            "title": "Contratos — Classes Abstratas",
            "icon": "🏛️",
            "theory": """
## Classes Abstratas

Diferente de uma interface pura, uma **classe abstrata** pode combinar métodos abstratos (sem implementação) com métodos concretos (com implementação compartilhada).

Ela define uma base comum para uma família de classes.

```python
from abc import ABC, abstractmethod

class Relatorio(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    # Métodos abstratos — cada subclasse implementa do seu jeito
    @abstractmethod
    def gerar_cabecalho(self) -> str:
        pass

    @abstractmethod
    def gerar_corpo(self, dados: list) -> str:
        pass

    # Método concreto — comportamento compartilhado por todas
    def exportar(self, dados: list) -> str:
        cab  = self.gerar_cabecalho()
        corp = self.gerar_corpo(dados)
        return f"{cab}\\n{corp}\\n--- fim do relatório ---"


class RelatorioPDF(Relatorio):
    def gerar_cabecalho(self):
        return f"[PDF] === {self.titulo} ==="

    def gerar_corpo(self, dados):
        return "\\n".join(f"• {item}" for item in dados)


class RelatorioCSV(Relatorio):
    def gerar_cabecalho(self):
        return self.titulo

    def gerar_corpo(self, dados):
        return ",".join(str(d) for d in dados)


vendas = ["Janeiro: R$10k", "Fevereiro: R$12k"]

pdf = RelatorioPDF("Relatório de Vendas")
csv = RelatorioCSV("Vendas")

print(pdf.exportar(vendas))
print(csv.exportar(vendas))
```

### Quando usar cada um?

| Situação | Use |
|---|---|
| Só precisa definir o que deve existir | Interface pura |
| Precisa de comportamento compartilhado + contrato | Classe abstrata |
| Quer combinar múltiplos contratos | Múltiplas interfaces |
""",
            "exercise": {
                "question": "Qual a principal diferença entre uma interface pura e uma classe abstrata?",
                "options": [
                    "Interfaces só existem em Java; Python só tem classes abstratas.",
                    "Interfaces definem apenas o contrato; classes abstratas podem ter métodos concretos compartilhados além dos abstratos.",
                    "Classes abstratas não podem ser herdadas, apenas instanciadas.",
                    "Interfaces permitem instanciação direta; classes abstratas não.",
                ],
                "correct": 1,
                "explanation": "Correto! Classes abstratas combinam contrato com implementação parcial compartilhada — ideal quando há comportamento comum entre as subclasses.",
            },
        },
        {
            "id": "2-6",
            "title": "Relacionamentos",
            "icon": "🔗",
            "theory": """
## Relacionamentos entre objetos

Objetos raramente existem sozinhos. Em sistemas reais, eles se conectam de formas diferentes — e cada tipo de conexão tem um nome e implicações diferentes.

### Os 3 tipos principais

| Tipo | Símbolo | Força | Analogia |
|---|---|---|---|
| **Associação** | → | Fraca | Motorista usa um carro |
| **Agregação** | ◇→ | Média | Time tem jogadores |
| **Composição** | ◆→ | Forte | Casa tem cômodos |

### A pergunta-chave: o que acontece quando o "todo" é destruído?

- **Associação** — a parte continua existindo (o carro não some se o motorista sair)
- **Agregação** — a parte continua existindo (jogadores continuam existindo sem o time)
- **Composição** — a parte é destruída junto (cômodos não existem sem a casa)

### Por que isso importa?

Modelar relações corretamente impacta:
- **Ciclo de vida** dos objetos (quem cria, quem destrói)
- **Responsabilidade** por memória e recursos
- **Flexibilidade** do design (o que pode ser trocado ou reutilizado)

> As próximas seções detalham cada tipo com exemplos práticos.
""",
            "exercise": {
                "question": "Qual pergunta central diferencia os 3 tipos de relacionamento entre objetos?",
                "options": [
                    "Quantos métodos cada objeto possui?",
                    "O que acontece com a parte quando o objeto 'todo' é destruído?",
                    "Qual objeto foi criado primeiro na memória?",
                    "Quantas classes participam do relacionamento?",
                ],
                "correct": 1,
                "explanation": "Correto! A sobrevivência da parte quando o todo é destruído é o critério que define se a relação é associação, agregação ou composição.",
            },
        },
        {
            "id": "2-7",
            "title": "Relacionamentos — Associação",
            "icon": "↔️",
            "theory": """
## Associação

**Associação** é a relação mais fraca — um objeto *usa* outro, mas nenhum depende do ciclo de vida do outro.

Os objetos existem de forma independente e a relação é temporária ou opcional.

```python
class Motorista:
    def __init__(self, nome):
        self.nome = nome

    def dirigir(self, carro):  # recebe o carro — não é dono dele
        return f"{self.nome} está dirigindo {carro.modelo}."

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

fusca  = Carro("Fusca")
gol    = Carro("Gol")
ana    = Motorista("Ana")

print(ana.dirigir(fusca))  # Ana está dirigindo Fusca.
print(ana.dirigir(gol))    # Ana está dirigindo Gol.
# fusca e gol continuam existindo independente de ana
```

### Associação bidirecional

```python
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        aluno.professor = self  # bidirecional

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

prof  = Professor("Dr. Silva")
aluno = Aluno("Bia")
prof.adicionar_aluno(aluno)

print(aluno.professor.nome)     # Dr. Silva
print(prof.alunos[0].nome)      # Bia
```

### Características da Associação

- Objetos **independentes** — um pode existir sem o outro
- Relação **temporária** ou **opcional**
- Implementada passando objetos como **parâmetros** ou referências
""",
            "exercise": {
                "question": "Qual característica define uma relação de **Associação** entre objetos?",
                "options": [
                    "Um objeto cria e destrói o outro durante seu ciclo de vida.",
                    "Os objetos se conhecem e interagem, mas existem de forma independente.",
                    "Um objeto é parte estrutural do outro e não pode existir sozinho.",
                    "Um objeto herda atributos e métodos do outro.",
                ],
                "correct": 1,
                "explanation": "Correto! Na associação, os objetos interagem mas são independentes — nenhum controla o ciclo de vida do outro.",
            },
        },
        {
            "id": "2-8",
            "title": "Relacionamentos — Agregação",
            "icon": "🧺",
            "theory": """
## Agregação

**Agregação** é uma relação "tem um" — o objeto todo **contém** partes, mas as partes **podem existir independentemente** do todo.

É uma associação com maior grau de pertencimento, mas sem controle total do ciclo de vida.

```python
class Jogador:
    def __init__(self, nome, posicao):
        self.nome    = nome
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} ({self.posicao})"

class Time:
    def __init__(self, nome):
        self.nome    = nome
        self.jogadores = []  # agrega jogadores

    def adicionar(self, jogador):
        self.jogadores.append(jogador)

    def listar(self):
        for j in self.jogadores:
            print(f"  {j}")

# Jogadores existem antes e independente do time
ana    = Jogador("Ana", "Atacante")
carlos = Jogador("Carlos", "Goleiro")

flamengo = Time("Flamengo")
flamengo.adicionar(ana)
flamengo.adicionar(carlos)

# Se o time for dissolvido, os jogadores continuam existindo
del flamengo
print(ana)  # Ana (Atacante) — ainda existe!
```

### Características da Agregação

| Característica | Valor |
|---|---|
| Relação | "tem um" |
| Ciclo de vida | Partes independentes do todo |
| Criação das partes | Fora do objeto todo |
| Destruição | Todo destruído ≠ partes destruídas |

> **Dica:** se os objetos "parte" são criados fora do "todo" e passados para ele, provavelmente é agregação.
""",
            "exercise": {
                "question": "O que diferencia Agregação de Composição?",
                "options": [
                    "Na agregação, as partes são criadas dentro do todo e destruídas junto com ele.",
                    "Na agregação, as partes existem independentemente do todo e podem ser reutilizadas por outros objetos.",
                    "Agregação usa herança, enquanto composição usa interfaces.",
                    "Não há diferença prática — são apenas nomes diferentes para o mesmo conceito.",
                ],
                "correct": 1,
                "explanation": "Correto! Na agregação, as partes têm vida própria — podem existir sem o todo e até pertencer a outros objetos ao mesmo tempo.",
            },
        },
        {
            "id": "2-9",
            "title": "Relacionamentos — Composição",
            "icon": "🧱",
            "theory": """
## Composição

**Composição** é a relação mais forte — o objeto todo **cria suas partes** e elas **não existem sem ele**. Quando o todo é destruído, as partes vão junto.

```python
class Comodo:
    def __init__(self, nome, area_m2):
        self.nome    = nome
        self.area_m2 = area_m2

    def __str__(self):
        return f"{self.nome} ({self.area_m2}m²)"

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        # Cômodos criados DENTRO da Casa — composição
        self.comodos = [
            Comodo("Sala",    30),
            Comodo("Quarto",  20),
            Comodo("Cozinha", 15),
        ]

    def area_total(self):
        return sum(c.area_m2 for c in self.comodos)

    def __str__(self):
        lista = "\\n  ".join(str(c) for c in self.comodos)
        return f"Casa em {self.endereco}:\\n  {lista}\\n  Total: {self.area_total()}m²"

minha_casa = Casa("Rua das Flores, 42")
print(minha_casa)
```

### Composição com lógica de negócio

```python
class Motor:
    def __init__(self, cilindradas):
        self.cilindradas = cilindradas
        self.ligado = False

    def ligar(self):
        self.ligado = True

class Carro:
    def __init__(self, modelo, cilindradas):
        self.modelo = modelo
        self.motor  = Motor(cilindradas)  # Motor criado dentro do Carro

    def ligar(self):
        self.motor.ligar()
        return f"{self.modelo} ligado com motor de {self.motor.cilindradas}cc."
```

### Resumo dos relacionamentos

| | Associação | Agregação | Composição |
|---|---|---|---|
| Força | Fraca | Média | Forte |
| "Parte" independente? | ✓ | ✓ | ✗ |
| Quem cria a "parte"? | Externo | Externo | O próprio todo |
| Destruição | Independente | Independente | Junto com o todo |
""",
            "exercise": {
                "question": "Em qual situação a Composição é o relacionamento mais adequado?",
                "options": [
                    "Quando dois objetos se referenciam mas existem de forma totalmente independente.",
                    "Quando as partes de um objeto não fazem sentido fora dele e são criadas e destruídas junto com o todo.",
                    "Quando um objeto pode pertencer a múltiplos objetos 'todo' simultaneamente.",
                    "Quando a relação entre objetos é temporária e baseada em parâmetros de método.",
                ],
                "correct": 1,
                "explanation": "Correto! Composição é para partes que só existem no contexto do todo — como cômodos de uma casa ou órgãos de um corpo.",
            },
        },
        {
            "id": "2-10",
            "title": "Resumo",
            "icon": "📋",
            "theory": """
## Resumo — A sociedade dos objetos

Você dominou como objetos se comportam e se relacionam em sistemas reais.

### Quadro geral

| Conceito | Em uma linha |
|---|---|
| **Sobrescrita** | Subclasse redefine método da superclasse |
| **Sobrecarga** | Método aceita diferentes formas de chamada |
| **Interface** | Contrato puro — define o quê, não o como |
| **Classe abstrata** | Contrato com implementação parcial compartilhada |
| **Associação** | Objetos se usam, mas vivem de forma independente |
| **Agregação** | "Tem um" — partes independentes do todo |
| **Composição** | "É composto de" — partes não existem sem o todo |

### Tudo junto em um sistema de e-commerce

```python
from abc import ABC, abstractmethod

class Pagamento(ABC):         # interface/contrato
    @abstractmethod
    def processar(self, valor): pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"💳 Cartão: R${valor:.2f} aprovado."

class Endereco:               # composição com Pedido
    def __init__(self, rua, cidade):
        self.rua    = rua
        self.cidade = cidade

class Produto:                # agregação com Pedido
    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

class Pedido:
    def __init__(self, rua, cidade):
        self.endereco = Endereco(rua, cidade)  # composição
        self.itens    = []                     # agregação

    def adicionar(self, produto):
        self.itens.append(produto)

    def total(self):
        return sum(p.preco for p in self.itens)

    def finalizar(self, pagamento: Pagamento):  # associação
        return pagamento.processar(self.total())

caneta  = Produto("Caneta", 2.50)
caderno = Produto("Caderno", 15.00)

pedido = Pedido("Rua A", "SP")
pedido.adicionar(caneta)
pedido.adicionar(caderno)

print(pedido.finalizar(CartaoCredito()))
```

> Próximo módulo: **engenharia e qualidade** — como escrever código que dura.
""",
            "exercise": {
                "question": "Em um sistema de biblioteca, livros existem antes e independente de uma coleção, e podem pertencer a várias coleções. Qual relacionamento modela isso?",
                "options": [
                    "Composição, porque os livros fazem parte da coleção.",
                    "Associação, porque livros e coleções não têm nenhuma relação.",
                    "Agregação, porque os livros existem independentemente e podem pertencer a mais de uma coleção.",
                    "Herança, porque Livro herda comportamentos de Coleção.",
                ],
                "correct": 2,
                "explanation": "Correto! Livros existem independentemente e podem ser parte de múltiplas coleções — isso é agregação: relação 'tem um' sem controle do ciclo de vida.",
            },
        },
    ],
}
