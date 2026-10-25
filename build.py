"""Build the dependency-free static draft. No network, secrets or deployment."""
from pathlib import Path
import html, json
ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))
def e(value): return html.escape(str(value), quote=True)
def block(kind, value):
    if kind == "p": return "<p>" + e(value) + "</p>"
    if kind == "callout": return '<div class="scope-note"><p>' + e(value) + '</p></div>'
    if kind == "placeholder": return '<p class="placeholder">' + e(value) + '</p>'
    if kind == "fields": return '<dl class="identity">' + ''.join('<div><dt>'+e(k)+'</dt><dd class="placeholder">'+e(v)+'</dd></div>' for k,v in value) + '</dl>'
    if kind == "table":
        return '<div class="table-wrap"><table><thead><tr>' + ''.join('<th scope="col">'+e(v)+'</th>' for v in value[0]) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+e(v)+'</td>' for v in row)+'</tr>' for row in value[1:]) + '</tbody></table></div>'
    raise ValueError(kind)
for locale, d in DATA.items():
    prefix = "" if locale == "hu" else "../"
    path = ROOT / "dist" / ("index.html" if locale == "hu" else locale + "/index.html")
    path.parent.mkdir(parents=True, exist_ok=True)
    language_links = []
    for code,label in [("hu","Magyar"),("en","English"),("de","Deutsch")]:
        href = prefix + ("index.html" if code == "hu" else code + "/index.html")
        current = ' aria-current="page"' if code == locale else ''
        language_links.append('<a lang="'+code+'" hreflang="'+code+'" href="'+href+'"'+current+'>'+label+'</a>')
    toc = '<ol>'+''.join('<li><a href="#'+e(key)+'">'+e(title)+'</a></li>' for key,title,_ in d['sections'])+'</ol>'
    sections = ''.join('<section id="'+e(key)+'" aria-labelledby="'+e(key)+'-title"><h2 id="'+e(key)+'-title"><span aria-hidden="true">'+str(i+1).zfill(2)+'</span>'+e(title)+'</h2>'+''.join(block(k,v) for k,v in body)+'</section>' for i,(key,title,body) in enumerate(d['sections']))
    document = '<!doctype html>\n<html lang="'+locale+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="referrer" content="no-referrer"><meta name="description" content="'+e(d['intro'])+'"><title>ArcherFW · '+e(d['title'])+' · '+e(d['draft'])+'</title><link rel="stylesheet" href="'+prefix+'assets/privacy.css"></head><body id="top"><a class="skip" href="#main">'+e(d['skip'])+'</a><header class="site-header"><a class="brand" href="'+prefix+'index.html"><span class="brand-mark" aria-hidden="true">AF</span><span>ArcherFW<small>'+e(d['label'])+'</small></span></a><nav class="languages" aria-label="Language">'+''.join(language_links)+'</nav></header><main id="main"><div class="hero"><p class="eyebrow">ARCHERFW / '+e(d['label']).upper()+'</p><h1>'+e(d['title'])+'</h1><p class="intro">'+e(d['intro'])+'</p><p class="version">'+e(d['updated'])+'<span>·</span>'+e(d['effective'])+'</p></div><div class="draft-notice" role="note"><strong>'+e(d['draft'])+'</strong><p>'+e(d['warning'])+'</p></div><div class="reading-layout"><article><details class="mobile-toc"><summary>'+e(d['contents'])+'</summary>'+toc+'</details>'+sections+'<div class="provider-links"><a href="https://unity.com/legal/privacy-policy" target="_blank" rel="noopener noreferrer">'+e(d['sourceLabel'])+' <span aria-hidden="true">↗</span></a><a href="https://player-account.unity.com/" target="_blank" rel="noopener noreferrer">'+e(d['accountLabel'])+' <span aria-hidden="true">↗</span></a></div></article><aside><nav class="toc" aria-label="'+e(d['contents'])+'"><p>'+e(d['contents'])+'</p>'+toc+'<div class="margin-note">'+e(d['placeholders'])+'</div></nav></aside></div></main><footer><p>'+e(d['note'])+'</p><a href="#top">'+e(d['back'])+' ↑</a></footer></body></html>\n'
    path.write_text(document, encoding="utf-8")
print("Built 3 static pages from content.json; no dependencies or network calls.")
