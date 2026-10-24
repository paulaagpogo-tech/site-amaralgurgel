import sys, html, os
sys.path.insert(0, os.path.dirname(__file__))
from conteudo import GUIAS

OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/guias/out"
os.makedirs(OUT, exist_ok=True)

CSS = """:root{--paper:#F6F3EE;--paper-2:#EEE8DF;--white:#FFFDF9;--ink:#151210;--ink-2:#4B443E;--line:#DCD3C7;--copper:#9A5530;--copper-hi:#D49A6A;--sheen:linear-gradient(90deg,#7A3F22,#C68558 45%,#E3B58C 55%,#9A5530);--night:#1C1714;--night-2:#27201C;--on-night:#F3EDE5;--on-night-2:#BDB0A3;--line-night:rgba(243,237,229,.16);--f-display:"Libre Caslon Display","Libre Caslon Text",Georgia,serif;--f-serif:"Libre Caslon Text",Georgia,serif;--f-body:"Hanken Grotesk","Helvetica Neue",Arial,sans-serif;color-scheme:light}
*{box-sizing:border-box}
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--f-body);font-size:18px;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:inherit}
:focus-visible{outline:2px solid var(--copper);outline-offset:3px}
.wrap{max-width:1180px;margin-inline:auto;padding-inline:clamp(18px,4.5vw,48px)}
.read{max-width:720px}
h1,h2,h3{margin:0;font-weight:400;text-wrap:balance}
h1{font-family:var(--f-display);font-size:clamp(38px,5.4vw,64px);line-height:1.06}
h2{font-family:var(--f-serif);font-size:clamp(24px,2.6vw,30px);line-height:1.2;margin-bottom:16px}
p{margin:0}
p+p{margin-top:14px}
.label{font-size:12.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--copper)}
.top{background:var(--night);color:var(--on-night);border-bottom:1px solid var(--line-night)}
.top .wrap{display:flex;justify-content:space-between;align-items:center;gap:16px;padding-block:14px}
.brand{text-decoration:none;font-family:var(--f-serif);font-size:18px}
.brand small{display:block;font-family:var(--f-body);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--on-night-2);margin-top:3px}
.back{font-size:14.5px;color:var(--on-night-2);text-decoration:none}
.back:hover{color:var(--on-night)}
.hero{background:var(--night);color:var(--on-night);position:relative}
.hero::after{content:"";position:absolute;inset:auto 0 0 0;height:1px;background:var(--sheen)}
.hero .wrap{padding-block:clamp(48px,8vw,96px) clamp(44px,7vw,80px)}
.hero .label{color:var(--copper-hi)}
.hero h1{margin-top:18px}
.hero .lead{margin-top:22px;font-size:clamp(18px,1.6vw,20px);color:var(--on-night-2);max-width:60ch}
main .wrap{display:grid;grid-template-columns:minmax(0,720px) minmax(0,1fr);gap:clamp(32px,6vw,88px);padding-block:clamp(48px,7vw,88px)}
article section{padding-block:28px;border-top:1px solid var(--line)}
article section:first-child{border-top:0;padding-top:0}
article ul{margin:0;padding:0;list-style:none;display:grid;gap:10px}
article li{position:relative;padding-left:22px}
article li::before{content:"";position:absolute;left:0;top:.8em;width:10px;height:1px;background:var(--copper)}
.box{background:var(--white);border:1px solid var(--line);padding:24px 26px}
.box ul{gap:8px}
.box li{padding-left:28px}
.box li::before{width:14px;height:14px;top:.38em;border:1px solid var(--copper);background:none}
details{border-bottom:1px solid var(--line)}
details:first-of-type{border-top:1px solid var(--ink)}
summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:20px;padding:18px 0;font-family:var(--f-serif);font-size:19px;line-height:1.35}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-family:var(--f-body);color:var(--copper);font-size:22px;line-height:1;transition:transform .2s}
details[open] summary::after{transform:rotate(45deg)}
details p{padding-bottom:20px;color:var(--ink-2);font-size:17px}
aside{align-self:start;position:sticky;top:24px;display:grid;gap:20px}
.cta{background:var(--night);color:var(--on-night);padding:26px;position:relative}
.cta::before{content:"";position:absolute;inset:0 0 auto 0;height:2px;background:var(--sheen)}
.cta h3{font-family:var(--f-serif);font-size:22px;line-height:1.25;margin-bottom:10px}
.cta p{color:var(--on-night-2);font-size:15.5px;line-height:1.55}
.btn{display:flex;align-items:center;justify-content:center;gap:9px;margin-top:16px;font:600 15px/1 var(--f-body);text-decoration:none;border-radius:2px;padding:15px 18px;background:var(--copper);color:#FFF8F1}
.btn:hover{background:#7F4424}
.btn.wa{background:#1DAA61;color:#FFFFFF;margin-top:10px}
.btn.wa:hover{background:#168A4E}
.btn.line{background:transparent;border:1px solid var(--line-night);color:var(--on-night);margin-top:10px}
.btn.line:hover{border-color:var(--copper-hi)}
.btn svg{width:16px;height:16px}
.others{border-top:1px solid var(--ink);padding-top:14px}
.others p{font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--copper);margin-bottom:8px}
.others a{display:block;padding:7px 0;border-bottom:1px solid var(--line);text-decoration:none;font-size:15.5px}
.others a:hover{color:var(--copper)}
footer{background:var(--night);color:var(--on-night-2);font-size:13px;line-height:1.6;padding-block:30px 40px}
footer b{color:var(--on-night);font-family:var(--f-serif);font-weight:400;font-size:14px}
footer p+p{margin-top:8px}
@media (max-width:900px){main .wrap{grid-template-columns:1fr}aside{position:static}}
@media (max-width:640px){body{font-size:17px}.back span{display:none}.box{padding:20px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'

def body_of(content):
    if isinstance(content, list):
        return "<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in content) + "</ul>"
    return content

def page(g):
    secs = "".join(f'<section><h2>{html.escape(t)}</h2>{body_of(c)}</section>' for t, c in g["secoes"])
    guardar = '<section><h2>O que guardar</h2><div class="box"><ul>' + "".join(f"<li>{html.escape(x)}</li>" for x in g["guardar"]) + "</ul></div></section>"
    faq = '<section><h2>Perguntas comuns</h2>' + "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in g["faq"]) + "</section>"
    outros = "".join(f'<a href="guia-{o["slug"]}.html">{html.escape(o["titulo"])}</a>' for o in GUIAS if o["slug"] != g["slug"])
    wa_text = f"Olá, Dra. Paula. Li o guia sobre {g['titulo'].lower()} no site e gostaria de uma análise do meu caso."
    import urllib.parse
    wa = "https://wa.me/5551992150331?text=" + urllib.parse.quote(wa_text)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(g['titulo'])} · Guia · Paula do Amaral Gurgel Advocacia</title>
<meta name="description" content="{html.escape(g['lead'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="guia.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="./">Paula do Amaral Gurgel<small>Advocacia · OAB/RS 83.847</small></a>
  <a class="back" href="./#guias">← <span>Todos os guias</span></a>
</div></header>
<div class="hero"><div class="wrap">
  <p class="label">Guia informativo</p>
  <h1>{html.escape(g['titulo'])}</h1>
  <p class="lead">{html.escape(g['lead'])}</p>
</div></div>
<main><div class="wrap">
  <article class="read">{secs}{guardar}{faq}</article>
  <aside>
    <div class="cta">
      <h3>Quer que o seu caso seja analisado?</h3>
      <p>Responda à triagem do caso em menos de um minuto. Um de nossos advogados irá lhe atender.</p>
      <a class="btn" href="./#triagem">Fazer a triagem do caso</a>
    </div>
    <nav class="others" aria-label="Outros guias"><p>Outros guias</p>{outros}</nav>
  </aside>
</div></main>
<footer><div class="wrap">
  <p><b>Paula do Amaral Gurgel</b> · Advogada · OAB/RS 83.847</p>
  <p>Conteúdo de caráter exclusivamente informativo e educativo. Não substitui a análise individual do caso e não constitui promessa de resultado.</p>
</div></footer>
</body>
</html>
"""

open(os.path.join(OUT, "guia.css"), "w").write(CSS)
for g in GUIAS:
    open(os.path.join(OUT, f"guia-{g['slug']}.html"), "w").write(page(g))
print(len(GUIAS), "guias em", OUT)
