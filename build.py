from jinja2 import Environment, FileSystemLoader
import markdown
from pathlib import Path
from datetime import datetime

# =========================================================
# JINJA SETUP
# =========================================================

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("base.html")

# =========================================================
# CONTENT CONFIG (PT / EN)
# =========================================================

SITE_CONTENT = {
    "pt": {
        "lang": "pt-BR",
        "page_title": "Willian Pina | Portfólio em Ciência de Dados",
        "hero_intro": "Eu sou",
        "hero_subtitle": "Entusiasta por dados, desafios e tecnologia.",
    },
    "en": {
        "lang": "en",
        "page_title": "Willian Pina | Data Science Portfolio",
        "hero_intro": "I am",
        "hero_subtitle": "Passionate about data, challenges, and technology.",
    },
}

# =========================================================
# RENDER FUNCTION
# =========================================================

def render_page(lang_key: str):
    content_dir = Path("content") / lang_key
    if not content_dir.exists():
        raise FileNotFoundError(f"Content directory not found: {content_dir}")

    # Load markdown sections
    sections = {}
    for md_file in content_dir.glob("*.md"):
        with open(md_file, encoding="utf-8") as f:
            sections[md_file.stem] = markdown.markdown(
                f.read(),
                extensions=["extra", "smarty"]
            )

    # Render HTML
    html = template.render(
        lang=SITE_CONTENT[lang_key]["lang"],
        page_title=SITE_CONTENT[lang_key]["page_title"],
        hero_intro=SITE_CONTENT[lang_key]["hero_intro"],
        hero_subtitle=SITE_CONTENT[lang_key]["hero_subtitle"],
        sections=sections,
        year=datetime.now().year,
    )

    # Output file (GitHub Pages root)
    output_file = (
        Path("index.html")
        if lang_key == "en"
        else Path("index_pt.html")
    )

    output_file.write_text(html, encoding="utf-8")
    print(f"✔ Página gerada: {output_file}")

# =========================================================
# BUILD
# =========================================================

render_page("en")
render_page("pt")

print("✅ Site gerado com sucesso")


print("✅ Site gerado com sucesso")
