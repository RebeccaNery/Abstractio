import streamlit as st
from curriculum import CURRICULUM, get_flat_missoes, get_total_missoes

st.set_page_config(
    page_title="Abstractio — POO Gamificado",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════════════════════

with open("styles.css") as _f:
    st.markdown(f"<style>{_f.read()}</style>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════════════════════

RANKS = ["Iniciante", "Estagiário", "Júnior", "Pleno", "Sênior"]

EMBLEMAS_MAP = {
    50:  "Encapsuladora Iniciante",
    100: "Mestre da Herança",
    150: "Rainha da Abstração",
    200: "Polimorfista Suprema",
}

# ══════════════════════════════════════════════════════════════
#  SESSION STATE INIT
# ══════════════════════════════════════════════════════════════

def _init():
    defaults = {
        "screen":              "dashboard",
        "nivel_idx":           0,   # índice do nível no currículo
        "missao_idx":          0,
        "pontuacao":           10,
        "rank":                "Iniciante",
        "rank_idx":            0,
        "completed":           set(),   # set of "nv-ms" strings
        "niveis_concluidos":   set(),   # set of nivel indices
        "emblemas":            [],
        "first_visit":         True,
        # per-missao exercise state (keyed so navigating resets it)
        "ex_key":              "",      # current missao id
        "ex_submitted":        False,
        "ex_correct":          False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init()

# Show welcome toast once
if st.session_state.first_visit:
    st.toast("Parabéns por iniciar sua jornada!", icon=":material/celebration:")
    st.session_state.first_visit = False

# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════

def go(screen, nivel_idx=None, missao_idx=None):
    st.session_state.screen = screen
    if nivel_idx is not None:
        st.session_state.nivel_idx = nivel_idx
    if missao_idx is not None:
        st.session_state.missao_idx = missao_idx
    st.rerun()


def missao_key(nv, ms):
    return f"{nv}-{ms}"


def is_done(nv, ms):
    return missao_key(nv, ms) in st.session_state.completed


def reset_exercise(nv, ms):
    key = missao_key(nv, ms)
    if st.session_state.ex_key != key:
        st.session_state.ex_key = key
        st.session_state.ex_submitted = False
        st.session_state.ex_correct = is_done(nv, ms)  # already done → mark correct


def _award_points(n):
    old = st.session_state.pontuacao
    st.session_state.pontuacao += n
    new = st.session_state.pontuacao
    for threshold, badge in EMBLEMAS_MAP.items():
        if old < threshold <= new and badge not in st.session_state.emblemas:
            st.session_state.emblemas.append(badge)
            st.toast(f"Emblema desbloqueado: {badge}!", icon=":material/military_tech:")


def complete_missao(nv, ms):
    key = missao_key(nv, ms)
    if key not in st.session_state.completed:
        st.session_state.completed = st.session_state.completed | {key}
        st.session_state.ex_correct = True
        _award_points(15)
        st.toast("+15 pontos! Continue assim!", icon=":material/star:")
        nivel = CURRICULUM[nv]
        needed = {missao_key(nv, i) for i in range(len(nivel["missoes"]))}
        if needed.issubset(st.session_state.completed) and nv not in st.session_state.niveis_concluidos:
            st.session_state.niveis_concluidos = st.session_state.niveis_concluidos | {nv}
            _rank_up()


def _rank_up():
    idx = st.session_state.rank_idx
    if idx < len(RANKS) - 1:
        st.session_state.rank_idx += 1
        st.session_state.rank = RANKS[st.session_state.rank_idx]
        st.toast(f"Você evoluiu para **{st.session_state.rank}**!", icon=":material/trending_up:")


def navigate_next():
    nv = st.session_state.nivel_idx
    ms = st.session_state.missao_idx
    nivel = CURRICULUM[nv]
    if ms + 1 < len(nivel["missoes"]):
        go("missao", nv, ms + 1)
    elif nv + 1 < len(CURRICULUM):
        go("missao", nv + 1, 0)
    else:
        go("trilha")


# ══════════════════════════════════════════════════════════════
#  PROGRESS BAR
# ══════════════════════════════════════════════════════════════

def render_progress_bar():
    flat = get_flat_missoes()
    total = len(flat)
    done_count = len(st.session_state.completed)
    pct = int(done_count / total * 100) if total else 0

    circles = ""
    prev_nv = None

    for idx, (nv_idx, ms_idx, missao) in enumerate(flat):
        # Nível separator
        if prev_nv is not None and nv_idx != prev_nv:
            nv_label = CURRICULUM[nv_idx]["short"]
            circles += (
                f'<div class="pb-separator">'
                f'  <div class="pb-sep-label">{nv_label}</div>'
                f'  <div class="pb-sep-line"></div>'
                f'</div>'
            )
        elif prev_nv is None:
            # First nivel label
            nv_label = CURRICULUM[nv_idx]["short"]
            circles += (
                f'<div class="pb-separator" style="margin-left:0;margin-right:6px">'
                f'  <div class="pb-sep-label">{nv_label}</div>'
                f'  <div class="pb-sep-line"></div>'
                f'</div>'
            )

        # Connector before dot (not first in nivel)
        if prev_nv == nv_idx:
            conn_cls = "pb-connector done" if is_done(nv_idx, ms_idx) else "pb-connector"
            circles += f'<div class="{conn_cls}"></div>'

        # Dot
        is_active = (
            st.session_state.screen == "missao"
            and nv_idx == st.session_state.nivel_idx
            and ms_idx == st.session_state.missao_idx
        )
        if is_active:
            dot_cls = "pb-dot active"
        elif is_done(nv_idx, ms_idx):
            dot_cls = "pb-dot done"
        else:
            dot_cls = "pb-dot"

        circles += f'<div class="{dot_cls}" title="{missao["title"]}"></div>'
        prev_nv = nv_idx

    html = f"""
    <div class="pb-wrap">
      <div class="pb-header">
        <span class="pb-title">Progresso da Trilha</span>
        <span class="pb-percent">{done_count}/{total} missões &nbsp;·&nbsp; {pct}%</span>
      </div>
      <div class="pb-track">{circles}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════

def render_sidebar():
    with st.sidebar:
        st.markdown("## Abstractio")
        st.caption("Aprenda POO na prática!")
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Pontos", st.session_state.pontuacao)
        with col2:
            st.metric("Nível", st.session_state.rank)

        st.divider()

        if st.button("Dashboard", icon=":material/home:", use_container_width=True,
                     type="primary" if st.session_state.screen == "dashboard" else "secondary"):
            go("dashboard")

        if st.button("Trilha POO", icon=":material/map:", use_container_width=True,
                     type="primary" if st.session_state.screen == "trilha" else "secondary"):
            go("trilha")

        if st.session_state.emblemas:
            st.divider()
            st.markdown("**Emblemas**")
            for badge in st.session_state.emblemas:
                st.markdown(f'<span class="badge">{badge}</span>', unsafe_allow_html=True)


render_sidebar()

# ══════════════════════════════════════════════════════════════
#  DIALOG — skip confirmation
# ══════════════════════════════════════════════════════════════

@st.dialog("Missão não concluída")
def skip_dialog():
    st.markdown(
        "Tem certeza que quer prosseguir? "
        "Você ainda não concluiu o exercício da missão atual."
    )
    st.markdown("Você pode voltar a qualquer momento para completá-lo.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sim, prosseguir", icon=":material/check:", type="primary", use_container_width=True):
            navigate_next()
    with col2:
        if st.button("Cancelar", icon=":material/arrow_back:", use_container_width=True):
            st.rerun()


# ══════════════════════════════════════════════════════════════
#  SCREEN: DASHBOARD
# ══════════════════════════════════════════════════════════════

def screen_dashboard():
    render_progress_bar()

    # Hero
    st.markdown("""
    <div class="hero">
      <div class="hero-title">Bem-vindo ao Abstractio</div>
      <div class="hero-sub">
        Aprenda os conceitos abstratos da Ciência da Computação na prática,
        com lições interativas e jogos em cada nível.
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_btn, _, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("Comece já", icon=":material/rocket_launch:", type="primary", use_container_width=True):
            go("trilha")

    st.markdown("---")
    st.markdown("### Destaques")

    c1, c2, c3 = st.columns(3)
    cards = [
        ("adjust", "Orientação a Objetos",
         "Classes, herança e polimorfismo para criar código como um profissional.", False),
        ("database", "Estruturas de Dados",
         "Do array ao grafo, domine como organizar dados de forma eficiente.", True),
        ("push_pin", "Ponteiros",
         "Domine boas ordenações e eficiência computacional com exemplos reais.", True),
    ]
    for col, (icon, title, desc, muted) in zip([c1, c2, c3], cards):
        with col:
            css_class = "feat-card feat-card--muted" if muted else "feat-card"
            st.markdown(
                f'<div class="{css_class}">'
                f'  <div class="feat-icon"><span class="material-symbols-rounded">{icon}</span></div>'
                f'  <div class="feat-title">{title}</div>'
                f'  <div class="feat-desc">{desc}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
            if not muted:
                st.write("")
                if st.button("Explorar", icon=":material/arrow_forward:", key="hero_explore", type="primary"):
                    go("trilha")
            else:
                st.markdown('<p style="color:#555570;font-size:0.75rem;margin-top:0.5rem;">em breve</p>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  SCREEN: TRILHA
# ══════════════════════════════════════════════════════════════

def screen_trilha():
    render_progress_bar()

    st.markdown("## Programação Orientada a Objetos")

    st.info(
        "Você irá aprender todos os conceitos fundamentais de POO — classes, objetos, "
        "encapsulamento, herança e polimorfismo — com exemplos práticos e exercícios reais.",
    )
    st.markdown("---")

    for nv_idx, nivel in enumerate(CURRICULUM):
        total_ms = len(nivel["missoes"])
        done_ms = sum(1 for ms_idx in range(total_ms) if is_done(nv_idx, ms_idx))
        pts_total = total_ms * 15

        st.markdown(
            f'<div class="module-header">'
            f'  <span class="module-title">{nivel["title"]}</span>'
            f'  <span class="module-pts">{done_ms}/{total_ms} missões &nbsp;·&nbsp; {pts_total} pts</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

        for ms_idx, missao in enumerate(nivel["missoes"]):
            done = is_done(nv_idx, ms_idx)
            status_icon = '<span class="material-symbols-rounded" style="color:#10b981;font-size:1rem;">check_circle</span>' if done else '<span class="material-symbols-rounded" style="color:#4b5563;font-size:1rem;">radio_button_unchecked</span>'
            col_sec, col_btn = st.columns([5, 1])
            with col_sec:
                st.markdown(
                    f'<div class="section-row {"done" if done else ""}">'
                    f'  <span class="section-status">{status_icon}</span>'
                    f'  <span class="section-name">{missao["title"]}</span>'
                    f'  <span class="section-pts">+15 pts</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            with col_btn:
                btn_label = "Rever" if done else "Iniciar"
                btn_icon = ":material/replay:" if done else ":material/play_arrow:"
                if st.button(btn_label, icon=btn_icon, key=f"trl_{nv_idx}_{ms_idx}",
                             type="primary" if not done else "secondary"):
                    go("missao", nv_idx, ms_idx)

        st.markdown("")

    # Pre-requisites note
    st.caption("Pré-requisitos: Nenhum pré-requisito obrigatório. Ter noções básicas de lógica de programação é recomendado.")


# ══════════════════════════════════════════════════════════════
#  SCREEN: MISSÃO
# ══════════════════════════════════════════════════════════════

def screen_missao():
    nv = st.session_state.nivel_idx
    ms = st.session_state.missao_idx
    nivel = CURRICULUM[nv]
    missao = nivel["missoes"][ms]
    is_last_in_nivel = (ms == len(nivel["missoes"]) - 1)
    is_last_nivel = (nv == len(CURRICULUM) - 1)

    reset_exercise(nv, ms)

    render_progress_bar()

    # Breadcrumb
    col_bc, col_nav = st.columns([4, 1])
    with col_bc:
        st.caption(f"{nivel['title']} › {missao['title']}")
    with col_nav:
        if st.button("Trilha", icon=":material/arrow_back:", key="back_to_trilha"):
            go("trilha")

    st.markdown(f"# {missao['title']}")

    # ── Theory ──────────────────────────────────────────────
    st.markdown(missao["theory"])

    # ── Interactive placeholder ──────────────────────────────
    st.info("**Interação Visual / Jogo** — `# TODO`: mini-jogo interativo para esta missão será implementado aqui.")

    st.markdown("---")

    # ── Exercise ─────────────────────────────────────────────
    ex = missao["exercise"]
    st.markdown(
        f'<div class="exercise-header">'
        f'<span class="exercise-tag">Exercício Prático</span>'
        f'</div>'
        f'<div class="exercise-question">{ex["question"]}</div>',
        unsafe_allow_html=True,
    )

    selected = st.radio(
        "Escolha sua resposta:",
        options=list(range(len(ex["options"]))),
        format_func=lambda i: ex["options"][i],
        key=f"radio_{missao['id']}",
        index=None if not st.session_state.ex_correct else ex["correct"],
        label_visibility="collapsed",
    )

    col_test, _ = st.columns([1, 3])

    with col_test:
        test_disabled = st.session_state.ex_correct
        if st.button("Testar", icon=":material/science:", key=f"test_{missao['id']}",
                     disabled=test_disabled, use_container_width=True):
            if selected is None:
                st.warning("Selecione uma alternativa antes de testar.")
            else:
                st.session_state.ex_submitted = True
                if selected == ex["correct"]:
                    complete_missao(nv, ms)
                    st.rerun()

    # Feedback
    if st.session_state.ex_submitted and not st.session_state.ex_correct:
        st.error("Resposta incorreta. Revise o conteúdo e tente novamente!")

    if st.session_state.ex_correct:
        st.success(ex['explanation'])

    st.markdown("---")

    # ── Nivel completion banner ───────────────────────────────
    nivel_completo = nv in st.session_state.niveis_concluidos

    if is_last_in_nivel and nivel_completo:
        st.markdown(
            f'<div class="completion-banner">'
            f'  <h2>Nível concluído!</h2>'
            f'  <p>Você completou <strong>{nivel["title"]}</strong> e avançou para '
            f'  o rank <strong>{st.session_state.rank}</strong>!</p>'
            f'</div>',
            unsafe_allow_html=True,
        )
        if not is_last_nivel:
            next_nivel = CURRICULUM[nv + 1]
            if st.button(f"Seguir para {next_nivel['title']}", icon=":material/arrow_forward:",
                         type="primary", key="next_nivel"):
                go("missao", nv + 1, 0)
        else:
            st.balloons()
            st.markdown(
                '<div class="completion-banner">'
                '  <h2>Trilha Completa!</h2>'
                '  <p>Parabéns! Você dominou todos os conceitos de POO!</p>'
                '</div>',
                unsafe_allow_html=True,
            )
            if st.button("Ver trilha completa", icon=":material/map:", type="primary"):
                go("trilha")
    else:
        # ── Navigation buttons ────────────────────────────────
        btn_cols = st.columns([1, 2])
        missao_concluida = st.session_state.ex_correct

        if is_last_in_nivel and not is_last_nivel:
            next_label = f"Seguir para {CURRICULUM[nv + 1]['title']}"
            next_icon = ":material/arrow_forward:"
        elif is_last_in_nivel and is_last_nivel:
            next_label = "Finalizar trilha"
            next_icon = ":material/flag:"
        else:
            next_ms = nivel["missoes"][ms + 1] if ms + 1 < len(nivel["missoes"]) else None
            next_label = f"Próxima Missão: {next_ms['title']}" if next_ms else "Próxima Missão"
            next_icon = ":material/arrow_forward:"

        with btn_cols[0]:
            # Previous missao
            if ms > 0:
                if st.button("Anterior", icon=":material/arrow_back:", key="prev_ms"):
                    go("missao", nv, ms - 1)
            elif nv > 0:
                prev_nivel = CURRICULUM[nv - 1]
                if st.button("Anterior", icon=":material/arrow_back:", key="prev_ms_nv"):
                    go("missao", nv - 1, len(prev_nivel["missoes"]) - 1)

        with btn_cols[1]:
            st.markdown('<span class="next-btn-marker"></span>', unsafe_allow_html=True)
            btn_type = "primary" if missao_concluida else "secondary"
            if st.button(next_label, icon=next_icon, type=btn_type, key="next_ms"):
                if missao_concluida:
                    navigate_next()
                else:
                    skip_dialog()


# ══════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════

screen = st.session_state.screen

if screen == "dashboard":
    screen_dashboard()
elif screen == "trilha":
    screen_trilha()
elif screen == "missao":
    screen_missao()
