import streamlit as st
from curriculum import CURRICULUM, get_flat_sections, get_total_sections

st.set_page_config(
    page_title="Abstractio — POO Gamificado",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════════════════════

st.markdown("""
<style>
/* ── Base ─────────────────────────────────────────── */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #0f0f23;
    color: #e2e8f0;
}
[data-testid="stSidebar"] {
    background-color: #1a1a2e;
    border-right: 1px solid #2d2d44;
}
[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}
.main .block-container {
    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
    max-width: 1100px;
}

/* ── Buttons ──────────────────────────────────────── */
.stButton > button {
    background-color: #1e1e35;
    color: #e2e8f0;
    border: 1px solid #3d3d5e;
    border-radius: 8px;
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background-color: #2d2d4e;
    border-color: #7c3aed;
    color: #fff;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed, #5b21b6);
    border: none;
    color: white;
    font-weight: 600;
    letter-spacing: 0.03em;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #8b5cf6, #7c3aed);
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(124,58,237,0.5);
}

/* ── Metrics ─────────────────────────────────────── */
[data-testid="stMetricValue"] {
    color: #a78bfa !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
}
[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-size: 0.75rem !important;
}

/* ── Markdown headings ───────────────────────────── */
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: #c4b5fd;
}

/* ── Code blocks ─────────────────────────────────── */
.stMarkdown pre {
    background-color: #0d0d1f !important;
    border: 1px solid #2d2d44;
    border-radius: 8px;
}

/* ── Radio ───────────────────────────────────────── */
.stRadio > div > label {
    background-color: #1a1a2e;
    border: 1px solid #2d2d44;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    margin-bottom: 6px;
    cursor: pointer;
    transition: border-color 0.15s;
}
.stRadio > div > label:hover {
    border-color: #7c3aed;
}
[data-testid="stRadio"] label span {
    color: #e2e8f0 !important;
}

/* ── Alerts / info boxes ─────────────────────────── */
[data-testid="stInfo"] {
    background-color: #1e1e35;
    border-left: 4px solid #7c3aed;
    color: #c4b5fd;
}
[data-testid="stSuccess"] {
    background-color: #052e16;
    border-left: 4px solid #10b981;
}
[data-testid="stWarning"] {
    background-color: #1c1700;
    border-left: 4px solid #f59e0b;
}

/* ── Dividers ────────────────────────────────────── */
hr {
    border-color: #2d2d44;
}

/* ── Progress bar custom ─────────────────────────── */
.pb-wrap {
    background: #1a1a2e;
    border: 1px solid #2d2d44;
    border-radius: 12px;
    padding: 14px 20px;
    margin-bottom: 1.5rem;
}
.pb-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}
.pb-title {
    font-size: 0.78rem;
    color: #94a3b8;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.pb-percent {
    font-size: 0.85rem;
    color: #a78bfa;
    font-weight: 700;
}
.pb-track {
    display: flex;
    align-items: center;
    gap: 0;
    flex-wrap: nowrap;
    overflow-x: auto;
    padding-bottom: 4px;
}
.pb-module-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
}
.pb-module-label {
    font-size: 0.65rem;
    color: #64748b;
    white-space: nowrap;
}
.pb-circles {
    display: flex;
    align-items: center;
    gap: 4px;
}
.pb-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #374151;
    border: 2px solid #4b5563;
    flex-shrink: 0;
    transition: all 0.2s;
}
.pb-dot.done {
    background: #10b981;
    border-color: #059669;
}
.pb-dot.active {
    background: #7c3aed;
    border-color: #a78bfa;
    box-shadow: 0 0 8px rgba(124,58,237,0.7);
}
.pb-connector {
    width: 16px;
    height: 2px;
    background: #374151;
    flex-shrink: 0;
}
.pb-connector.done {
    background: #10b981;
}
.pb-separator {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 10px;
    gap: 6px;
}
.pb-sep-label {
    font-size: 0.6rem;
    color: #475569;
    white-space: nowrap;
}
.pb-sep-line {
    width: 2px;
    height: 16px;
    background: #2d2d44;
}

/* ── Hero (dashboard) ────────────────────────────── */
.hero {
    background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 50%, #7c3aed 100%);
    border-radius: 16px;
    padding: 3.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "";
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    border-radius: 50%;
    background: rgba(255,255,255,0.05);
}
.hero-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 0.8rem;
}
.hero-sub {
    font-size: 1.05rem;
    color: #ddd6fe;
    max-width: 520px;
    line-height: 1.6;
    margin-bottom: 2rem;
}

/* ── Feature cards (dashboard) ───────────────────── */
.feat-card {
    background: #1a1a2e;
    border: 1px solid #2d2d44;
    border-radius: 12px;
    padding: 1.5rem;
    height: 100%;
    transition: border-color 0.2s, transform 0.2s;
}
.feat-card:hover {
    border-color: #7c3aed;
    transform: translateY(-2px);
}
.feat-card--muted {
    opacity: 0.4;
    pointer-events: none;
}
.feat-card--muted:hover {
    border-color: #2d2d44;
    transform: none;
}
.feat-icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
.feat-title {
    font-size: 1rem;
    font-weight: 700;
    color: #c4b5fd;
    margin-bottom: 0.4rem;
}
.feat-desc { font-size: 0.88rem; color: #94a3b8; line-height: 1.5; }

/* ── Section card ────────────────────────────────── */
.section-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    border-radius: 8px;
    margin-bottom: 4px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.15s;
}
.section-row:hover {
    background: #1e1e38;
    border-color: #3d3d5e;
}
.section-row.done {
    border-color: #065f46;
    background: #052e16;
}
.section-status { font-size: 0.9rem; min-width: 20px; }
.section-name { font-size: 0.92rem; color: #e2e8f0; flex: 1; }
.section-pts { font-size: 0.75rem; color: #64748b; }

/* ── Module block (trilha) ───────────────────────── */
.module-header {
    background: #1a1a2e;
    border: 1px solid #2d2d44;
    border-radius: 10px;
    padding: 1rem 1.4rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.module-title { font-size: 1rem; font-weight: 700; color: #c4b5fd; }
.module-pts { font-size: 0.8rem; color: #7c3aed; background: #1e1e35;
              padding: 2px 10px; border-radius: 20px; border: 1px solid #3d3d5e; }

/* ── Theory area ─────────────────────────────────── */
.theory-box {
    background: #1a1a2e;
    border: 1px solid #2d2d44;
    border-radius: 12px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
}

/* ── Exercise area ───────────────────────────────── */
.exercise-box {
    background: #12122a;
    border: 1px solid #3730a3;
    border-radius: 12px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
}
.exercise-title {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #818cf8;
    margin-bottom: 0.8rem;
}
.exercise-q { font-size: 1rem; color: #e2e8f0; margin-bottom: 1.2rem; }

/* ── Badge pills ─────────────────────────────────── */
.badge {
    display: inline-block;
    background: linear-gradient(135deg, #451a03, #92400e);
    border: 1px solid #b45309;
    color: #fcd34d;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 2px;
}

/* ── Completion banner ───────────────────────────── */
.completion-banner {
    background: linear-gradient(135deg, #052e16, #065f46);
    border: 1px solid #10b981;
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    margin: 1rem 0;
}
.completion-banner h2 { color: #34d399; margin-bottom: 0.5rem; }
.completion-banner p  { color: #6ee7b7; }

/* ── Dialog ─────────────────────────────────────── */
[data-testid="stDialog"] {
    background-color: #1a1a2e !important;
    border: 1px solid #3d3d5e !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════════════════════

NIVEIS = ["Iniciante", "Estagiário", "Júnior", "Pleno", "Sênior"]

EMBLEMAS_MAP = {
    50:  "🏅 Encapsuladora Iniciante",
    100: "🏆 Mestre da Herança",
    150: "💎 Rainha da Abstração",
    200: "🌟 Polimorfista Suprema",
}

# ══════════════════════════════════════════════════════════════
#  SESSION STATE INIT
# ══════════════════════════════════════════════════════════════

def _init():
    defaults = {
        "screen":             "dashboard",
        "module_idx":         0,
        "section_idx":        0,
        "pontuacao":          10,
        "nivel":              "Iniciante",
        "nivel_idx":          0,
        "completed":          set(),   # set of "m-s" strings
        "modules_done":       set(),   # set of module indices
        "emblemas":           [],
        "first_visit":        True,
        # per-section exercise state (keyed so navigating resets it)
        "ex_key":             "",      # current section id
        "ex_submitted":       False,
        "ex_correct":         False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init()

# Show welcome toast once
if st.session_state.first_visit:
    st.toast("🎉 Parabéns por iniciar sua jornada!", icon="🚀")
    st.session_state.first_visit = False

# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════

def go(screen, module_idx=None, section_idx=None):
    st.session_state.screen = screen
    if module_idx is not None:
        st.session_state.module_idx = module_idx
    if section_idx is not None:
        st.session_state.section_idx = section_idx
    st.rerun()


def section_key(m, s):
    return f"{m}-{s}"


def is_done(m, s):
    return section_key(m, s) in st.session_state.completed


def reset_exercise(m, s):
    key = section_key(m, s)
    if st.session_state.ex_key != key:
        st.session_state.ex_key = key
        st.session_state.ex_submitted = False
        st.session_state.ex_correct = is_done(m, s)  # already done → mark correct


def _award_points(n):
    old = st.session_state.pontuacao
    st.session_state.pontuacao += n
    new = st.session_state.pontuacao
    for threshold, badge in EMBLEMAS_MAP.items():
        if old < threshold <= new and badge not in st.session_state.emblemas:
            st.session_state.emblemas.append(badge)
            st.toast(f"🎖️ Emblema desbloqueado: {badge}!", icon="🏅")


def complete_section(m, s):
    key = section_key(m, s)
    if key not in st.session_state.completed:
        st.session_state.completed.add(key)
        st.session_state.ex_correct = True
        _award_points(15)
        st.toast("+15 pontos! Continue assim! 🔥", icon="⭐")
        # Check module completion
        module = CURRICULUM[m]
        needed = {section_key(m, i) for i in range(len(module["sections"]))}
        if needed.issubset(st.session_state.completed) and m not in st.session_state.modules_done:
            st.session_state.modules_done.add(m)
            _nivel_up()


def _nivel_up():
    idx = st.session_state.nivel_idx
    if idx < len(NIVEIS) - 1:
        st.session_state.nivel_idx += 1
        st.session_state.nivel = NIVEIS[st.session_state.nivel_idx]
        st.toast(f"⬆️ Você evoluiu para **{st.session_state.nivel}**!", icon="🌟")


def navigate_next():
    m = st.session_state.module_idx
    s = st.session_state.section_idx
    module = CURRICULUM[m]
    if s + 1 < len(module["sections"]):
        go("secao", m, s + 1)
    elif m + 1 < len(CURRICULUM):
        go("secao", m + 1, 0)
    else:
        go("trilha")


# ══════════════════════════════════════════════════════════════
#  PROGRESS BAR
# ══════════════════════════════════════════════════════════════

def render_progress_bar():
    flat = get_flat_sections()
    total = len(flat)
    done_count = len(st.session_state.completed)
    pct = int(done_count / total * 100) if total else 0

    circles = ""
    prev_m = None

    for idx, (m_idx, s_idx, sec) in enumerate(flat):
        # Module separator
        if prev_m is not None and m_idx != prev_m:
            mod_label = CURRICULUM[m_idx]["short"]
            circles += (
                f'<div class="pb-separator">'
                f'  <div class="pb-sep-label">{mod_label}</div>'
                f'  <div class="pb-sep-line"></div>'
                f'</div>'
            )
        elif prev_m is None:
            # First module label
            mod_label = CURRICULUM[m_idx]["short"]
            circles += (
                f'<div class="pb-separator" style="margin-left:0;margin-right:6px">'
                f'  <div class="pb-sep-label">{mod_label}</div>'
                f'  <div class="pb-sep-line"></div>'
                f'</div>'
            )

        # Connector before dot (not first in module)
        if prev_m == m_idx:
            conn_cls = "pb-connector done" if is_done(m_idx, s_idx) else "pb-connector"
            circles += f'<div class="{conn_cls}"></div>'

        # Dot
        is_active = (
            st.session_state.screen == "secao"
            and m_idx == st.session_state.module_idx
            and s_idx == st.session_state.section_idx
        )
        if is_active:
            dot_cls = "pb-dot active"
        elif is_done(m_idx, s_idx):
            dot_cls = "pb-dot done"
        else:
            dot_cls = "pb-dot"

        circles += f'<div class="{dot_cls}" title="{sec["title"]}"></div>'
        prev_m = m_idx

    html = f"""
    <div class="pb-wrap">
      <div class="pb-header">
        <span class="pb-title">Progresso da Trilha</span>
        <span class="pb-percent">{done_count}/{total} seções &nbsp;·&nbsp; {pct}%</span>
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
        st.markdown("## 🎓 Abstractio")
        st.caption("Aprenda POO na prática")
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("⭐ Pontos", st.session_state.pontuacao)
        with col2:
            st.metric("🏆 Nível", st.session_state.nivel)

        st.divider()

        if st.button("Dashboard", icon=":material/home:", use_container_width=True,
                     type="primary" if st.session_state.screen == "dashboard" else "secondary"):
            go("dashboard")

        if st.button("Trilha POO", icon=":material/map:", use_container_width=True,
                     type="primary" if st.session_state.screen == "trilha" else "secondary"):
            go("trilha")

        if st.session_state.emblemas:
            st.divider()
            st.markdown("**🎖️ Emblemas**")
            for badge in st.session_state.emblemas:
                st.markdown(f'<span class="badge">{badge}</span>', unsafe_allow_html=True)


render_sidebar()

# ══════════════════════════════════════════════════════════════
#  DIALOG — skip confirmation
# ══════════════════════════════════════════════════════════════

@st.dialog("⚠️ Exercício não concluído")
def skip_dialog():
    st.markdown(
        "Tem certeza que quer prosseguir? "
        "Você ainda não concluiu o exercício da seção atual."
    )
    st.markdown("Você pode voltar a qualquer momento para completá-lo.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Sim, prosseguir", type="primary", use_container_width=True):
            navigate_next()
    with col2:
        if st.button("↩️ Cancelar", use_container_width=True):
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
        if st.button("🚀 Comece já!", type="primary", use_container_width=True):
            go("trilha")

    st.markdown("---")
    st.markdown("### Destaques")

    c1, c2, c3 = st.columns(3)
    cards = [
        ("🎯", "Orientação a Objetos",
         "Classes, herança e polimorfismo para criar código como um profissional.", False),
        ("🗄️", "Estruturas de Dados",
         "Do array ao grafo, domine como organizar dados de forma eficiente.", True),
        ("📌", "Ponteiros",
         "Domine boas ordenações e eficiência computacional com exemplos reais.", True),
    ]
    for col, (icon, title, desc, muted) in zip([c1, c2, c3], cards):
        with col:
            css_class = "feat-card feat-card--muted" if muted else "feat-card"
            st.markdown(
                f'<div class="{css_class}">'
                f'  <div class="feat-icon">{icon}</div>'
                f'  <div class="feat-title">{title}</div>'
                f'  <div class="feat-desc">{desc}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
            if not muted:
                st.write("")
                if st.button("Explorar →", key="hero_explore", type="primary"):
                    go("trilha")
            else:
                st.markdown('<p style="color:#555570;font-size:0.75rem;margin-top:0.5rem;">em breve</p>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  SCREEN: TRILHA
# ══════════════════════════════════════════════════════════════

def screen_trilha():
    render_progress_bar()

    st.markdown("## 🎓 Programação Orientada a Objetos")

    st.info(
        "Você irá aprender todos os conceitos fundamentais de POO — classes, objetos, "
        "encapsulamento, herança e polimorfismo — com exemplos práticos e exercícios reais.",
    )
    st.markdown("---")

    for m_idx, module in enumerate(CURRICULUM):
        total_s = len(module["sections"])
        done_s = sum(1 for s_idx in range(total_s) if is_done(m_idx, s_idx))
        pts_total = total_s * 15

        st.markdown(
            f'<div class="module-header">'
            f'  <span class="module-title">{module["title"]}</span>'
            f'  <span class="module-pts">{done_s}/{total_s} seções &nbsp;·&nbsp; {pts_total} pts</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

        for s_idx, section in enumerate(module["sections"]):
            done = is_done(m_idx, s_idx)
            status_icon = "✅" if done else "🔵"
            col_sec, col_btn = st.columns([5, 1])
            with col_sec:
                st.markdown(
                    f'<div class="section-row {"done" if done else ""}">'
                    f'  <span class="section-status">{status_icon}</span>'
                    f'  <span class="section-name">{section["icon"]} {section["title"]}</span>'
                    f'  <span class="section-pts">+15 pts</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            with col_btn:
                btn_label = "✓ Rever" if done else "→ Iniciar"
                if st.button(btn_label, key=f"trl_{m_idx}_{s_idx}",
                             type="primary" if not done else "secondary"):
                    go("secao", m_idx, s_idx)

        st.markdown("")

    # Pre-requisites note
    st.caption("Pré-requisitos: Nenhum pré-requisito obrigatório. Ter noções básicas de lógica de programação é recomendado.")


# ══════════════════════════════════════════════════════════════
#  SCREEN: SEÇÃO
# ══════════════════════════════════════════════════════════════

def screen_secao():
    m = st.session_state.module_idx
    s = st.session_state.section_idx
    module = CURRICULUM[m]
    section = module["sections"][s]
    is_last_in_module = (s == len(module["sections"]) - 1)
    is_last_module = (m == len(CURRICULUM) - 1)

    reset_exercise(m, s)

    render_progress_bar()

    # Breadcrumb
    col_bc, col_nav = st.columns([4, 1])
    with col_bc:
        st.caption(f"{module['title']} › {section['title']}")
    with col_nav:
        if st.button("← Trilha", key="back_to_trilha"):
            go("trilha")

    st.markdown(f"# {section['icon']} {section['title']}")
    st.markdown("---")

    # ── Theory ──────────────────────────────────────────────
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown(section["theory"])
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Interactive placeholder ──────────────────────────────
    st.info("🎮 **Interação Visual / Jogo** — `# TODO`: mini-jogo interativo para esta seção será implementado aqui.")

    st.markdown("---")

    # ── Exercise ─────────────────────────────────────────────
    ex = section["exercise"]
    st.markdown('<div class="exercise-box">', unsafe_allow_html=True)
    st.markdown('<div class="exercise-title">🧪 Exercício Prático</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="exercise-q">{ex["question"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    selected = st.radio(
        "Escolha sua resposta:",
        options=list(range(len(ex["options"]))),
        format_func=lambda i: ex["options"][i],
        key=f"radio_{section['id']}",
        index=None if not st.session_state.ex_correct else ex["correct"],
        label_visibility="collapsed",
    )

    col_test, _ = st.columns([1, 3])

    with col_test:
        test_disabled = st.session_state.ex_correct
        if st.button("🧪 Testar", key=f"test_{section['id']}",
                     disabled=test_disabled, use_container_width=True):
            if selected is None:
                st.warning("Selecione uma alternativa antes de testar.")
            else:
                st.session_state.ex_submitted = True
                if selected == ex["correct"]:
                    complete_section(m, s)
                    st.rerun()

    # Feedback
    if st.session_state.ex_submitted and not st.session_state.ex_correct:
        st.error("❌ Resposta incorreta. Revise o conteúdo e tente novamente!")

    if st.session_state.ex_correct:
        st.success(f"✅ {ex['explanation']}")

    st.markdown("---")

    # ── Module completion banner ──────────────────────────────
    module_complete = m in st.session_state.modules_done

    if is_last_in_module and module_complete:
        st.markdown(
            f'<div class="completion-banner">'
            f'  <h2>🎉 Módulo concluído!</h2>'
            f'  <p>Você completou <strong>{module["title"]}</strong> e avançou para '
            f'  o nível <strong>{st.session_state.nivel}</strong>!</p>'
            f'</div>',
            unsafe_allow_html=True,
        )
        if not is_last_module:
            next_module = CURRICULUM[m + 1]
            if st.button(f"➡️ Seguir para {next_module['title']}",
                         type="primary", key="next_module"):
                go("secao", m + 1, 0)
        else:
            st.balloons()
            st.markdown(
                '<div class="completion-banner">'
                '  <h2>🏆 Trilha Completa!</h2>'
                '  <p>Parabéns! Você dominou todos os conceitos de POO!</p>'
                '</div>',
                unsafe_allow_html=True,
            )
            if st.button("🗺️ Ver trilha completa", type="primary"):
                go("trilha")
    else:
        # ── Navigation buttons ────────────────────────────────
        btn_cols = st.columns([1, 1, 3])
        section_completed = st.session_state.ex_correct

        if is_last_in_module and not is_last_module:
            next_label = f"➡️ Seguir para {CURRICULUM[m + 1]['title']}"
        elif is_last_in_module and is_last_module:
            next_label = "🏁 Finalizar trilha"
        else:
            next_module_sections = module["sections"]
            next_sec = next_module_sections[s + 1] if s + 1 < len(next_module_sections) else None
            next_label = f"→ Próxima: {next_sec['title']}" if next_sec else "→ Próxima seção"

        with btn_cols[0]:
            # Previous section
            if s > 0:
                if st.button("← Anterior", key="prev_sec"):
                    go("secao", m, s - 1)
            elif m > 0:
                prev_module = CURRICULUM[m - 1]
                if st.button("← Anterior", key="prev_sec_mod"):
                    go("secao", m - 1, len(prev_module["sections"]) - 1)

        with btn_cols[1]:
            btn_type = "primary" if section_completed else "secondary"
            if st.button(next_label, type=btn_type, key="next_sec", use_container_width=True):
                if section_completed:
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
elif screen == "secao":
    screen_secao()
