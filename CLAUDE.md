# Abstractio — CLAUDE.md

App educacional gamificado para ensinar POO em Python, construído com Streamlit.

## Regras de colaboração

- **Nunca realizar mudanças ou implementações sem confirmação prévia da Rebecca.** Apresente a proposta, aguarde aprovação, só então execute.

## Convenções de git

- Mensagens de commit sempre em **Português do Brasil**
- Usar **Conventional Commits** em pt-BR: `tipo: descrição curta` (ex: `feat: adicionar missão de herança`)
- Tipos aceitos: `feat`, `fix`, `refactor`, `style`, `docs`, `chore`
- Quando houver múltiplas mudanças relevantes, incluir corpo com bullet points em pt-BR
- **Ao finalizar qualquer implementação**, perguntar à Rebecca se deseja que o commit seja feito antes de encerrar

## Como rodar

```bash
python -m streamlit run app.py
```

> Sempre que a Rebecca disser "rodar" (ou "roda", "rode", "vamos rodar"), execute automaticamente o comando acima via Bash.

## Estrutura do projeto

```
app.py                  # único arquivo da UI (Streamlit)
styles.css              # todo o CSS global da aplicação
curriculum/
  __init__.py           # exporta CURRICULUM, get_flat_missoes, get_total_missoes
  nivel_1/
    __init__.py         # define NIVEL (dict com metadata + lista de missões)
    missao_1.py         # MISSAO dict + render_interativo() opcional
    missao_2.py
    ...                 # (6 missões no total)
  nivel_2/              # (6 missões)
  nivel_3/              # (11 missões)
  nivel_4/              # (7 missões)
```

## Nomenclatura (importante)

O currículo usa os termos:
- **Nível** — o que seria "módulo" em outras plataformas
- **Missão** — o que seria "seção/aula" em outras plataformas

Isso se reflete nos nomes de variáveis e chaves de dicionário por todo o código.

## Estrutura de um Nível

```python
NIVEL_N = {
    "id": int,
    "title": "Nível N — Nome",
    "short": "NomeCurto",   # usado na progress bar
    "missoes": [
        {
            "id": "nv-ms",  # ex: "0-0"
            "title": str,
            "icon": str,    # emoji (ainda não renderizado na UI)
            "theory": str,  # Markdown
            "exercise": {
                "question": str,
                "options": [str, ...],
                "correct": int,         # índice da opção correta
                "explanation": str,
            },
        },
        ...
    ],
}
```

## Chaves de session_state relevantes

| Chave | Tipo | Significado |
|---|---|---|
| `nivel_idx` | int | Índice do nível atual no currículo |
| `missao_idx` | int | Índice da missão atual no nível |
| `completed` | set | Strings `"nv-ms"` das missões concluídas |
| `niveis_concluidos` | set | Índices dos níveis 100% completos |
| `pontuacao` | int | Pontos totais do usuário |
| `nivel_nome` | str | Nome do nível de gamificação (Polvinho → Kraken) |
| `nivel_nome_idx` | int | Índice do nome atual em `NIVEL_NOMES` |

> `nivel_nome`/`nivel_nome_idx` são o sistema de gamificação. Não confundir com `nivel_idx`, que é a posição no currículo.

## Screens (rotas internas)

- `"dashboard"` — tela inicial com hero e cards
- `"trilha"` — lista de todos os níveis e missões
- `"missao"` — conteúdo de uma missão (teoria + exercício)

## Estrutura de um arquivo de missão (`missao_N.py`)

```python
# render_interativo é opcional — só existe em missões com mini-jogo
def render_interativo():
    import streamlit.components.v1 as components
    components.html(_HTML, height=480, scrolling=False)

_HTML = """..."""  # HTML/CSS/JS do mini-jogo (string longa)

MISSAO = {
    "id": "nv-ms",              # ex: "0-0" (nivel-missao, base 0)
    "title": str,
    "icon": str,                # emoji
    "theory": str,              # Markdown exibido antes do exercício
    "exercise": {
        "question": str,
        "options": [str, ...],
        "correct": int,         # índice da opção correta
        "explanation": str,
    },
    "render_interativo": render_interativo,  # omitir se não houver mini-jogo
}
```

## Fluxo para criar uma missão nova

1. Criar `curriculum/nivel_N/missao_M.py` seguindo a estrutura acima.
2. Importar no `curriculum/nivel_N/__init__.py` e adicionar à lista `"missoes"`.
3. Nenhuma outra alteração é necessária — `curriculum/__init__.py` e `app.py` consomem tudo dinamicamente.

## Pontuação e ranks

- +15 pts por missão concluída
- Completar um nível inteiro sobe o rank
- Nomes de nível (`NIVEL_NOMES`): Polvinho → Explorador → Mestre dos Mares → Kraken
- Emblemas desbloqueados em 50 / 100 / 150 / 200 pts
