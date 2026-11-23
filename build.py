"""
Gerador estático do site Vinovare.

    python build.py

Lê os templates em src/templates e os dados em src/data e gera os arquivos
HTML na raiz do projeto (pronto para GitHub Pages ou qualquer hospedagem
estática). Requer: pip install jinja2
"""
import json
import os
import sys
from datetime import date
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, TemplateNotFound, pass_context, select_autoescape
from markupsafe import Markup, escape

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'src', 'data'))

import site_data as S  # noqa: E402
from artigos import ARTIGOS, CATEGORIAS, POR_SLUG as ARTIGO  # noqa: E402
from procedimentos import (AREAS, DESTAQUES, PROCEDIMENTOS, PROTOCOLOS_AREA,  # noqa: E402
                           POR_SLUG as PROC)

SITE_URL = 'https://vinovare.com.br/'

with open(os.path.join(ROOT, 'assets', 'img', 'manifest.json'), encoding='utf-8') as f:
    MANIFEST = json.load(f)


# ----------------------------------------------------------------- helpers
def wa(text='Olá! Gostaria de agendar uma avaliação com a Dra. Karinie Marinho.'):
    return f'https://wa.me/{S.WHATSAPP}?text={quote(text)}'


def maps_embed():
    return f'https://www.google.com/maps?q={quote(S.MAPS_QUERY)}&output=embed'


def maps_link():
    return f'https://www.google.com/maps/search/?api=1&query={quote(S.MAPS_QUERY)}'


@pass_context
def img(ctx, name, alt='', cls='', sizes='(max-width: 900px) 100vw, 50vw', eager=False, attrs=''):
    """<img> responsivo com srcset a partir do manifest de imagens otimizadas."""
    root = ctx.get('root', '')
    m = MANIFEST[name]
    ws = m['sizes']
    srcset = ', '.join(f'{root}assets/img/{name}-{w}.webp {w}w' for w in ws)
    w0 = ws[0]
    h0 = round(m['h'] * w0 / m['w'])
    extra = ' loading="eager" fetchpriority="high"' if eager else ' loading="lazy"'
    cls_attr = f' class="{cls}"' if cls else ''
    return Markup(
        f'<img src="{root}assets/img/{name}-{w0}.webp" srcset="{srcset}" sizes="{sizes}" '
        f'width="{w0}" height="{h0}" alt="{escape(alt)}"{cls_attr} decoding="async"{extra} {attrs}>'
    )


@pass_context
def img_url(ctx, name, size=None):
    ws = MANIFEST[name]['sizes']
    w = size if size in ws else ws[-1]
    return f'{ctx.get("root", "")}assets/img/{name}-{w}.webp'


def procs(slugs):
    return [PROC[s] for s in slugs if s in PROC]


def arts(slugs):
    return [ARTIGO[s] for s in slugs if s in ARTIGO]


def por_area(area):
    return [p for p in PROCEDIMENTOS if area in p['areas']]


env = Environment(
    loader=FileSystemLoader(os.path.join(ROOT, 'src', 'templates')),
    autoescape=select_autoescape(['html']),
    trim_blocks=True, lstrip_blocks=True,
)
env.globals.update(
    S=S, wa=wa, img=img, img_url=img_url, maps_embed=maps_embed, maps_link=maps_link,
    AREAS=AREAS, PROCEDIMENTOS=PROCEDIMENTOS, PROC=PROC, procs=procs, por_area=por_area,
    DESTAQUES=DESTAQUES, PROTOCOLOS_AREA=PROTOCOLOS_AREA, ARTIGOS=ARTIGOS, ARTIGO=ARTIGO,
    arts=arts, CATEGORIAS=CATEGORIAS, ano=date.today().year, SITE_URL=SITE_URL,
)

BUILT = []


def render(template, out, **ctx):
    depth = out.count('/')
    ctx.setdefault('root', '../' * depth)
    ctx.setdefault('canonical', SITE_URL + ('' if out == 'index.html' else out))
    try:
        tpl = env.get_template(template)
    except TemplateNotFound:
        print(f'  [aviso] template ausente: {template}')
        return
    html = tpl.render(**ctx)
    path = os.path.join(ROOT, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    BUILT.append(out)


def quiz_data():
    """Dados enxutos para o questionário 'Descubra seu cuidado'."""
    def mini(slug):
        p = PROC[slug]
        return {'slug': slug, 'nome': p['nome'], 'curto': p['curto'], 'tipo': p['tipo'], 'img': p['img']}
    def mini_art(slug):
        a = ARTIGO[slug]
        return {'slug': slug, 'titulo': a['titulo'], 'categoria': a['categoria'], 'img': a['img'],
                'leitura': a['leitura']}
    return {'procs': {p['slug']: mini(p['slug']) for p in PROCEDIMENTOS},
            'arts': {a['slug']: mini_art(a['slug']) for a in ARTIGOS}}


def main():
    pages = [
        ('pages/index.html', 'index.html', 'home',
         'Dermatologia e medicina personalizada em Brasília',
         'Vinovare Medicina Personalizada: clínica de dermatologia da Dra. Karinie Marinho na Asa Sul, Brasília. '
         'Tratamentos faciais, corporais e capilares com avaliação integral e protocolos individualizados.'),
        ('pages/tratamentos.html', 'tratamentos.html', 'tratamentos', 'Tratamentos faciais, corporais e capilares',
         'Conheça os tratamentos da Vinovare: rejuvenescimento facial, lasers, bioestimuladores, contorno corporal e '
         'medicina capilar, sempre a partir de uma avaliação médica.'),
        ('pages/dra-karinie.html', 'dra-karinie.html', 'dra', 'Dra. Karinie Marinho — Dermatologista',
         'Conheça a Dra. Karinie Marinho, médica dermatologista (CRM/DF 19437 · RQE 20108) e fundadora da Vinovare '
         'Medicina Personalizada.'),
        ('pages/clinica.html', 'clinica.html', 'clinica', 'Tour pela clínica',
         'Conheça os ambientes da Vinovare na Asa Sul: recepção, consultório e salas de procedimentos pensados '
         'para o seu conforto e segurança.'),
        ('pages/descubra.html', 'descubra.html', 'descubra', 'Descubra seu cuidado',
         'Responda a algumas perguntas e descubra conteúdos e tratamentos alinhados aos seus interesses. '
         'Uma experiência de orientação — sem diagnóstico.'),
        ('pages/conteudos.html', 'conteudos.html', 'conteudos', 'Conteúdo dermatológico',
         'Orientações sobre cuidados com a pele, saúde capilar, prevenção e tratamentos dermatológicos, '
         'pela Dra. Karinie Marinho.'),
        ('pages/agendamento.html', 'agendamento.html', 'agendamento', 'Agende sua avaliação',
         'Agende sua consulta com a Dra. Karinie Marinho pelo WhatsApp ou solicite um horário online.'),
        ('pages/contato.html', 'contato.html', 'contato', 'Localização e contato',
         'Vinovare Medicina Personalizada — Centro Médico Júlio Adnet, SEPS 709/909, Asa Sul, Brasília. '
         'Horários, mapa e canais de atendimento.'),
        ('pages/404.html', '404.html', 'erro', 'Página não encontrada', 'Página não encontrada.'),
    ]
    for tpl, out, page, title, desc in pages:
        render(tpl, out, page=page, title=title, description=desc,
               quiz=quiz_data() if page == 'descubra' else None)

    for p in PROCEDIMENTOS:
        area = p['areas'][0]
        render('procedimento.html', f'procedimentos/{p["slug"]}.html', page='tratamentos', p=p,
               area=area, title=p['nome'], description=p['curto'], og_img=p['img'],
               relacionados=procs(p['relacionados']))

    for a in ARTIGOS:
        rel = arts(a['relacionados'])
        rel += [x for x in ARTIGOS if x is not a and x not in rel]
        render('artigo.html', f'conteudos/{a["slug"]}.html', page='conteudos', a=a, title=a['titulo'],
               description=a['resumo'], relacionados=rel[:3], og_img=a['img'])

    # sitemap + robots
    urls = [SITE_URL + ('' if b == 'index.html' else b) for b in BUILT if b != '404.html']
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{u}</loc></url>' for u in urls]
    sm.append('</urlset>')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(sm) + '\n')
    with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n')

    print(f'{len(BUILT)} páginas geradas.')


if __name__ == '__main__':
    main()
