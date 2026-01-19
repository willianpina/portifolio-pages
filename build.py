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

    site_cfg = SITE_CONTENT[lang_key]

    # =====================================================
    # Load markdown sections (Jinja → Markdown)
    # =====================================================

    sections = {}

    for md_file in content_dir.glob("*.md"):
        with open(md_file, encoding="utf-8") as f:
            md_raw = f.read()

        # Render Markdown as Jinja template (for {{ year }}, etc.)
        md_template = env.from_string(md_raw)
        md_rendered = md_template.render(
            year=datetime.now().year
        )

        # Convert Markdown to HTML
        sections[md_file.stem] = markdown.markdown(
            md_rendered,
            extensions=["extra", "smarty"]
        )

    # =====================================================
    # Render final HTML page
    # =====================================================

    html = template.render(
        lang=site_cfg["lang"],
        page_title=site_cfg["page_title"],
        hero_intro=site_cfg["hero_intro"],
        hero_subtitle=site_cfg["hero_subtitle"],
        sections=sections,
        year=datetime.now().year,
    )

    # =====================================================
    # Output file (GitHub Pages root)
    # =====================================================

    output_file = Path("index.html") if lang_key == "en" else Path("index_pt.html")
    output_file.write_text(html, encoding="utf-8")

    print(f"✔ Página gerada: {output_file}")

# =========================================================
# BUILD
# =========================================================

render_page("en")
render_page("pt")

print("✅ Site gerado com sucesso")


