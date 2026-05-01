import json
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from curriculum import CURRICULUM


def export_curriculum():
    result = []

    for nivel_idx, nivel in enumerate(CURRICULUM):
        nivel_num = nivel_idx + 1
        nivel_data = {
            "id": nivel["id"],
            "title": nivel["title"],
            "short": nivel["short"],
            "missoes": [],
        }

        for missao_idx, missao in enumerate(nivel["missoes"]):
            missao_num = missao_idx + 1
            has_interativo = "render_interativo" in missao

            missao_data = {
                "id": missao["id"],
                "title": missao["title"],
                "icon": missao["icon"],
                "theory": missao["theory"],
                "exercise": missao["exercise"],
                "has_interativo": has_interativo,
            }

            if has_interativo:
                mod_name = f"curriculum.nivel_{nivel_num}.missao_{missao_num}"
                try:
                    mod = importlib.import_module(mod_name)
                    html = getattr(mod, "_HTML", None)
                    if html:
                        html_dir = os.path.join("export", "interativos")
                        os.makedirs(html_dir, exist_ok=True)
                        html_file = f"nivel_{nivel_num}_missao_{missao_num}.html"
                        with open(os.path.join(html_dir, html_file), "w", encoding="utf-8") as f:
                            f.write(html)
                        missao_data["interativo_html"] = f"interativos/{html_file}"
                except Exception as e:
                    print(f"AVISO: Erro ao exportar interativo de {mod_name}: {e}")

            nivel_data["missoes"].append(missao_data)

        result.append(nivel_data)

    return result


if __name__ == "__main__":
    data = export_curriculum()
    os.makedirs("export", exist_ok=True)

    with open("export/curriculum.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total = sum(len(n["missoes"]) for n in data)
    interativos = sum(1 for n in data for m in n["missoes"] if m.get("has_interativo"))

    print(f"OK: Exportado em export/curriculum.json")
    print(f"   {len(data)} niveis | {total} missoes | {interativos} com mini-jogo")
    if interativos:
        print(f"   HTMLs dos mini-jogos em export/interativos/")
