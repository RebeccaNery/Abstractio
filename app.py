import base64
import os
import streamlit as st
import streamlit.components.v1 as components

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

NIVEL_NOMES = ["Polvinho", "Explorador", "Mestre dos Mares", "Kraken"]

EMBLEMAS = {
    # Nível 1 — Fundamentos
    "0-0": {"nome_f": "Descobridora do Paradigma", "nome_m": "Descobridor do Paradigma",  "icon": "🧩"},
    "0-1": {"nome_f": "Escultora de Classes",       "nome_m": "Escultor de Classes",        "icon": "🏛️"},
    "0-2": {"nome_f": "Criadora de Objetos",        "nome_m": "Criador de Objetos",         "icon": "🐙"},
    "0-3": {"nome_f": "Invocadora de Métodos",      "nome_m": "Invocador de Métodos",       "icon": "⚡"},
    "0-4": {"nome_f": "Mestra do Construtor",       "nome_m": "Mestre do Construtor",       "icon": "🔨"},
    "0-5": {"nome_f": "Fundamentos Dominados",      "nome_m": "Fundamentos Dominados",      "icon": "⭐"},
    # Nível 2 — As leis do mundo
    "1-0": {"nome_f": "Exploradora dos Pilares",    "nome_m": "Explorador dos Pilares",     "icon": "🌊"},
    "1-1": {"nome_f": "Pensadora Abstrata",         "nome_m": "Pensador Abstrato",          "icon": "💭"},
    "1-2": {"nome_f": "Guardiã do Segredo",         "nome_m": "Guardião do Segredo",        "icon": "🔒"},
    "1-3": {"nome_f": "Herdeira do Código",         "nome_m": "Herdeiro do Código",         "icon": "🧬"},
    "1-4": {"nome_f": "Mestra das Formas",          "nome_m": "Mestre das Formas",          "icon": "🦋"},
    "1-5": {"nome_f": "Pilares Conquistados",       "nome_m": "Pilares Conquistados",       "icon": "🏆"},
    # Nível 3 — A sociedade dos objetos
    "2-0":  {"nome_f": "Exploradora das Relações",  "nome_m": "Explorador das Relações",    "icon": "🗺️"},
    "2-1":  {"nome_f": "Reescritora de Leis",       "nome_m": "Reescritor de Leis",         "icon": "✍️"},
    "2-2":  {"nome_f": "Sobrecarregada de Poder",   "nome_m": "Sobrecarregado de Poder",    "icon": "⚡"},
    "2-3":  {"nome_f": "Firmadora de Contratos",    "nome_m": "Firmador de Contratos",      "icon": "📜"},
    "2-4":  {"nome_f": "Arquiteta de Interfaces",   "nome_m": "Arquiteto de Interfaces",    "icon": "🔌"},
    "2-5":  {"nome_f": "Mestra da Abstração",       "nome_m": "Mestre da Abstração",        "icon": "🎭"},
    "2-6":  {"nome_f": "Conectora de Mundos",       "nome_m": "Conector de Mundos",         "icon": "🕸️"},
    "2-7":  {"nome_f": "Tecelã de Associações",     "nome_m": "Tecelão de Associações",     "icon": "🧵"},
    "2-8":  {"nome_f": "Guardiã da Agregação",      "nome_m": "Guardião da Agregação",      "icon": "🫧"},
    "2-9":  {"nome_f": "Compositora de Sistemas",   "nome_m": "Compositor de Sistemas",     "icon": "🎼"},
    "2-10": {"nome_f": "Sociedade Dominada",        "nome_m": "Sociedade Dominada",         "icon": "🌐"},
    # Nível 4 — O arquiteto mestre
    "3-0": {"nome_f": "Aprendiz da Arquitetura",    "nome_m": "Aprendiz da Arquitetura",    "icon": "🏗️"},
    "3-1": {"nome_f": "Mestra da Coesão",           "nome_m": "Mestre da Coesão",           "icon": "🎯"},
    "3-2": {"nome_f": "Redutora do Acoplamento",    "nome_m": "Redutor do Acoplamento",     "icon": "⚗️"},
    "3-3": {"nome_f": "Princesa SOLID",             "nome_m": "Príncipe SOLID",             "icon": "💎"},
    "3-4": {"nome_f": "Domadora dos Generics",      "nome_m": "Domador dos Generics",       "icon": "🧲"},
    "3-5": {"nome_f": "Conhecedora dos Padrões",    "nome_m": "Conhecedor dos Padrões",     "icon": "🗝️"},
    "3-6": {"nome_f": "Arquiteta Mestre",           "nome_m": "Arquiteto Mestre",           "icon": "👑"},
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
        "nivel_nome":          "Polvinho",
        "nivel_nome_idx":      0,
        "completed":           set(),   # set of "nv-ms" strings
        "niveis_concluidos":   set(),   # set of nivel indices
        "new_emblema":         None,    # id da missão recém-concluída (para o dialog)
        "nome":                "",
        "genero":              "feminino",
        "avatar":              "octopus.png",
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

@st.cache_data
def _avatar_b64(filename):
    with open(f"assets/avatars/{filename}", "rb") as f:
        return base64.b64encode(f.read()).decode()


def _avatar_html():
    av = st.session_state.avatar
    if av.endswith(".png"):
        b64 = _avatar_b64(av)
        return f'<img src="data:image/png;base64,{b64}" style="width:100%;height:100%;object-fit:cover;border-radius:50%;">'
    return av


def get_emblema_nome(emb):
    genero = st.session_state.genero
    if genero == "feminino":
        return emb["nome_f"]
    if genero == "masculino":
        return emb["nome_m"]
    partes = emb["nome_m"].split(" ", 1)
    return partes[0] + "(a)" + (" " + partes[1] if len(partes) > 1 else "")


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
    st.session_state.pontuacao += n


def complete_missao(nv, ms):
    key = missao_key(nv, ms)
    if key not in st.session_state.completed:
        st.session_state.completed = st.session_state.completed | {key}
        st.session_state.ex_correct = True
        _award_points(15)
        st.toast("+15 pontos! Continue assim!", icon=":material/star:")
        if EMBLEMAS.get(key):
            st.session_state.new_emblema = key
        nivel = CURRICULUM[nv]
        needed = {missao_key(nv, i) for i in range(len(nivel["missoes"]))}
        if needed.issubset(st.session_state.completed) and nv not in st.session_state.niveis_concluidos:
            st.session_state.niveis_concluidos = st.session_state.niveis_concluidos | {nv}
            _atualizar_nivel_nome()


def _atualizar_nivel_nome():
    new_idx = min(len(st.session_state.niveis_concluidos), len(NIVEL_NOMES) - 1)
    if new_idx > st.session_state.nivel_nome_idx:
        st.session_state.nivel_nome_idx = new_idx
        st.session_state.nivel_nome = NIVEL_NOMES[new_idx]
        st.toast(f"Você evoluiu para **{NIVEL_NOMES[new_idx]}**!", icon=":material/trending_up:")


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
        nome_exibido = st.session_state.nome or "Sr. Polvonilson"
        st.markdown('<div class="sidebar-title-top">Abstractio</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="avatar-circle" id="st-avatar-circle">{_avatar_html()}</div>',
            unsafe_allow_html=True,
        )
        if st.button("go_perfil", key="sidebar_avatar"):
            go("perfil")
        components.html("""
        <script>
        (function poll() {
            var doc = window.parent.document;
            var circle = doc.getElementById('st-avatar-circle');
            var target = null;
            var btns = doc.querySelectorAll('button');
            for (var i = 0; i < btns.length; i++) {
                if (btns[i].innerText.trim() === 'go_perfil') { target = btns[i]; break; }
            }
            if (!circle || !target) { setTimeout(poll, 150); return; }
            var wrapper = target.closest('div[data-testid]') || target.parentElement;
            if (wrapper) wrapper.style.display = 'none';
            if (circle.dataset.wired) return;
            circle.dataset.wired = '1';
            circle.style.cursor = 'pointer';
            circle.addEventListener('click', function() { target.click(); });
        })();
        </script>
        """, height=0)
        st.markdown(f'<div class="sidebar-nome">{nome_exibido}</div>', unsafe_allow_html=True)
        st.divider()

        st.metric("Pontos", st.session_state.pontuacao)
        st.metric("Nível", st.session_state.nivel_nome)

        st.divider()

        if st.button("Dashboard", icon=":material/home:", use_container_width=True,
                     type="primary" if st.session_state.screen == "dashboard" else "secondary"):
            go("dashboard")

        if st.button("Minhas Trilhas", icon=":material/map:", use_container_width=True,
                     type="primary" if st.session_state.screen == "trilhas" else "secondary"):
            go("trilhas")

        if st.button("Conquistas", icon=":material/military_tech:", use_container_width=True,
                     type="primary" if st.session_state.screen == "conquistas" else "secondary"):
            go("conquistas")


render_sidebar()

# ══════════════════════════════════════════════════════════════
#  DIALOG — skip confirmation
# ══════════════════════════════════════════════════════════════

@st.dialog("🏆 Troféu desbloqueado!")
def emblema_dialog():
    emb = EMBLEMAS[st.session_state.new_emblema]
    st.markdown(
        f'<div style="text-align:center;font-size:4.5rem;margin:0.5rem 0">{emb["icon"]}</div>'
        f'<div style="text-align:center;font-size:1.1rem;font-weight:700;color:#c4b5fd;margin-bottom:0.4rem">'
        f'{get_emblema_nome(emb)}</div>'
        f'<div style="text-align:center;font-size:0.9rem;color:#94a3b8">'
        f'Parabéns! Você conquistou este troféu ao concluir a missão.</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ver minhas conquistas", icon=":material/military_tech:", use_container_width=True):
            st.session_state.new_emblema = None
            go("conquistas")
    with col2:
        if st.button("Próxima Missão", icon=":material/arrow_forward:", type="primary", use_container_width=True):
            st.session_state.new_emblema = None
            navigate_next()


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

    # Carrossel hero (apenas visual — sem botões ocultos)
    st.markdown("""
    <div class="hero-carousel">
      <div class="hero hero-slide active">
        <div class="hero-title">Bem-vindo ao Abstractio</div>
        <div class="hero-sub">Aprenda os conceitos de Orientação a Objetos na prática,
        com lições interativas e jogos em cada nível.</div>
      </div>
      <div class="hero hero-slide">
        <div class="hero-title">Conheça o Abstractio</div>
        <div class="hero-sub">Entenda como funcionam os Níveis, Missões, Exercícios
        e Emblemas da plataforma.</div>
      </div>
      <div class="hero-dots">
        <span class="hero-dot active" data-idx="0"></span>
        <span class="hero-dot" data-idx="1"></span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # JS: apenas animação dos slides (sem truques de botões ocultos)
    components.html("""
    <script>
    (function() {
        var doc = window.parent.document;
        var current = 0;
        var timer;

        function goTo(n) {
            var slides = doc.querySelectorAll('.hero-slide');
            var dots   = doc.querySelectorAll('.hero-dot');
            slides.forEach(function(s, i) { s.classList.toggle('active', i === n); });
            dots.forEach(function(d, i)   { d.classList.toggle('active', i === n); });
            current = n;
        }

        function startTimer() {
            clearInterval(timer);
            timer = setInterval(function() { goTo((current + 1) % 2); }, 5000);
        }

        function setup() {
            var dots = doc.querySelectorAll('.hero-dot');
            if (!dots.length) { setTimeout(setup, 150); return; }
            dots.forEach(function(dot) {
                dot.addEventListener('click', function() {
                    goTo(parseInt(dot.dataset.idx));
                    startTimer();
                });
            });
            startTimer();
        }
        setup();
    })();
    </script>
    """, height=0)

    # CTAs reais abaixo do carrossel
    col_a, col_b, _ = st.columns([1, 1, 2])
    with col_a:
        if st.button("Comece já", icon=":material/rocket_launch:", type="primary", use_container_width=True):
            go("trilhas")
    with col_b:
        if st.button("Como funciona", icon=":material/info:", use_container_width=True):
            go("como_funciona")

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
                    go("trilhas")
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
                    f'  <span class="section-name">Missão {ms_idx + 1} — {missao["title"]}</span>'
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
    col_nav, col_bc = st.columns([1, 4])
    with col_nav:
        if st.button("Trilha", icon=":material/arrow_back:", key="back_to_trilha"):
            go("trilha")
    with col_bc:
        st.caption(f"{nivel['title']} › {missao['title']}")

    st.markdown(f"# {missao['title']}")

    # ── Theory ──────────────────────────────────────────────
    st.markdown(missao["theory"])

    # ── Interactive ──────────────────────────────────────────
    if "render_interativo" in missao and callable(missao["render_interativo"]):
        missao["render_interativo"]()
    else:
        st.info("Componente interativo em breve.")

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
            f'  <p>Você completou <strong>{nivel["title"]}</strong> e virou <strong>{st.session_state.nivel_nome}</strong>!</p>'
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
                    if st.session_state.new_emblema:
                        emblema_dialog()
                    else:
                        navigate_next()
                else:
                    skip_dialog()


# ══════════════════════════════════════════════════════════════
#  SCREEN: PERFIL
# ══════════════════════════════════════════════════════════════

AVATARES = sorted(f for f in os.listdir("assets/avatars") if f.endswith(".png"))

def screen_perfil():
    col_back, _ = st.columns([1, 5])
    with col_back:
        if st.button("Voltar", icon=":material/arrow_back:", key="perfil_back"):
            go("dashboard")

    nome_exibido = st.session_state.nome or "Sr. Polvonilson"
    missoes_feitas = len(st.session_state.completed)

    st.markdown(
        f'<div style="display:flex;flex-direction:column;align-items:center;gap:0.6rem;margin:1.5rem 0 2rem 0;">'
        f'  <div class="avatar-circle" style="width:130px;height:130px;font-size:3rem;pointer-events:none;">'
        f'    {_avatar_html()}'
        f'  </div>'
        f'  <div style="font-size:1.6rem;font-weight:700;color:#e2e8f0;">{nome_exibido}</div>'
        f'  <div style="font-size:0.9rem;color:#a78bfa;font-weight:600;">{st.session_state.nivel_nome}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Pontuação", st.session_state.pontuacao)
    with c2:
        st.metric("Missões concluídas", missoes_feitas)

    st.markdown("")
    col_btn, _ = st.columns([1, 2])
    with col_btn:
        if st.button("Editar perfil", icon=":material/edit:", type="primary", use_container_width=True):
            go("perfil_edit")


def screen_perfil_edit():
    col_back, _ = st.columns([1, 5])
    with col_back:
        if st.button("Voltar", icon=":material/arrow_back:", key="perfil_edit_back"):
            go("perfil")

    st.markdown("# Editar Perfil")
    st.markdown("---")

    nome = st.text_input(
        "Nome",
        value=st.session_state.nome,
        placeholder="Como quer ser chamado(a)?",
        key="perfil_nome_input",
    )

    st.markdown("**Gênero**")
    st.caption("Define a forma dos seus títulos de conquista.")
    gcols = st.columns(3)
    for col, (label, valor) in zip(gcols, [("Feminino", "feminino"), ("Masculino", "masculino"), ("Neutro", "neutro")]):
        with col:
            ativo = st.session_state.genero == valor
            if st.button(label, key=f"g_{valor}", type="primary" if ativo else "secondary", use_container_width=True):
                st.session_state.genero = valor
                st.rerun()

    st.markdown("**Avatar**")
    acols = st.columns(len(AVATARES))
    for col, av in zip(acols, AVATARES):
        with col:
            ativo = st.session_state.avatar == av
            b64 = _avatar_b64(av)
            borda = "#7c3aed" if ativo else "#2d2d44"
            st.markdown(
                f'<div style="width:72px;height:72px;border-radius:50%;border:3px solid {borda};'
                f'margin:0 auto 6px auto;overflow:hidden;cursor:pointer;">'
                f'<img src="data:image/png;base64,{b64}" style="width:100%;height:100%;object-fit:cover;">'
                f'</div>',
                unsafe_allow_html=True,
            )
            if st.button("✓" if ativo else " ", key=f"av_{av}",
                         type="primary" if ativo else "secondary",
                         use_container_width=True):
                st.session_state.avatar = av
                st.rerun()

    st.markdown("")
    if st.button("Salvar perfil", icon=":material/check:", type="primary"):
        st.session_state.nome = st.session_state.perfil_nome_input
        st.toast("Perfil salvo!", icon=":material/check:")
        go("perfil")


# ══════════════════════════════════════════════════════════════
#  SCREEN: MINHAS TRILHAS
# ══════════════════════════════════════════════════════════════

def screen_trilhas():
    st.markdown("# Minhas Trilhas")
    st.caption("Acompanhe seu progresso em cada trilha de aprendizado.")
    st.markdown("---")

    total = get_total_missoes()
    done  = len(st.session_state.completed)
    pct   = int(done / total * 100) if total else 0

    st.markdown(
        f'<div class="trail-card">'
        f'  <div class="trail-header">'
        f'    <div class="trail-icon"><img src="data:image/png;base64,{_avatar_b64("octopus.png")}" style="width:2.2rem;height:2.2rem;object-fit:cover;border-radius:50%;"></div>'
        f'    <div class="trail-info">'
        f'      <div class="trail-title">Orientação a Objetos</div>'
        f'      <div class="trail-sub">Python · {total} missões · 4 níveis</div>'
        f'    </div>'
        f'    <div class="trail-badge">{st.session_state.nivel_nome}</div>'
        f'  </div>'
        f'  <div class="trail-progress-wrap">'
        f'    <div class="trail-progress-bar">'
        f'      <div class="trail-progress-fill" style="width:{pct}%"></div>'
        f'    </div>'
        f'    <span class="trail-pct">{done}/{total} missões · {pct}%</span>'
        f'  </div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    if st.button("Acessar trilha", icon=":material/arrow_forward:", type="primary", key="acessar_poo"):
        go("trilha")

    st.markdown("### Em breve")
    cols = st.columns(2)
    futuras = [
        ("📊", "Estruturas de Dados", "Do array ao grafo, domine como organizar dados de forma eficiente."),
        ("📌", "Ponteiros",           "Domine boas ordenações e eficiência computacional com exemplos reais."),
    ]
    for col, (icon, title, desc) in zip(cols, futuras):
        with col:
            st.markdown(
                f'<div class="trail-card trail-card--locked">'
                f'  <div class="trail-header">'
                f'    <div class="trail-icon">{icon}</div>'
                f'    <div class="trail-info">'
                f'      <div class="trail-title">{title}</div>'
                f'      <div class="trail-sub">Em breve</div>'
                f'    </div>'
                f'    <div class="trail-lock">🔒</div>'
                f'  </div>'
                f'  <div class="trail-desc">{desc}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )


# ══════════════════════════════════════════════════════════════
#  SCREEN: CONQUISTAS
# ══════════════════════════════════════════════════════════════

def screen_conquistas():
    render_progress_bar()
    st.markdown("# Conquistas")
    st.caption("Cada missão concluída desbloqueia um troféu.")

    completed = st.session_state.completed

    for nivel in CURRICULUM:
        st.markdown(f"### {nivel['title']}")

        earned_html   = ""
        unearned_html = ""

        for missao in nivel["missoes"]:
            mid = missao["id"]
            emb = EMBLEMAS.get(mid)
            if not emb:
                continue
            card = (
                f'<div class="trophy-card {"earned" if mid in completed else "unearned"}">'
                f'  <div class="trophy-icon">{emb["icon"]}</div>'
                f'  <div class="trophy-nome">{get_emblema_nome(emb)}</div>'
                f'</div>'
            )
            if mid in completed:
                earned_html += card
            else:
                unearned_html += card

        if earned_html:
            st.markdown(f'<div class="trophy-shelf">{earned_html}</div>', unsafe_allow_html=True)
        else:
            st.caption("Nenhum troféu conquistado neste nível ainda.")

        if unearned_html:
            unearned_count = unearned_html.count("trophy-card")
            with st.expander(f"Ver {unearned_count} troféu(s) por conquistar"):
                st.markdown(f'<div class="trophy-shelf">{unearned_html}</div>', unsafe_allow_html=True)

        st.markdown("---")


# ══════════════════════════════════════════════════════════════
#  SCREEN: COMO FUNCIONA
# ══════════════════════════════════════════════════════════════

def screen_como_funciona():
    col_back, _ = st.columns([1, 5])
    with col_back:
        if st.button("Voltar", icon=":material/arrow_back:", key="como_back"):
            go("dashboard")

    st.markdown("# Como funciona o Abstractio")
    st.caption("Aprenda no seu ritmo, com missões práticas e recompensas a cada conquista.")
    st.markdown("---")

    passos = [
        ("🎯", "Níveis",      "O currículo é dividido em 4 Níveis, cada um cobrindo um tema central de POO. Avance do mais simples ao mais avançado."),
        ("📚", "Missões",     "Cada Nível contém de 6 a 11 Missões com explicação teórica e um componente interativo para praticar o conceito."),
        ("✏️", "Exercícios",  "Ao final de cada missão, responda um exercício de múltipla escolha para confirmar o aprendizado e ganhar +15 pontos."),
        ("🏆", "Emblemas",    "Cada missão concluída desbloqueia um Emblema exclusivo. Acesse Conquistas para ver sua estante de troféus."),
    ]

    for i, (icon, title, desc) in enumerate(passos):
        st.markdown(
            f'<div class="como-card">'
            f'  <div class="como-step">{i + 1}</div>'
            f'  <div class="como-icon">{icon}</div>'
            f'  <div class="como-body">'
            f'    <div class="como-title">{title}</div>'
            f'    <div class="como-desc">{desc}</div>'
            f'  </div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown("")
    col_btn, _ = st.columns([1, 3])
    with col_btn:
        if st.button("Começar agora", icon=":material/rocket_launch:", type="primary", use_container_width=True):
            go("trilhas")


# ══════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════

screen = st.session_state.screen

if screen == "dashboard":
    screen_dashboard()
elif screen == "perfil":
    screen_perfil()
elif screen == "perfil_edit":
    screen_perfil_edit()
elif screen == "trilhas":
    screen_trilhas()
elif screen == "trilha":
    screen_trilha()
elif screen == "missao":
    screen_missao()
elif screen == "conquistas":
    screen_conquistas()
elif screen == "como_funciona":
    screen_como_funciona()
