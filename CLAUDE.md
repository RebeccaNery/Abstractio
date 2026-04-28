# Abstractio — CLAUDE.md

App educacional gamificado para ensinar POO em Python, construído com Streamlit.

## Convenções de git

- Mensagens de commit sempre em **Português do Brasil**

## Como rodar

```bash
python -m streamlit run app.py
```

## Estrutura do projeto

```
app.py                  # único arquivo da UI (Streamlit)
curriculum/
  __init__.py           # exporta CURRICULUM, get_flat_missoes, get_total_missoes
  modulo_1.py           # NIVEL_1 — Fundamentos (6 missões)
  modulo_2.py           # NIVEL_2 — As leis do mundo / Pilares (6 missões)
  modulo_3.py           # NIVEL_3 — A sociedade dos objetos (11 missões)
  modulo_4.py           # NIVEL_4 — O arquiteto mestre (7 missões)
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
| `rank` | str | Rank de gamificação (Iniciante → Sênior) |
| `rank_idx` | int | Índice do rank atual em `RANKS` |

> `rank`/`rank_idx` são o sistema de gamificação. Não confundir com `nivel_idx`, que é a posição no currículo.

## Screens (rotas internas)

- `"dashboard"` — tela inicial com hero e cards
- `"trilha"` — lista de todos os níveis e missões
- `"missao"` — conteúdo de uma missão (teoria + exercício)

## Reestruturação planejada (próximo passo)

Migrar de 1 arquivo por nível para **1 arquivo por missão** em subdiretórios:

```
curriculum/
  nivel_1/
    __init__.py     # metadata do nível
    missao_1.py     # theory + exercise + render_interativo()
    missao_2.py
    ...
```

Motivação: cada missão receberá componentes interativos com imports próprios (bibliotecas externas, mini-jogos). Manter tudo num arquivo por nível ficaria pesado.

## Pontuação e ranks

- +15 pts por missão concluída
- Completar um nível inteiro sobe o rank
- Ranks: Iniciante → Estagiário → Júnior → Pleno → Sênior
- Emblemas desbloqueados em 50 / 100 / 150 / 200 pts
