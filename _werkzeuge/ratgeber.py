#!/usr/bin/env python3
"""Erzeugt Ratgeberseiten für novaworks-it.de/<produkt>/ratgeber/.

   python3 _werkzeuge/ratgeber.py azubihub
   python3 _werkzeuge/ratgeber.py kontora

Die Inhalte stehen in _werkzeuge/ratgeber_<produkt>.py (Liste SEITEN und Dict PRODUKT).
Ordner mit Unterstrich veröffentlicht GitHub Pages nicht.
"""
import html, importlib.util, json, os, sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
produkt = sys.argv[1]
spec = importlib.util.spec_from_file_location("inhalt", os.path.join(WURZEL, "_werkzeuge", f"ratgeber_{produkt}.py"))
inhalt = importlib.util.module_from_spec(spec); spec.loader.exec_module(inhalt)
P, SEITEN = inhalt.PRODUKT, inhalt.SEITEN
ZIEL = os.path.join(WURZEL, produkt, "ratgeber")
BASIS = f"https://novaworks-it.de/{produkt}/ratgeber/"
STAND = P.get("stand", "Oktober 2026")
DATUM = P.get("datum", "2026-10-21")
e = html.escape


def kopf(titel, beschreibung, url, jsonld, typ="article"):
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(titel)} | {e(P['name'])}</title>
  <meta name="description" content="{e(beschreibung)}">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="../../assets/{P['icon']}">
  <meta name="theme-color" content="{P['paper']}">
  <meta property="og:type" content="{typ}">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="NovaWorks">
  <meta property="og:title" content="{e(titel)}">
  <meta property="og:description" content="{e(beschreibung)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{P['bild']}">
  <link rel="stylesheet" href="../produkt.css">
  <style>:root{{{P['farben']}}}.text a{{color:var(--blue)}}.quellen li{{font-size:.92rem}}.inhalt{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px 20px;margin:24px 0}}.inhalt ol{{margin:6px 0 0;padding-left:20px}}.tipp{{background:var(--soft);border-radius:14px;padding:14px 18px;margin:18px 0}}table.t{{width:100%;border-collapse:collapse;margin:14px 0;font-size:.95rem;background:#fff}}table.t th,table.t td{{border:1px solid var(--line);padding:9px 11px;text-align:left;vertical-align:top}}table.t th{{background:var(--soft)}}.tw{{overflow-x:auto}}.text h1,.text h2{{hyphens:auto;overflow-wrap:break-word}}@media(max-width:560px){{table.t{{font-size:.84rem}}table.t th,table.t td{{padding:7px 8px;hyphens:auto;overflow-wrap:anywhere}}}}.weitere{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;list-style:none;padding:0}}.weitere a{{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;text-decoration:none;font-weight:600}}</style>
  <script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="../"><img src="../../assets/{P['icon']}" alt="" width="34" height="34">{e(P['name'])} <small>Ratgeber</small></a>
    <nav aria-label="{e(P['name'])}"><a href="../">Über {e(P['name'])}</a><a href="./">Alle Ratgeber</a><a class="btn btn-primary" href="{P['cta_url']}">{e(P['cta_kurz'])}</a></nav>
  </div>
</header>
"""


FUSS = f"""<footer><div class="wrap"><span>{e(P['name'])} ist ein Produkt von <a href="../../">NovaWorks</a>, Warburg.</span><nav aria-label="Rechtliches"><a href="../">Über {e(P['name'])}</a><a href="./">Ratgeber</a><a href="../../impressum.html">Impressum</a><a href="../../datenschutz.html">Datenschutz</a></nav></div></footer>
</body>
</html>
"""


def brotkrumen(eintraege):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(eintraege)]}


def seite(s):
    url = BASIS + s["datei"]
    art = {"@context": "https://schema.org", "@type": "Article", "headline": s["titel"], "description": s["beschreibung"],
           "inLanguage": "de", "datePublished": DATUM, "dateModified": DATUM,
           "author": {"@type": "Organization", "name": "NovaWorks", "url": "https://novaworks-it.de/"},
           "publisher": {"@type": "Organization", "name": "NovaWorks", "url": "https://novaworks-it.de/", "logo": {"@type": "ImageObject", "url": "https://novaworks-it.de/icon-512.png"}},
           "image": P["bild"], "mainEntityOfPage": url}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}
    bc = brotkrumen([("NovaWorks", "https://novaworks-it.de/"), (P["name"], f"https://novaworks-it.de/{produkt}/"),
                     ("Ratgeber", BASIS), (s["kurz"], url)])
    o = [kopf(s["titel"], s["beschreibung"], url, [art, faq, bc])]
    o.append('<main id="inhalt" class="wrap text">\n')
    o.append(f'  <p class="klein"><a href="../">{e(P["name"])}</a> › <a href="./">Ratgeber</a> › {e(s["kurz"])}</p>\n')
    o.append(f'  <h1>{e(s["titel"])}</h1>\n  <p class="lead" style="color:var(--muted)">{s["lead"]}</p>\n')
    if s.get("kurzantwort"):
        o.append(f'  <div class="tipp"><strong>Kurz gesagt:</strong> {s["kurzantwort"]}</div>\n')
    if len(s["abschnitte"]) >= 4:
        o.append('  <nav class="inhalt" aria-label="Inhalt"><strong>Inhalt</strong><ol>' +
                 "".join(f'<li><a href="#a{i+1}">{e(t[0])}</a></li>' for i, t in enumerate(s["abschnitte"])) +
                 '<li><a href="#fragen">Häufige Fragen</a></li></ol></nav>\n')
    for i, teil in enumerate(s["abschnitte"]):
        h, absaetze = teil[0], teil[1]
        o.append(f'  <h2 id="a{i+1}">{e(h)}</h2>\n')
        for a in absaetze or []:
            raw = a.lstrip().startswith("<") and not a.lstrip().startswith(("<strong", "<a ", "<em"))
            o.append((f'  <div class="tw">\n{a}  </div>\n' if a.lstrip().startswith("<table") else a) if raw else f"  <p>{a}</p>\n")
        if len(teil) > 2 and teil[2]:
            o.append("  <ul>\n" + "".join(f"    <li>{x}</li>\n" for x in teil[2]) + "  </ul>\n")
    o.append('  <h2 id="fragen">Häufige Fragen</h2>\n')
    for q, a in s["faq"]:
        o.append(f"  <details><summary>{e(q)}</summary><p>{e(a)}</p></details>\n")
    if s.get("passend"):
        o.append(f'  <p class="tipp">Passend dazu: <a href="{s["passend"][1]}">{e(s["passend"][0])}</a></p>\n')
    o.append(f'  <div class="demo-band" style="margin-top:40px"><div><h2>{e(P["band_titel"])}</h2><p>{e(s.get("band_text") or P["band_text"])}</p></div><a class="btn" href="{P["cta_url"]}">{e(P["cta"])} <span aria-hidden="true">→</span></a></div>\n')
    if s.get("quellen"):
        o.append('  <h2>Quellen</h2>\n  <ul class="quellen">\n' + "".join(
            f'    <li><a href="{u}" rel="noopener">{e(t)}</a></li>\n' for t, u in s["quellen"]) + "  </ul>\n")
    if s.get("hinweis"):
        o.append(f'  <p class="hinweis" style="margin-top:24px">{e(s["hinweis"])}</p>\n')
    weitere = [x for x in SEITEN if x is not s]
    o.append('  <h2>Weitere Ratgeber</h2>\n  <ul class="weitere">\n' + "".join(
        f'    <li><a href="{x["datei"]}">{e(x["kurz"])}</a></li>\n' for x in weitere) + "  </ul>\n")
    o.append(f'  <p class="klein">Stand: {STAND} · Von NovaWorks, Warburg</p>\n</main>\n')
    o.append(FUSS)
    return "".join(o)


def uebersicht():
    liste = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": BASIS + s["datei"], "name": s["titel"]} for i, s in enumerate(SEITEN)]}
    bc = brotkrumen([("NovaWorks", "https://novaworks-it.de/"), (P["name"], f"https://novaworks-it.de/{produkt}/"), ("Ratgeber", BASIS)])
    o = [kopf(P["ratgeber_titel"], P["ratgeber_beschreibung"], BASIS, [liste, bc], typ="website")]
    o.append(f'<main id="inhalt" class="wrap text">\n  <p class="klein"><a href="../">{e(P["name"])}</a> › Ratgeber</p>\n  <h1>{e(P["ratgeber_titel"])}</h1>\n')
    o.append(f'  <p class="lead" style="color:var(--muted)">{e(P["ratgeber_lead"])}</p>\n')
    for s in SEITEN:
        o.append(f'  <h2><a href="{s["datei"]}">{e(s["titel"])}</a></h2>\n  <p>{e(s["beschreibung"])}</p>\n')
    o.append(f'  <div class="demo-band" style="margin-top:40px"><div><h2>{e(P["band_titel"])}</h2><p>{e(P["band_text"])}</p></div><a class="btn" href="{P["cta_url"]}">{e(P["cta"])} <span aria-hidden="true">→</span></a></div>\n')
    o.append(f'  <p class="klein">Stand: {STAND}</p>\n</main>\n')
    o.append(FUSS)
    return "".join(o)


os.makedirs(ZIEL, exist_ok=True)
for s in SEITEN:
    open(os.path.join(ZIEL, s["datei"]), "w", encoding="utf-8").write(seite(s))
open(os.path.join(ZIEL, "index.html"), "w", encoding="utf-8").write(uebersicht())
print("\n".join([BASIS] + [BASIS + s["datei"] for s in SEITEN]))
