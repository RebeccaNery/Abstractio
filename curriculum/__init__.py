from .modulo_1 import MODULO_1
from .modulo_2 import MODULO_2
from .modulo_3 import MODULO_3
from .modulo_4 import MODULO_4

CURRICULUM = [MODULO_1, MODULO_2, MODULO_3, MODULO_4]


def get_flat_sections():
    """Returns list of (module_idx, section_idx, section_dict)."""
    flat = []
    for m_idx, module in enumerate(CURRICULUM):
        for s_idx, section in enumerate(module["sections"]):
            flat.append((m_idx, s_idx, section))
    return flat


def get_total_sections():
    return sum(len(m["sections"]) for m in CURRICULUM)
