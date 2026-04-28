from .nivel_1 import NIVEL as NIVEL_1
from .nivel_2 import NIVEL as NIVEL_2
from .nivel_3 import NIVEL as NIVEL_3
from .nivel_4 import NIVEL as NIVEL_4

CURRICULUM = [NIVEL_1, NIVEL_2, NIVEL_3, NIVEL_4]


def get_flat_missoes():
    """Returns list of (nivel_idx, missao_idx, missao_dict)."""
    flat = []
    for nv_idx, nivel in enumerate(CURRICULUM):
        for ms_idx, missao in enumerate(nivel["missoes"]):
            flat.append((nv_idx, ms_idx, missao))
    return flat


def get_total_missoes():
    return sum(len(nv["missoes"]) for nv in CURRICULUM)
