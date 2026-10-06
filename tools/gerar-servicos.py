#!/usr/bin/env python3
"""Gera /servicos/ e as páginas de cada serviço a partir de SERVICOS.

Rode na raiz do site: python3 tools/gerar-servicos.py
Edite a copy aqui, não nos HTML gerados. O sprite de ícones vem do index.html.
"""
import html
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://duckflow.com.br/'
WHATSAPP = '5554984384244'
ASSET_VERSION = '20260930a'

SERVICOS = [
    {
        'slug': 'automacao-com-ia',
        'nome': 'Automação com IA',
        'icone': 'icon-workflow',
        'area': 'Operação',
        'title': 'Automação com IA para empresas | Duck Flow',
        'description': 'Automação com IA para tirar da equipe tarefas repetidas, como triagem, atualização de status e relatórios. Preço fechado por projeto. Canela, Gramado e todo o Brasil.',
        'h1': 'Automação com IA<br><em>para a rotina da empresa</em>',
        'lede': 'Se a equipe passa horas copiando dados entre sistemas, conferindo status e cobrando o próximo passo, desenhamos um fluxo que executa essas etapas e chama uma pessoa quando é preciso decidir.',
        'resumo': 'Tarefas repetidas viram um fluxo que roda sozinho, com validação humana nas etapas que exigem decisão.',
        'tags': ['Triagem', 'Status', 'Relatórios'],
        'sinais': [
            ('A mesma planilha, toda semana.', 'Alguém junta números de várias ferramentas para montar o mesmo relatório.'),
            ('O pedido chega e espera alguém.', 'E-mails, anexos e solicitações ficam parados até uma pessoa ler e redistribuir.'),
            ('Em que pé isso está?', 'Para saber o status de um pedido ou projeto, é preciso perguntar para alguém.'),
        ],
        'entregas': [
            ('Mapa do processo', 'Registramos como a tarefa acontece hoje, quem participa e onde ela trava, antes de automatizar qualquer etapa.'),
            ('Fluxo automatizado', 'Conectamos as ferramentas que você já usa e colocamos IA nas etapas que exigem ler, classificar ou resumir.'),
            ('Validação humana', 'Definimos em que pontos o fluxo pede aprovação, para que as decisões importantes continuem com a equipe.'),
            ('Documentação e treinamento', 'O fluxo fica documentado na sua infraestrutura e a equipe aprende a operar e ajustar.'),
        ],
        'aplicacoes_titulo': 'Onde a automação com IA costuma entrar',
        'aplicacoes': ['Triagem de e-mails e pedidos', 'Extração de dados de documentos', 'Atualização de status entre sistemas', 'Relatórios recorrentes enviados no horário', 'Avisos quando algo sai do padrão', 'Cadastro de clientes e pedidos'],
        'faq': [
            ('Que ferramentas vocês usam para automatizar?', 'Escolhemos depois de entender o processo. Integramos as ferramentas que sua empresa já usa, e a proposta indica qualquer ferramenta nova e o custo dela.'),
            ('E se a IA errar?', 'As etapas em que um erro custa caro passam por validação humana. Antes da entrada em produção, testamos o fluxo com casos reais da sua operação.'),
            ('Quanto custa uma automação?', 'O preço é fechado por projeto e depende do escopo. Ele vem na proposta, depois da sessão gratuita de 30 minutos.'),
        ],
    },
    {
        'slug': 'estruturacao-de-dados',
        'nome': 'Estruturação de dados',
        'icone': 'icon-database',
        'area': 'Dados',
        'title': 'Estruturação de dados e dashboards com IA | Duck Flow',
        'description': 'Organizamos os dados da empresa em uma fonte confiável, com dashboards automáticos, avisos e um segundo cérebro com IA. Preço fechado por projeto, em todo o Brasil.',
        'h1': 'Estruturação de dados<br><em>para decidir com um número só</em>',
        'lede': 'Quando cada ferramenta mostra uma versão da operação, juntar os números vira trabalho manual. Organizamos as informações em uma fonte confiável, com dashboards que se atualizam sozinhos e avisos para o que precisa de atenção.',
        'resumo': 'Uma fonte confiável para os números da empresa, com dashboards, avisos e um segundo cérebro com IA.',
        'tags': ['Fonte única', 'Dashboards', 'Avisos'],
        'sinais': [
            ('Qual número está certo?', 'CRM, planilha e financeiro não batem, e alguém precisa conferir antes de cada decisão.'),
            ('O conhecimento está espalhado.', 'Processos, contratos e respostas prontas vivem em pastas, conversas e na memória das pessoas.'),
            ('O problema aparece tarde.', 'Um atraso ou uma queda só é notado quando alguém abre a planilha.'),
        ],
        'entregas': [
            ('Fonte única de dados', 'Definimos de onde vem cada número e reunimos as informações em uma base que o time consulta com confiança.'),
            ('Dashboards automáticos', 'Painéis com os indicadores que a gestão acompanha, atualizados sem ninguém exportar planilha.'),
            ('Avisos', 'Alertas por e-mail ou WhatsApp quando um indicador sai do esperado.'),
            ('Segundo cérebro com IA', 'Uma base com os documentos e processos da empresa, ou os seus, que a IA consulta para responder com as suas informações.'),
        ],
        'aplicacoes_titulo': 'O que costuma entrar em um projeto de dados',
        'aplicacoes': ['Painel comercial com dados do CRM', 'Fechamento financeiro sem planilha manual', 'Base de conhecimento para o atendimento', 'Indicadores da operação por unidade', 'Alertas de prazo, estoque ou inadimplência', 'Busca em documentos internos com IA'],
        'faq': [
            ('Preciso ter os dados organizados para começar?', 'Não. Entender e organizar os dados necessários pode fazer parte do projeto. A sessão inicial ajuda a identificar o que já existe e o que falta.'),
            ('Onde os dados ficam guardados?', 'Na infraestrutura da sua empresa. A proposta informa quais ferramentas guardam cada dado e quem tem acesso.'),
            ('O que é um segundo cérebro empresarial?', 'É uma base com os documentos, processos e respostas da empresa, organizada para que a IA encontre a informação e responda com base nela. Serve para atendimento, integração de novos funcionários e consulta interna.'),
        ],
    },
    {
        'slug': 'agentes-de-ia',
        'nome': 'Agentes de IA sob medida',
        'icone': 'icon-bot',
        'area': 'Inteligência',
        'title': 'Agentes de IA sob medida para empresas | Duck Flow',
        'description': 'Agentes de IA com as regras, fontes e limites do seu negócio para atendimento, triagem e suporte interno, inclusive no WhatsApp. Canela, Gramado e todo o Brasil.',
        'h1': 'Agentes de IA<br><em>com as regras do seu negócio</em>',
        'lede': 'Se as mesmas perguntas e solicitações ocupam a equipe todos os dias, criamos agentes que respondem com as informações da empresa, respeitam os limites que você definir e passam a conversa para uma pessoa quando o assunto pede.',
        'resumo': 'Agentes que atendem, fazem triagem e dão suporte com as regras, fontes e limites da sua empresa.',
        'tags': ['Atendimento', 'Triagem', 'Suporte'],
        'sinais': [
            ('As mesmas perguntas, o dia inteiro.', 'Preço, prazo, horário e status tomam o tempo de quem deveria cuidar dos casos difíceis.'),
            ('Mensagem fora do horário.', 'O cliente escreve à noite ou no fim de semana e só recebe resposta no dia seguinte.'),
            ('Como é que se faz isso mesmo?', 'A equipe interrompe colegas para descobrir um procedimento interno.'),
        ],
        'entregas': [
            ('Regras do agente', 'Definimos com você o que o agente responde, o que ele não faz e o tom que usa com o cliente.'),
            ('Conexão com as suas fontes', 'O agente consulta documentos, catálogo, agenda ou CRM para responder com informação atual.'),
            ('Passagem para uma pessoa', 'Quando a conversa sai do escopo, o agente transfere para a pessoa certa com o histórico junto.'),
            ('Acompanhamento', 'Revisamos as conversas e ajustamos as respostas conforme aparecem casos novos.'),
        ],
        'aplicacoes_titulo': 'Onde um agente de IA costuma entrar',
        'aplicacoes': ['Recepção e atendimento no WhatsApp', 'Agendamento e confirmação de horários', 'Triagem de solicitações e chamados', 'Suporte interno para a equipe', 'Consulta a processos e documentos', 'Primeira qualificação de leads'],
        'faq': [
            ('O agente pode atender no WhatsApp?', 'Pode. O agente pode atender no WhatsApp, no site ou em canais internos. O canal entra na proposta, junto com as regras de atendimento.'),
            ('E se o agente não souber responder?', 'Ele avisa o cliente e transfere a conversa para uma pessoa. Esse limite é definido e testado antes da entrada em produção.'),
            ('Qual a diferença para um chatbot de menu?', 'O chatbot de menu segue um roteiro fixo de opções. O agente entende a pergunta do jeito que o cliente escreveu, consulta as informações da empresa e segue as regras definidas com você.'),
        ],
    },
    {
        'slug': 'ia-para-vendas',
        'nome': 'IA para geração de leads e vendas',
        'icone': 'icon-trend',
        'area': 'Comercial',
        'title': 'IA para geração de leads e vendas | Duck Flow',
        'description': 'Prospecção, qualificação, registro no CRM e follow-up com IA para nenhum lead ficar sem retorno. Projetos com preço fechado para empresas B2B em todo o Brasil.',
        'h1': 'IA para geração<br>de leads <em>e vendas</em>',
        'lede': 'O lead não deveria depender da memória de alguém para receber retorno. Montamos prospecção, qualificação, registro no CRM e follow-up para o time comercial agir com contexto e na hora certa.',
        'resumo': 'Prospecção, qualificação, CRM e follow-up conectados para o comercial agir com contexto.',
        'tags': ['Prospecção', 'CRM', 'Follow-up'],
        'sinais': [
            ('O lead chegou. E depois?', 'Sem um próximo passo claro, o contato esfria entre uma ferramenta e outra.'),
            ('O CRM está atrasado.', 'O vendedor registra quando lembra, e a gestão não sabe o que está de fato no funil.'),
            ('Prospectar fica para depois.', 'Buscar e pesquisar contatos novos só acontece quando sobra tempo na agenda.'),
        ],
        'entregas': [
            ('Prospecção e enriquecimento', 'Listas de contatos no perfil do seu cliente, com dados da empresa para o vendedor chegar preparado.'),
            ('Qualificação e prioridade', 'A IA classifica os leads que chegam e indica quais atender primeiro.'),
            ('CRM atualizado', 'Conversas, e-mails e mudanças de etapa entram no CRM sem o vendedor digitar tudo.'),
            ('Follow-up na hora certa', 'Lembretes e mensagens de acompanhamento para nenhum contato ficar sem retorno.'),
        ],
        'aplicacoes_titulo': 'Onde a IA entra no comercial',
        'aplicacoes': ['Resposta rápida a leads do site e do WhatsApp', 'Enriquecimento de contatos com dados públicos', 'Priorização de leads por perfil', 'Registro automático de conversas no CRM', 'Cadência de follow-up', 'Resumo semanal do funil'],
        'faq': [
            ('Preciso trocar o CRM que usamos?', 'O primeiro passo é entender o que você já usa. A proposta deixa claro quais ferramentas serão mantidas, integradas ou precisarão de ajustes.'),
            ('A IA vai falar com meus clientes no lugar do vendedor?', 'Só onde você decidir. A IA pode cuidar da primeira resposta, da pesquisa e do registro, e o vendedor conduz a negociação.'),
            ('Quanto custa?', 'O preço é fechado por projeto e depende do escopo. Ele vem na proposta, depois da sessão gratuita de 30 minutos.'),
        ],
    },
    {
        'slug': 'workshops-de-ia',
        'nome': 'Workshops de IA',
        'icone': 'icon-workshop',
        'area': 'Equipe',
        'title': 'Workshop de IA para empresas | Duck Flow',
        'description': 'Treinamento prático de IA para equipes, com situações reais da empresa e as ferramentas que o time já usa. Turmas fechadas, presenciais na Serra Gaúcha ou online.',
        'h1': 'Workshops de IA<br><em>com o trabalho real da equipe</em>',
        'lede': 'Sua equipe já testou IA, mas ainda não sabe onde aplicá-la no dia a dia? Treinamos o time com situações da própria empresa e as ferramentas que ele já usa.',
        'resumo': 'Treinamento prático com situações reais da empresa, para a IA entrar na rotina do time.',
        'tags': ['Turmas fechadas', 'Prática', 'Material'],
        'sinais': [
            ('Cada um usa de um jeito.', 'Alguns usam IA todo dia, outros nunca abriram, e ninguém sabe o que funciona.'),
            ('Medo de expor dados.', 'Sem regras claras, o time evita a IA ou usa sem cuidado com informações de clientes.'),
            ('O curso não virou rotina.', 'Os exemplos da aula não tinham relação com o trabalho de ninguém.'),
        ],
        'entregas': [
            ('Diagnóstico da turma', 'Antes do workshop, levantamos as tarefas da equipe e quanto cada área já usa IA.'),
            ('Prática com casos reais', 'Os exercícios usam documentos, processos e perguntas da própria empresa.'),
            ('Regras de uso', 'Orientação sobre o que pode ir para a IA e como cuidar dos dados de clientes.'),
            ('Material de consulta', 'Prompts e roteiros testados em aula para a equipe reutilizar depois.'),
        ],
        'aplicacoes_titulo': 'O que a equipe pratica',
        'aplicacoes': ['Pedidos claros para a IA', 'Resumo de reuniões, documentos e e-mails', 'Propostas e respostas em menos tempo', 'Análise de planilhas com IA', 'Tarefas que valem automação', 'Uso de IA sem expor dados sensíveis'],
        'faq': [
            ('A equipe precisa saber usar IA antes?', 'Não. O diagnóstico antes da aula mostra o nível da turma, e os exercícios são ajustados a ele.'),
            ('O workshop é presencial ou online?', 'Os dois. Em Canela, Gramado, Nova Petrópolis e na Serra Gaúcha, podemos ir até a empresa. Para outras regiões, o workshop é online.'),
            ('Quanto custa?', 'O valor depende do tamanho da turma e da duração, e vem na proposta depois da sessão gratuita de 30 minutos.'),
        ],
    },
]

PROCESSO = [
    ('Mapa do gargalo', 'Entendemos como o trabalho acontece hoje, onde ele trava e o que vale resolver primeiro.', 'Grátis · 30 min'),
    ('Proposta', 'Você recebe o que será feito, o prazo e um preço fechado para decidir com clareza.', ''),
    ('Construção e entrega', 'Construímos e testamos o sistema no seu fluxo, com atualizações semanais até a entrada em produção.', ''),
    ('Gestão contínua', 'Monitoramos o sistema, ajustamos fluxos e evoluímos a solução conforme a operação muda.', ''),
]


def esc(text):
    return html.escape(text, quote=True)


def em_frase(nome):
    return nome if nome.startswith('IA') else nome[0].lower() + nome[1:]


def icon(name):
    return f'<svg class="icon" aria-hidden="true" focusable="false"><use href="#{name}"></use></svg>'


def sprite():
    source = (ROOT / 'index.html').read_text(encoding='utf-8')
    match = re.search(r'<svg class="icon-sprite".*?</defs></svg>', source, re.S)
    return match.group(0)


def pill_html(texto):
    return f' <span class="pill">{esc(texto)}</span>' if texto else ''


def whatsapp(texto):
    return f'https://wa.me/{WHATSAPP}?text={quote(texto)}'


def header(root):
    return f'''<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header" id="topo"><div class="container header-inner">
<a class="brand" href="{root}" aria-label="Duck Flow, página inicial"><img src="{root}assets/brand/logo-com-texto-white.webp" width="1600" height="332" alt="Duck Flow"></a>
<nav class="main-nav" id="main-nav" aria-label="Navegação principal"><a href="{root}servicos/">Serviços</a><a href="{root}#como-funciona">Como funciona</a><a href="{root}#diferenciais">Por que a Duck Flow</a><a href="{root}#quem-somos">Quem somos</a><a href="{root}#perguntas">Perguntas</a></nav>
<a class="button button-primary header-cta" href="{root}#contato">Vamos conversar {icon('icon-arrow-up-right')}</a>
<button class="menu-toggle" type="button" aria-controls="main-nav" aria-expanded="false" aria-label="Abrir menu"><span></span><span></span></button>
</div></header>'''


def footer(root):
    links = ''.join(f'<a href="{root}servicos/{s["slug"]}/">{esc(s["nome"])}</a>' for s in SERVICOS)
    return f'''<footer class="site-footer"><div class="container"><div class="footer-main"><div><a href="{root}" class="footer-brand" aria-label="Duck Flow, página inicial"><img src="{root}assets/brand/logo-com-texto-dark.webp" alt="Duck Flow" width="220" height="90"></a><p>IA aplicada ao negócio.<br>Da estratégia ao sistema em produção.</p></div><div class="footer-links"><div><strong>Serviços</strong>{links}<a href="{root}servicos/">Todos os serviços</a></div><div><strong>Explore</strong><a href="{root}#como-funciona">Como funciona</a><a href="{root}#diferenciais">Por que a Duck Flow</a><a href="{root}#quem-somos">Quem somos</a><a href="{root}#perguntas">Perguntas</a></div><div><strong>Contato</strong><a href="mailto:lmiguelcolombo@gmail.com">E-mail</a><a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener noreferrer">WhatsApp</a><span>Canela · Rio Grande do Sul</span></div></div></div><div class="footer-bottom"><span>© 2026 Duck Flow · 57.697.808 Luís Miguel Colombo · CNPJ 57.697.808/0001-97</span><a href="#topo">Voltar ao topo {icon('icon-arrow-up')}</a></div></div></footer>'''


def breadcrumb(root, trilha):
    items = []
    for nome, href in trilha:
        if href is None:
            items.append(f'<li aria-current="page">{esc(nome)}</li>')
        else:
            items.append(f'<li><a href="{root}{href}">{esc(nome)}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Você está em"><ol>{"".join(items)}</ol></nav>'


def breadcrumb_ld(trilha, url):
    elementos = []
    for posicao, (nome, href) in enumerate(trilha, 1):
        item = {'@type': 'ListItem', 'position': posicao, 'name': nome, 'item': SITE + href if href is not None else url}
        elementos.append(item)
    return {'@type': 'BreadcrumbList', 'itemListElement': elementos}


def faq_html(perguntas, prefixo):
    rows = []
    for i, (pergunta, resposta) in enumerate(perguntas, 1):
        rows.append(f'<div class="faq-row"><button class="faq-q" type="button" id="{prefixo}-q-{i}" aria-expanded="false" aria-controls="{prefixo}-a-{i}"><span>{esc(pergunta)}</span><span class="faq-icon" aria-hidden="true"></span></button><div class="faq-answer" id="{prefixo}-a-{i}" role="region" aria-labelledby="{prefixo}-q-{i}" aria-hidden="true"><div class="faq-answer-inner"><p>{esc(resposta)}</p></div></div></div>')
    return '\n'.join(rows)


def cta(root, eyebrow_num, mensagem):
    return f'''<section class="contact-section cta-band" id="contato" aria-labelledby="contato-title"><div class="container"><div class="contact-heading" data-text-fade-child><span class="eyebrow light">{eyebrow_num} / Próximo passo</span><h2 id="contato-title" data-text-reveal>Traga o problema.<br><em>Encontramos o começo.</em></h2><p>Em 30 minutos, você mostra onde o trabalho trava. Juntos, identificamos um próximo passo e avaliamos se IA ou automação faz sentido.</p><div class="cta-actions"><a class="button button-orange" href="{root}#contato">Agendar sessão gratuita {icon('icon-arrow-up-right')}</a><a class="button button-outline" href="{esc(whatsapp(mensagem))}" target="_blank" rel="noopener noreferrer">Falar no WhatsApp {icon('icon-arrow-up-right')}</a></div></div></div></section>'''


def page(root, url, title, description, ld, corpo):
    ld_json = json.dumps({'@context': 'https://schema.org', '@graph': ld}, ensure_ascii=False, separators=(',', ':'))
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f7f5ef">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="icon" href="{root}favicon.ico" sizes="any" type="image/x-icon">
<link rel="icon" href="{root}assets/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{root}assets/favicons/apple-touch-icon.png" sizes="180x180">
<link rel="manifest" href="{root}assets/favicons/site-manifest.json">
<link rel="preload" href="{root}assets/brand/familjen-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/brand/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:url" content="{url}"><meta property="og:site_name" content="Duck Flow">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}assets/brand/logo-com-texto-dark.webp">
<meta name="twitter:card" content="summary_large_image">
<script>
if (!matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {{
  document.documentElement.classList.add('motion-ready');
  addEventListener('load', () => {{
    if (!document.documentElement.classList.contains('motion-initialized')) {{
      document.documentElement.classList.remove('motion-ready');
    }}
  }}, {{once: true}});
}}
</script><link rel="stylesheet" href="{root}assets/css/site.css?v={ASSET_VERSION}">
<script type="application/ld+json">
{ld_json}
</script>
</head>
<body>
{sprite()}
{header(root)}
<main id="conteudo">
{corpo}
</main>
{footer(root)}
<script src="{root}assets/js/site.js?v=20260926c" defer></script>
<script src="{root}assets/js/text-motion.js?v={ASSET_VERSION}" defer></script>
</body>
</html>
'''


def servico_page(s, indice):
    root = '../../'
    url = f'{SITE}servicos/{s["slug"]}/'
    trilha = [('Início', ''), ('Serviços', 'servicos/'), (s['nome'], None)]
    num = f'{indice:02d}'
    sinais = ''.join(f'<div><span class="signal-number">{i:02d}</span><strong>{esc(t)}</strong><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(s['sinais'], 1))
    entregas = ''.join(f'<article><span>{i:02d}</span><h3>{esc(t)}</h3><p>{esc(p)}</p></article>' for i, (t, p) in enumerate(s['entregas'], 1))
    aplicacoes = ''.join(f'<li>{icon("icon-check")}{esc(a)}</li>' for a in s['aplicacoes'])
    processo = ''.join(
        f'<article><span class="process-num">{i:02d}</span><div><h3>{esc(t)}{pill_html(pill)}</h3><p>{esc(p)}</p></div><span class="process-arrow" aria-hidden="true">{icon("icon-arrow-up-right")}</span></article>'
        for i, (t, p, pill) in enumerate(PROCESSO, 1))
    outros = ''.join(
        f'<a href="{root}servicos/{o["slug"]}/"><span class="service-icon">{icon(o["icone"])}</span><strong>{esc(o["nome"])}</strong><span>{esc(" · ".join(o["tags"]))} {icon("icon-arrow-up-right")}</span></a>'
        for o in SERVICOS if o is not s)
    corpo = f'''<section class="page-hero" aria-labelledby="hero-title"><div class="container">
{breadcrumb(root, trilha)}
<span class="eyebrow">Serviço {num} / {esc(s["area"])}</span><h1 id="hero-title" data-text-reveal>{s["h1"]}<span class="hero-period">.</span></h1><p class="hero-lede" data-text-fade>{esc(s["lede"])}</p><div class="hero-actions"><a class="button button-primary" href="#contato">Encontrar meu gargalo {icon('icon-arrow-up-right')}</a><a class="button button-outline" href="#entregas">O que entregamos {icon('icon-arrow-down')}</a></div><p class="hero-note"><span class="note-line"></span> Sessão inicial gratuita · 30 minutos · sem compromisso</p>
</div></section>
<section class="signal-strip" aria-label="Quando faz sentido"><div class="container signal-grid">{sinais}</div></section>
<section class="section services" id="entregas" aria-labelledby="entregas-title"><div class="container"><div class="section-heading" data-text-fade-child><div><span class="eyebrow">01 / O que entregamos</span><h2 id="entregas-title" data-text-reveal>O que você recebe<br><em>no projeto.</em></h2></div><p>{esc(s["resumo"])} Escopo, prazo e preço ficam definidos na proposta.</p></div><div class="deliver-grid">{entregas}</div></div></section>
<section class="dark-panel" aria-labelledby="aplicacoes-title"><div class="container dark-grid"><div class="dark-intro" data-text-fade-child><span class="eyebrow light">02 / Exemplos</span><h2 id="aplicacoes-title" data-text-reveal>{esc(s["aplicacoes_titulo"])}.</h2><p>Cada projeto começa pelo gargalo que você trouxer. Estes são pontos de partida comuns.</p></div><ul class="use-list">{aplicacoes}</ul></div></section>
<section class="section approach" aria-labelledby="processo-title"><div class="container"><div class="section-heading" data-text-fade-child><div><span class="eyebrow">03 / Como funciona</span><h2 id="processo-title" data-text-reveal>Do gargalo ao sistema<br><em>em produção.</em></h2></div><p>Você entende o que será construído, quanto custa e como a solução entra na rotina antes de assumir o projeto.</p></div><div class="process-list">{processo}</div></div></section>
<section class="section faq-section" aria-labelledby="faq-title"><div class="container faq-grid"><div><span class="eyebrow">04 / Perguntas frequentes</span><h2 id="faq-title" data-text-reveal>Perguntas sobre<br><em>{esc(em_frase(s["nome"]))}.</em></h2><p>Não encontrou a sua? Pergunte na sessão gratuita.</p></div><div class="faq-list">
{faq_html(s["faq"], s["slug"])}
</div></div></section>
<section class="section services" aria-labelledby="outros-title"><div class="container"><div class="section-heading" data-text-fade-child><div><span class="eyebrow">05 / Outros serviços</span><h2 id="outros-title" data-text-reveal>Os sistemas funcionam<br><em>melhor juntos.</em></h2></div><p>Muitos projetos combinam mais de uma frente. <a class="inline-link" href="{root}servicos/">Ver todos os serviços</a></p></div><div class="related-grid">{outros}</div></div></section>
{cta(root, "06", f"Olá, Duck Flow! Quero conversar sobre {s['nome']}.")}'''
    ld = [
        {'@type': 'Service', '@id': url + '#service', 'name': s['nome'], 'serviceType': s['nome'], 'description': s['description'], 'url': url,
         'provider': {'@id': SITE + '#organization'}, 'areaServed': ['Canela', 'Gramado', 'Nova Petrópolis', 'Serra Gaúcha', 'Brasil']},
        breadcrumb_ld(trilha, url),
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in s['faq']]},
    ]
    return page(root, url, s['title'], s['description'], ld, corpo)


def hub_page():
    root = '../'
    url = f'{SITE}servicos/'
    trilha = [('Início', ''), ('Serviços', None)]
    linhas = ''.join(
        f'<article><span class="service-icon">{icon(s["icone"])}</span><div><h2><a href="{s["slug"]}/">{esc(s["nome"])}</a></h2><p>{esc(s["resumo"])}</p></div><ul class="catalog-tags">{"".join("<li>" + pill_html(t).strip() + "</li>" for t in s["tags"])}</ul><a class="button button-outline" href="{s["slug"]}/" aria-label="Ver o serviço {esc(s["nome"])}">Ver serviço {icon("icon-arrow-up-right")}</a></article>'
        for s in SERVICOS)
    corpo = f'''<section class="page-hero" aria-labelledby="hero-title"><div class="container">
{breadcrumb(root, trilha)}
<span class="eyebrow">Serviços / IA + automação</span><h1 id="hero-title" data-text-reveal>Serviços de IA<br>e automação <em>para empresas</em><span class="hero-period">.</span></h1><p class="hero-lede" data-text-fade>Cinco frentes para tirar trabalho manual de vendas e operação. Você não precisa chegar sabendo qual contratar: na sessão gratuita, identificamos o gargalo e indicamos por onde começar.</p><div class="hero-actions"><a class="button button-primary" href="#contato">Encontrar meu gargalo {icon('icon-arrow-up-right')}</a></div><p class="hero-note"><span class="note-line"></span> Canela e Serra Gaúcha presencial · todo o Brasil remoto</p>
</div></section>
<section class="section approach" aria-label="Lista de serviços"><div class="container"><div class="catalog-list">{linhas}</div></div></section>
{cta(root, "02", "Olá, Duck Flow! Quero entender qual serviço faz sentido para a minha empresa.")}'''
    ld = [
        {'@type': 'CollectionPage', '@id': url, 'name': 'Serviços de IA e automação', 'url': url, 'isPartOf': {'@id': SITE + '#website'},
         'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i, 'url': f'{url}{s["slug"]}/', 'name': s['nome']} for i, s in enumerate(SERVICOS, 1)]}},
        breadcrumb_ld(trilha, url),
    ]
    return page(root, url, 'Serviços de IA e automação para empresas | Duck Flow',
                'Automação com IA, estruturação de dados, agentes de IA, IA para vendas e workshops. Preço fechado por projeto, presencial na Serra Gaúcha e remoto em todo o Brasil.',
                ld, corpo)


def main():
    destino = ROOT / 'servicos'
    destino.mkdir(exist_ok=True)
    (destino / 'index.html').write_text(hub_page(), encoding='utf-8')
    for indice, s in enumerate(SERVICOS, 1):
        pasta = destino / s['slug']
        pasta.mkdir(exist_ok=True)
        (pasta / 'index.html').write_text(servico_page(s, indice), encoding='utf-8')
    print(f'{len(SERVICOS) + 1} páginas geradas em {destino}')


if __name__ == '__main__':
    main()
