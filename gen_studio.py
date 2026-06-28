#!/usr/bin/env python3
# nichvs.studio — index + scrape/doc/net. Conteudo incrementado (sem GTM/receita).
import os
OUT="/mnt/user-data/outputs"

GFONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"/>'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>'
'<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet"/>')

NODES=[(50,12),(74,22),(86,47),(82,73),(66,86),(44,89),(23,79),(13,58),(17,33),(33,16)]
def net_nodes():
    return "".join(f'<circle class="net-node pulse" cx="{x}" cy="{y}" r="3" style="animation-delay:{i*.18:.2f}s"/>' for i,(x,y) in enumerate(NODES))

V_MASTER=('<svg class="hero-mark" viewBox="0 0 100 100" aria-hidden="true">'
 '<circle cx="50" cy="48" r="35" class="v-stroke" stroke-width="1" opacity=".28"/>'
 '<path class="v-fill" d="M26 24 L50 76 L74 24 L61 24 L50 54 L39 24 Z"/></svg>')
def logo_small():
    return ('<svg viewBox="0 0 100 100" aria-hidden="true">'
            '<path class="v-fill" d="M26 22 L50 78 L74 22 L61 22 L50 54 L39 22 Z"/></svg>')
IC_SCRAPE=('<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">'
 '<g class="v-fill"><rect x="6" y="27" width="28" height="4"/><rect x="14" y="38" width="24" height="4"/><rect x="22" y="49" width="20" height="4"/></g>'
 '<path class="v-fill" d="M40 22 L62 78 L86 22 L73 22 L62 52 L51 22 Z"/></svg>')
IC_DOC=('<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">'
 '<path class="v-stroke" stroke-width="4" stroke-linejoin="round" d="M26 14 H60 L78 32 V86 H26 Z"/>'
 '<path class="v-stroke" stroke-width="4" stroke-linejoin="round" d="M60 14 V32 H78"/>'
 '<path class="v-fill" d="M38 40 L51 70 L64 40 L57 40 L51 56 L45 40 Z"/></svg>')
IC_NET=('<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">'
 '<path class="v-stroke" stroke-width="1.2" opacity=".8" d="M50 12 L74 22 L86 47 L82 73 L66 86 L44 89 L23 79 L13 58 L17 33 L33 16 Z"/>'
 '<path class="v-stroke" stroke-width="1.2" opacity=".55" d="M50 12 L50 48 M13 58 L50 48 M86 47 L50 48 M66 86 L50 48"/>'
 + net_nodes() +
 '<path class="v-fill" d="M34 30 L50 68 L66 30 L58 30 L50 52 L42 30 Z"/></svg>')
ICONS={"scrape":IC_SCRAPE,"doc":IC_DOC,"net":IC_NET}

def sp(x): return f'<span class="spoiler" title="clique para revelar">{x}</span>'
def dash(cls,title,foot,metrics):
    m="".join(f'<div class="metric"><div class="ml">{l}</div><div class="mv">{v}</div></div>' for l,v in metrics)
    return (f'<div class="dash d-{cls}"><div class="dash-bar"><span class="dot"></span><span class="dot"></span>'
            f'<span class="dot"></span><span class="dt"><b>{title}</b></span></div>'
            f'<div class="dash-body">{m}</div><div class="dash-foot">{foot}</div></div>')

def head(title,desc,body_cls=""):
    return (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"/>'
        f'<meta name="viewport" content="width=device-width, initial-scale=1.0"/>'
        f'<title>{title}</title><meta name="description" content="{desc}"/>'
        f'{GFONTS}<link rel="stylesheet" href="studio.css"/></head><body class="{body_cls}">')

def header():
    return ('<header id="head"><div class="wrap nav">'
        f'<a class="brand" href="index.html" aria-label="NICHVS STUDIO">{logo_small()}'
        '<span class="bt">NICHVS <span>STUDIO</span></span></a>'
        '<nav class="nav-links">'
        '<a href="index.html#paradigma">Paradigma</a>'
        '<a href="index.html#arquitetura">Arquitetura</a>'
        '<a href="index.html#modulos">Módulos</a>'
        '<a href="index.html#telas">Telas</a>'
        '<a href="index.html#consultoria">Consultoria</a>'
        '<a class="nav-cta" href="mailto:contato@nichvs.studio">Contato</a>'
        '</nav></div></header>')

def footer():
    return ('<footer><div class="wrap"><div class="fgrid">'
        '<div class="fcol">'
        f'<a class="brand" href="index.html">{logo_small()}<span class="bt">NICHVS <span>STUDIO</span></span></a>'
        '<p class="fabout">A infraestrutura invisível para operações de alta complexidade. A inteligência em movimento perpétuo.</p></div>'
        '<div class="fcol"><h4>Módulos</h4>'
        '<a href="scrape.html">Scrape · Ingestão</a><a href="doc.html">Doc · Cognição</a><a href="net.html">Net · Orquestração</a></div>'
        '<div class="fcol"><h4>Ecossistema</h4>'
        '<a href="https://culturaflow.netlify.app" target="_blank" rel="noopener">CulturaFlow</a>'
        '<a href="https://nichvs.tech" target="_blank" rel="noopener">Nichvs Tecnologia</a></div>'
        '<div class="fcol"><h4>Contato</h4>'
        '<a href="mailto:contato@nichvs.studio">contato@nichvs.studio</a>'
        '<a href="mailto:contato@nichvs.studio?subject=Novo%20projeto">Iniciar projeto</a></div>'
        '</div><div class="fmeta">'
        '<span>Nichvs Tecnologia ME · Florianópolis/SC</span>'
        '<span class="gold">nichvs.studio · © 2026</span>'
        '</div></div></footer>')

SCRIPT=('<script>(function(){"use strict";'
 'var h=document.getElementById("head");'
 'function s(){if(window.pageYOffset>40){h.classList.add("scrolled");}else{h.classList.remove("scrolled");}}'
 'window.addEventListener("scroll",s,{passive:true});s();'
 'var it=document.querySelectorAll(".reveal");'
 'if("IntersectionObserver" in window){var io=new IntersectionObserver(function(e){for(var i=0;i<e.length;i++){if(e[i].isIntersecting){e[i].target.classList.add("in");io.unobserve(e[i].target);}}},{threshold:.12,rootMargin:"0px 0px -40px 0px"});'
 'for(var j=0;j<it.length;j++){io.observe(it[j]);}}else{for(var k=0;k<it.length;k++){it[k].classList.add("in");}}'
 'var sp=document.querySelectorAll(".spoiler");for(var q=0;q<sp.length;q++){sp[q].addEventListener("click",function(){this.classList.toggle("revealed");});}'
 '})();</script>')

# ---- 4 frentes de forca (home) ----
FRENTES=[
 ("01","Omnisciência de Dados","A ingestão onipresente","Captura ativa e multi-fonte com deduplicação em tempo real. Sistemas legados, APIs complexas e silos de dados são rompidos — a informação flui para o núcleo da corporação antes mesmo que o mercado registre o movimento."),
 ("02","Cognição Sintética Ativa","A transmutação documental","LLM somado a geração aumentada por recuperação (RAG) dá cognição real à máquina. Documentos, contratos e PDFs são dissecados e transmutados em JSON estruturado em milissegundos. O volume que asfixiava a operação vira inteligência pura."),
 ("03","Hiper-Orquestração Autônoma","O fim do atrito","Topologia de sistema nervoso central: roteamento em tempo real e filas de processamento isoladas. A plataforma age antes que um operador precise pensar — cadeias de valor ininterruptas, estruturadas para 24/7 sem degradação."),
 ("04","Soberania Criptográfica","A governança como engenharia","Conformidade como lei inquebrável da estrutura sistêmica, não como departamento reativo. Auditoria imutável de cada mutação de dado e controle de acesso cirúrgico desenhado desde a raiz."),
]

# ---- modulos ----
MODS={
 "scrape":{"cls":"m-scrape","name":"NICHVS STUDIO · SCRAPE","sub":"Módulo de Ingestão e Conectividade","title":"Omni-Captura",
   "tag":"A fronteira está onde nós estamos.",
   "con":["Movimento","Avanço","Penetração"],
   "lead":"A inteligência começa na ingestão — e ela <strong>não espera por integrações passivas.</strong>",
   "detail":["Pensado para operações que dependem de dados de fontes externas e sistemas legados, mas esbarram na lentidão das integrações tradicionais. O Scrape atua como uma força-tarefa de captura: avança ativamente sobre o ambiente externo e rompe APIs complexas, portais e silos de dados.",
             "Com esteiras de captura de alta precisão, ingestão multi-fonte e deduplicação em tempo real, a informação é empurrada para o seu núcleo por meio de webhooks automatizados — eliminando a busca braçal por novos eventos. A matéria-prima chega antes que o mercado registre o movimento."],
   "caps":[("01","Ingestão multi-fonte ativa","APIs abertas (Open Finance), portais e bancos de dados."),
           ("02","Parsers configuráveis","Varredura e extração adaptadas a cada fonte."),
           ("03","Deduplicação em tempo real","Sinal limpo, sem ruído nem redundância."),
           ("04","Webhooks automatizados","Eventos empurrados ao núcleo, sem polling manual.")],
   "chips":["Multi-fonte","Open Finance","Parsers","Dedup","Webhooks"]},
 "doc":{"cls":"m-doc","name":"NICHVS STUDIO · DOC","sub":"Módulo de Cognição e Estruturação","title":"Alquimia Semântica",
   "tag":"O caos estruturado em milissegundos.",
   "con":["Clareza","Inteligência","Precisão Cirúrgica"],
   "lead":"O fim da burocracia analógica. Damos <strong>cognição real à máquina.</strong>",
   "detail":["Pensado para empresas de crédito, escritórios jurídicos e back-offices sufocados por milhares de PDFs, imagens e contratos desestruturados. O Doc lê a massa documental que asfixia a operação.",
             "Funde Large Language Models com geração aumentada por recuperação (RAG) sobre bases de conhecimento restritas. Não apenas escaneia — disseca, interpreta e transmuta texto não estruturado e imagens em JSON limpo em milissegundos, com score de confiança que viabiliza a validação humana antifraude. Um documento entra; classificação, cláusulas extraídas e riscos apontados retornam prontos para uso."],
   "caps":[("01","Extração com LLM + RAG","Bases de conhecimento restritas, contexto controlado."),
           ("02","Transmutação em JSON","Texto e imagens viram dado estruturado."),
           ("03","Score de confiança","Precisão mensurável em cada extração."),
           ("04","Validação antifraude","Cláusulas e riscos apontados para revisão humana.")],
   "chips":["LLM","RAG","OCR","JSON","Confidence score"]},
 "net":{"cls":"m-net","name":"NICHVS STUDIO · NET","sub":"Módulo de Orquestração e Fluxo","title":"Sistema Nervoso Operacional",
   "tag":"A inteligência em movimento perpétuo.",
   "con":["Conectividade","Fluidez","Sistema Nervoso"],
   "lead":"Inteligência sem movimento é inútil. Operamos como um <strong>hub de orquestração contínua.</strong>",
   "detail":["Pensado para operações que já têm os dados estruturados, mas sofrem com falhas de comunicação entre departamentos, perda de timing e ausência de governança no roteamento. O Net é o sistema nervoso central que faz tudo reagir simultaneamente.",
             "Roteamento e processamento assíncrono sobre filas isoladas (arquitetura Redis/BullMQ), disparando gatilhos, alertas e orquestrando etapas de validação. Recebe eventos de múltiplos sistemas e garante a regra de negócio de ponta a ponta, 24/7, sem degradar o banco principal — com controle de acesso por papéis (RBAC) e auditoria imutável de cada ação."],
   "caps":[("01","Roteamento assíncrono","Filas isoladas, latência mínima, 24/7."),
           ("02","Malha de gatilhos","Alertas e etapas de validação orquestradas."),
           ("03","RBAC","Controle de acesso por papéis, desde a raiz."),
           ("04","Auditoria imutável","Trilha completa de cada mutação sistêmica.")],
   "chips":["Async","Redis / BullMQ","Webhooks","RBAC","Auditoria"]},
}
ORDER=["scrape","doc","net"]

def build_index():
    fr="".join(f'<div class="front reveal"><div class="fn">{n}</div><h3>{t}</h3><div class="fsub">{s}</div><p>{p}</p></div>' for n,t,s,p in FRENTES)
    mods=""
    for k in ORDER:
        m=MODS[k]; ic=ICONS[k].format(cls="mod-ico"); con=" · ".join(m["con"])
        mods+=(f'<a class="mod {m["cls"]} reveal" href="{k}.html">{ic}'
            f'<div class="mod-name">{m["name"]}</div><h3>{m["title"]}</h3>'
            f'<div class="mtag">“{m["tag"]}”</div><div class="mcon">{m["sub"]}</div>'
            f'<span class="go">Explorar módulo <span class="arw">&rarr;</span></span></a>')
    return (head("NICHVS STUDIO — A inteligência em movimento perpétuo",
                 "NICHVS STUDIO — A infraestrutura invisível para operações de alta complexidade. Arquitetura composable: Scrape, Doc e Net. Ingestão, cognição e orquestração com governança.")
        + header()
        + '<main id="top">'
        + '<section class="hero"><div class="hero-glow"></div>'
        + '<svg class="hero-frame" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0 6 V0 H6 M94 0 H100 V6 M100 94 V100 H94 M6 100 H0 V94" fill="none" stroke="currentColor" stroke-width=".4"/></svg>'
        + '<div class="wrap"><div class="hero-inner">' + V_MASTER
        + '<h1>NICHVS <span class="b2">STUDIO</span></h1>'
        + '<div class="hero-sub">Sistema de Identidade Modular · Engenharia de Alta Precisão</div>'
        + '<p class="hero-tag">“A inteligência em movimento perpétuo.”</p>'
        + '<div class="hero-actions"><a class="btn btn-primary" href="#modulos">Ver os módulos <span class="arw">&rarr;</span></a>'
        + '<a class="btn btn-ghost" href="#arquitetura">A arquitetura</a></div>'
        + '</div></div></section>'
        # paradigma
        + '<section class="sec" id="paradigma"><div class="wrap">'
        + '<div class="sec-label reveal">A Quebra do Paradigma</div>'
        + '<div class="para-grid"><div class="ptext reveal">'
        + '<h2>O fim do software legado.</h2>'
        + '<p>O mercado corporativo atingiu o limite da força bruta. Empilhar sistemas, comprar licenças e contratar exércitos para transitar dados entre planilhas não é mais crescimento — <strong>é obsolescência programada.</strong></p>'
        + '<p>A disrupção real não nasce de mais um aplicativo, mas de <strong>reescrever as leis da física da sua operação:</strong> tornar a complexidade invisível e a execução instantânea.</p>'
        + '</div><ul class="concept-list reveal">'
        + '<li><span class="n">01</span> Brutalismo Minimalista</li>'
        + '<li><span class="n">02</span> Ponta de Lança</li>'
        + '<li><span class="n">03</span> Precisão <span class="sm">Space Mono</span></li>'
        + '</ul></div></div></section>'
        # arquitetura / singularidade
        + '<section class="sec" id="arquitetura"><div class="wrap">'
        + '<div class="sec-label reveal">A Singularidade Operacional</div>'
        + '<h2 class="reveal" style="margin-bottom:14px">A nossa arquitetura.</h2>'
        + '<p class="reveal" style="color:var(--muted);font-weight:300;max-width:62ch;margin-bottom:36px">Não é uma ferramenta. É uma camada fundacional de hiperescalabilidade — assíncrona, agnóstica e implacável — que engole o caos de qualquer ecossistema e devolve previsibilidade absoluta, através de quatro frentes de força.</p>'
        + f'<div class="fronts">{fr}</div></div></section>'
        # modulos
        + '<section class="sec" id="modulos"><div class="wrap">'
        + '<div class="sec-label reveal">Os Módulos</div>'
        + '<h2 class="reveal" style="margin-bottom:30px">Arquitetura composable.</h2>'
        + '<div class="composable reveal"><span class="ctag">Composable</span>'
        + '<p>Uma plataforma desacoplada e assíncrona, desenhada para resolver gargalos de dados, cognição e fluxo. <b>Adote o módulo que resolve o seu limite atual; escale para o ecossistema completo quando estiver pronto.</b></p></div>'
        + f'<div class="mods">{mods}</div>'
        + '</div></section>'
        # telas & dashboards
        + '<section class="sec" id="telas"><div class="wrap">'
        + '<div class="sec-label reveal">Em Operação · Telas & Dashboards</div>'
        + '<h2 class="reveal" style="margin-bottom:10px">As interfaces dos módulos.</h2>'
        + '<p class="reveal" style="color:var(--muted);font-weight:300;max-width:60ch;margin-bottom:14px">Formatação e estrutura expostas; os dados de negócio ficam em spoiler.</p>'
        + '<div class="spoiler-note reveal">⌐ Dados sensíveis borrados · clique em qualquer valor para revelar</div>'
        + '<div class="telas reveal">'
        + dash("scrape","Scrape · Queue Monitor v2.1","2 workers paralelos · deadletter DLQ monitorado · webhooks ativos",[("Jobs ativos",sp("15")),("Aguardando",sp("32")),("Workers","3"),("Falhas",sp("2"))])
        + dash("doc","Doc · Cognitive Transmutation Hub","Documento → JSON estruturado · score de confiança por campo · validação humana",[("Docs/min",sp("xx")),("Confiança",sp("xx%")),("Campos",sp("xx")),("Status","ATIVO")])
        + dash("net","Net · Orchestration Monitor","Roteamento assíncrono · filas isoladas · RBAC + auditoria imutável",[("Eventos/s",sp("xxx")),("Filas","4"),("Latência",sp("xx ms")),("Uptime","99.9%")])
        + '</div></div></section>'
        # consultoria
        + '<section class="sec" id="consultoria"><div class="wrap">'
        + '<div class="sec-label reveal">Serviço Consultivo</div>'
        + '<h2 class="reveal" style="margin-bottom:10px">Modelagem da Jornada.</h2>'
        + '<p class="reveal" style="color:var(--muted);font-weight:300;max-width:64ch;margin-bottom:26px">Desenhamos, com método, a jornada da sua organização da operação atual até a Inteligência Infraestrutural — onde a complexidade fica invisível e a execução, instantânea.</p>'
        + '<div class="method reveal"><div class="mt">Compromisso de método</div>'
        + '<p>Todo o processo de consultoria é conduzido sob as <b>melhores práticas, metodologias e frameworks globais</b> de governança, segurança, dados, engenharia ágil, DevOps e IA — adaptados à realidade regulatória brasileira.</p>'
        + '<div class="fwchips">' + "".join(f'<span class="fwchip on">{c}</span>' for c in ["COBIT","ISO 27001","NIST CSF","DORA","DAMA","MLOps","DevSecOps","SAFe","Scrum/Kanban","Responsible AI","Open Finance"]) + '</div></div>'
        + '<div class="sec-label reveal" style="margin-top:36px">Dois modelos consultivos de referência</div>'
        + '<div class="models reveal">'
        + '<div class="model fin"><div class="mk">Modelo A · Financeiro</div><h4>Ecossistema Red</h4>'
        + '<p>Correspondente bancário, Open Finance e bancarização. Esteira de consignado/portabilidade, melhor oferta e radar regulatório.</p>'
        + '<div class="mrow"><span>Domínio</span><b>Serviços financeiros</b></div>'
        + '<div class="mrow"><span>Módulos</span><b>Scrape · Doc · Match · Net</b></div>'
        + f'<div class="mrow"><span>Ticket / metas</span><b>{sp("dados em spoiler")}</b></div>'
        + '<div class="mrow"><span>Regulatório</span><b>BACEN · SUSEP · LGPD</b></div></div>'
        + '<div class="model oss"><div class="mk">Modelo B · Terceiro Setor</div><h4>Instituto IDEAS</h4>'
        + '<p>Organização social de saúde (OSS). Prestação de contas auditável, editais &amp; orçamento, finanças &amp; pessoas multi-contrato.</p>'
        + '<div class="mrow"><span>Domínio</span><b>Saúde · OSS</b></div>'
        + '<div class="mrow"><span>Núcleos</span><b>Contas · Editais · Finanças · Desk</b></div>'
        + f'<div class="mrow"><span>Volumes / contratos</span><b>{sp("dados em spoiler")}</b></div>'
        + '<div class="mrow"><span>Regulatório</span><b>TCE/TCU · MROSC · ONA</b></div></div>'
        + '</div></div></section>'
        # promessa
        + '<section class="promise"><div class="wrap">'
        + '<div class="sec-label reveal">A Promessa</div>'
        + '<h2 class="big reveal"><span class="l1">O fim do software legado.</span><br><span class="l2">O início da inteligência infraestrutural.</span></h2>'
        + '<p class="sub reveal">A infraestrutura não deve apenas suportar o seu negócio — deve ser a vantagem que torna a operação da concorrência irrelevante.</p>'
        + '<a class="btn btn-primary reveal" href="mailto:contato@nichvs.studio">Falar com a engenharia <span class="arw">&rarr;</span></a>'
        + '</div></section>'
        + '</main>' + footer() + SCRIPT + '</body></html>')

def build_module(key):
    m=MODS[key]; ic=ICONS[key].format(cls="mhero-ico")
    con="".join(f'<span>{c}</span>' for c in m["con"])
    detail="".join(f'<p>{p}</p>' for p in m["detail"])
    caps="".join(f'<li><span class="ci">{n}</span><div><b>{t}</b><span>{d}</span></div></li>' for n,t,d in m["caps"])
    chips="".join(f'<span class="chip">{c}</span>' for c in m["chips"])
    others=[k for k in ORDER if k!=key]; xc=""
    for k in others:
        mm=MODS[k]
        xc+=(f'<a class="xcard {mm["cls"]}" href="{k}.html"><div><div class="xl">{mm["name"]}</div>'
             f'<div class="xt">{mm["title"]}</div></div><span class="arw">&rarr;</span></a>')
    xc+=('<a class="xcard" href="index.html#modulos"><div><div class="xl">Sistema completo</div>'
         '<div class="xt">Todos os módulos</div></div><span class="arw">&rarr;</span></a>')
    return (head(f'{m["name"]} — {m["title"]} | NICHVS STUDIO', f'{m["name"]} · {m["sub"]}. {m["tag"]}', body_cls=f'mod-{key}')
        + header()
        + '<main id="top"><div class="wrap">'
        + f'<div class="crumb"><a href="index.html">NICHVS STUDIO</a><span class="sep">/</span>{m["title"]}</div>'
        + '<section class="mhero">' + ic
        + f'<div class="mname">{m["name"]} · {m["sub"]}</div>'
        + f'<h1>{m["title"]}</h1><p class="mtagline">“{m["tag"]}”</p>'
        + f'<div class="mcon">{con}</div></section>'
        + '<section class="mbody">'
        + f'<div class="lead reveal">{m["lead"]}<div class="chips">{chips}</div></div>'
        + f'<div class="detail reveal">{detail}</div></section>'
        + '<section class="reveal"><ul class="caps">' + caps + '</ul></section>'
        + '</div>'
        + '<section class="xnav"><div class="wrap"><div class="sec-label">Continuar no sistema</div>'
        + f'<div class="xrow">{xc}</div></div></section>'
        + '<section class="promise"><div class="wrap">'
        + '<h2 class="big"><span class="l2">Pronto para mover?</span></h2>'
        + '<p class="sub">Conecte este módulo à sua operação. A engenharia começa numa conversa.</p>'
        + f'<a class="btn btn-primary" href="mailto:contato@nichvs.studio?subject={m["name"].replace(" ","%20")}">Falar com a engenharia <span class="arw">&rarr;</span></a>'
        + '</div></section></main>' + footer() + SCRIPT + '</body></html>')

files={"index.html":build_index(),"scrape.html":build_module("scrape"),
       "doc.html":build_module("doc"),"net.html":build_module("net")}
for n,h in files.items():
    open(os.path.join(OUT,n),"w",encoding="utf-8").write(h)
    print(f"escrito {n} ({len(h)} bytes)")
print("OK")
